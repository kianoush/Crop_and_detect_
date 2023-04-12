


import numpy as np
import imutils
import time
import cv2
import pyshine as ps
from ffpyplayer.player import MediaPlayer
from Ui_videoPlayer03 import *

class Computer_Vision:
    CNT = 0
    FRAMES_COUNT = 20
    ST = 0
    FPS = 0

    def __init__(self, video, ml_label, volume, parent=None):
        # define model
        self.fileAddress = ''
        self.video = video
        self.prototxt_path = "./deploy.prototxt"
        self.model_path = "./mobilenet_iter_73000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(self.prototxt_path, self.model_path)
        self.ml_label = ml_label
        self.points = []
        self.crop_image_labels = []
        self.volume = volume
###########################################################################

#############################################################################

        # initialize the list of class labels MobileNet SSD was trained to detect
        self.classes = ["background", "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                        "sofa", "train", "tvmonitor"]


    def process_frame_MobileNetSSD( self, image, ML_label):
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        (H, W) = image.shape[:2]

        # convert the frame to a blob and pass the blob through the
        # network and obtain the detections
        blob = cv2.dnn.blobFromImage(image, size=(300, 300), ddepth=cv2.CV_8U)

        self.net.setInput(blob, scalefactor=1.0 / 127.5, mean=[127.5, 127.5, 127.5])
        detections = self.net.forward()

        # loop over the detections`
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated
            # with the prediction
            confidence = detections[0, 0, i, 2]
            # filter out weak detections by ensuring the `confidence`
            # is greater than the minimum confidence
            if confidence > .8:
                # extract the index of the class label from the
                # detections list
                idx = int(detections[0, 0, i, 1])
                # if the class label is not a car, ignore it
                if self.classes[idx] != ML_label:
                    continue
                # compute the (x, y)-coordinates of the bounding box
                # for the object
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 250, 0), 2)

        return image

    def process_crop_image(self, image):
        # (H, W) = image.shape
        # print(H, W)
        # convert the frame to a blob and pass the blob through the
        # network and obtain the detections
        blob = cv2.dnn.blobFromImage(image, size=(300, 300), ddepth=cv2.CV_8U)
        self.net.setInput(blob, scalefactor=1.0 / 127.5, mean=[127.5, 127.5, 127.5])
        detections = self.net.forward()
        for label in self.classes:
        # loop over the detections`
            for i in np.arange(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated
                # with the prediction
                confidence = detections[0, 0, i, 2]
                # filter out weak detections by ensuring the `confidence`
                # is greater than the minimum confidence
                if confidence > .8:
                    # extract the index of the class label from the
                    # detections list
                    idx = int(detections[0, 0, i, 1])
                    # if the class label is not a car, ignore it
                    if self.classes[idx] == label:
                        self.crop_image_labels.append(label)
                    else:
                        continue
                    # compute the (x, y)-coordinates of the bounding box
                    # for the object
                    # box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                    # (startX, startY, endX, endY) = box.astype("int")
                    # cv2.rectangle(image, (startX, startY), (endX, endY), (0, 250, 0), 2)


    def check_file(self, fileAddress: str) -> str:
        if fileAddress:
            self.fileAddress = fileAddress
            return fileAddress

    def get_video(self):

        if self.fileAddress:
            #print(self.filename)
            self.video = cv2.VideoCapture(self.fileAddress)
            self.player = MediaPlayer(self.fileAddress)
        return self.video

    def get_audio(self, v):
        self.volume = v
        self.player.set_volume(self.volume / 100)

    def set_mute(self):
        playerVolume = self.player.get_volume()
        #print('Volume = ', playerVolume)
        if playerVolume == 0.0:
            self.player.set_volume(1.0)
            #print('Should now be unmuted')
        else:
            self.player.set_volume(0.0)
            #print('Should now be muted')

    def pause_audio(self, status = False):
        self.player.set_pause(status)

    def stop_audio(self):
        print('stop_audio')
        self.player.close_player()

    def get_duration(self, vid):
        return int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    def process(self, vid):
        img, image = vid.read()
        # if not image:
        #     self.ui.stop_()
        #     print("End of video")

        image = self.process_frame_MobileNetSSD(image, self.ml_label)
        image = cv2.resize(image, (617, 375), interpolation= cv2.INTER_LINEAR)
        if self.points:
            image = self.create_rectangle(self.points, image)
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            print(x1, y1,  x2, y2)

            image01 = image[(y1-23):y2, (x1-57):(x2-20)]
            # image01 = image[0:200, 0:100, :]
            #print(image01.shape)
            self.process_crop_image(image01)
            if self.crop_image_labels:
                #print(self.crop_image_labels)
                #cv2.imshow('',image01)
                self.ml_label = self.crop_image_labels[0]
            self.CNT += 1
            if self.CNT >= 100:
                self.points = []
                self.CNT = 0
        if Computer_Vision.CNT == self.FRAMES_COUNT:
            try:  # To avoid divide by 0 we put it in try except
                self.FPS = round(self.FRAMES_COUNT / (time.time() - self.ST))
                self.ST = time.time()
                self.process_frame_MobileNetSSD(image, self.ml_label)
            except:
                pass
        self.image = image
        return image

    def create_rectangle(self, points, image):
        point1, point2 = points
        x1, y1 = point1
        x2, y2 = point2
        cv2.rectangle(image, (x1-(57), y1-(23)), (x2-20, y2), (0, 0, 255), 2)
        return image

