


import numpy as np
import imutils
import time
import cv2
import pyshine as ps



class Computer_Vision():
    CNT = 0
    FRAMES_COUNT = 20
    ST = 0
    FPS = 0
    # p1 = None
    # p2 = None
    # p3 = None
    # p4 = None

    def __init__(self, video, ml_label):
        # define model
        self.filename = ''
        self.video = video
        self.prototxt_path = "./deploy.prototxt"
        self.model_path = "./mobilenet_iter_73000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(self.prototxt_path, self.model_path)
        self.p = 0
        # self.p1 = None
        # self.p2 = None
        # self.p3 = None
        # self.p4 = None
        self.ml_label = ml_label




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


    def check_file(self, filename: str) -> str:
        if filename:
            self.filename = filename
            return filename

    def get_video(self):
        if self.filename:
            #print(self.filename)
            self.video = cv2.VideoCapture(self.filename)
        return self.video

    def get_duration(self, vid):
        return int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    def proccess(self, vid, ml_label):
        img, image = vid.read()
        image = self.process_frame_MobileNetSSD(image, ml_label)
        if Computer_Vision.CNT == self.FRAMES_COUNT:
            try:  # To avoid divide by 0 we put it in try except
                self.FPS = round(self.FRAMES_COUNT / (time.time() - self.ST))
                self.ST = time.time()
                self.CNT = 0
                print('image')
                self.process_frame_MobileNetSSD(image, ml_label)
            except:
                pass
        return image

def create_rectangle(self, points):
        image = self.proccess(self.video, self.ml_label)

        point1, point2 = points
        # x1, y1 = point1
        # x2, y2 = point2

        cv2.rectangle(image, point1, point2, (0, 0, 255), 4)