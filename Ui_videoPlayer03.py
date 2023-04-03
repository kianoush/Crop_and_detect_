# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_videoPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog, QLineEdit, QTextBrowser
from PyQt5.QtGui import QIcon, QPalette, QImage
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, Q_ARG, QAbstractItemModel,
                          QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, QObject, Qt,
                          QThread, QTime, QUrl)
from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QMediaContent,
                                QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtMultimediaWidgets import QVideoWidget

import numpy as np
import imutils
import time
import cv2
import pyshine as ps
import CV
from CV import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 548)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 530))
        MainWindow.setMaximumSize(QtCore.QSize(900, 550))

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(850, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(850, 1500))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 860, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(860, 530))
        self.frame.setMaximumSize(QtCore.QSize(860, 530))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(830, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(380, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(450, 300))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(445, 295))

        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setMouseTracking(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./Img01"))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setEnabled(True)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 300))
        self.frame_3.setMaximumSize(QtCore.QSize(180, 450))
        self.frame_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_3.setMouseTracking(False)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listView = QtWidgets.QListView(self.frame_9)
        self.listView.setObjectName("listView")
        self.gridLayout_5.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_9, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(180, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(180, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(160, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(160, 40))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_11.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_11.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_11.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Blue/Blue/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.verticalLayout_2.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_9.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_9.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_9.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Gray/Gray/crop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_10.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.frame_8, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 3, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_6)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 5)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(830, 70))
        self.frame_5.setMaximumSize(QtCore.QSize(830, 70))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Blue/Blue/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Gray/Gray/stop-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Blue/Blue/skip-back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setText("")
        self.icon5 = QtGui.QIcon()
        self.icon5.addPixmap(QtGui.QPixmap(":/Blue/Blue/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(self.icon5)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.gridLayout_6.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Blue/Blue/skip-forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_5.setMinimumSize(QtCore.QSize(24, 24))
        self.pushButton_5.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_5.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Blue/Blue/volume-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 0, 5, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_5)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(70, 0))
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        spacerItem1 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)
        self.icon8 = QtGui.QIcon()
        self.icon8.addPixmap(QtGui.QPixmap(":/Blue/Blue/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        self.pushButton_6.clicked.connect(self.loadVideo) # type: ignore
        self.pushButton.clicked.connect(self.stop_) # type: ignore
        self.pushButton_3.clicked.connect(self.playvideo) # type: ignore
        self.pushButton_2.clicked.connect(self.default_address) # type: ignore
        self.pushButton_4.clicked.connect(self.label.clear) # type: ignore
        self.pushButton_5.clicked.connect(self.label.clear) # type: ignore
        self.horizontalSlider_2.rangeChanged['int','int'].connect(self.label.clear) # type: ignore
        self.comboBox.activated['int'].connect(self.label.clear) # type: ignore
        self.pushButton_7.clicked.connect(self.label.clear) # type: ignore
        self.pushButton_9.clicked.connect(self.crop_image_button) # type: ignore
        self.lineEdit.textEdited['QString'].connect(self.label.setText) # type: ignore
        self.pushButton_11.clicked.connect(self.text_box) # type: ignore
        self.horizontalSlider.sliderMoved.connect(self.set_position) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ################################################################################

        self.le = QLineEdit()
        self.tmp = None  # Will hold the temporary image for display
        self.brightness_value_now = 0  # Updated brightness value
        self.blur_value_now = 0  # Updated blur value
        self.fps = 0
        self.start = False
        self.stop = False
        self.pause = False
        self.ML_label = None
        self.image = None
        self.drawing = False
        self.point1 = ()
        self.point2 = ()
        self.crop = False
        self.position = 0
        self.video = None
        self.address = True

        #self.main= MainWindow()       #############################################################################

        self.computer_vision = Computer_Vision(None, None)


        # define model
        self.prototxt_path = "./deploy.prototxt"
        self.model_path = "./mobilenet_iter_73000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(self.prototxt_path, self.model_path)
        self.p = 0

        # initialize the list of class labels MobileNet SSD was trained to detect
        self.classes = ["background", "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                        "sofa", "train", "tvmonitor"]
        ################################################################################

    def default_address(self):
        if self.address:
            filename = 'E:/pro/Python/Project for CV/file1.mp4'
            self.computer_vision.check_file(filename)
            self.pushButton_3.setEnabled(True)

    def crop_image_button(self):
        """ This function will allo o get 2 points for cropping image"""
        self.crop = True

    def loadVideo(self):
        """ This function will load the camera device or video file"""
        filename = QFileDialog.getOpenFileName(filter="Video (*.*)")[0]
        self.computer_vision.check_file(filename)
        if self.computer_vision.filename:
            self.pushButton_3.setEnabled(True)

    def playvideo(self):

        """ This function obtain the image and set it to label using the setPhoto function
        """
        self.startedStatus()
        self.vid = self.computer_vision.get_video()
        self.computer_vision.video = self.vid
        duration = self.computer_vision.get_duration(self.vid)
        self.horizontalSlider.setRange(0, duration)

        if self.position:
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, self.position)
            #self.set_position()


        while self.vid.isOpened():
            if self.vid:
                QtWidgets.QApplication.processEvents()
                image = self.computer_vision.process(self.vid, self.ML_label)
                self.computer_vision.CNT += 1

                cv2.waitKey(0) & 0xFF
                if self.pause == True and self.start == False and self.stop == False:
                    self.pushButton_3.setIcon(self.icon5)
                    break

                if self.stop == True:
                    self.pushButton_3.setIcon(self.icon5)
                    self.label.setPixmap(QtGui.QPixmap("./Img01"))
                    self.position = 0
                    self.set_position()
                    self.stop = False
                    self.start = False
                    break

                # Update the slider bar
                self.position = int(self.vid.get(cv2.CAP_PROP_POS_FRAMES))
                self.set_position()
                # Update the image
                self.update(image)
            else:
                break

    def startedStatus(self):
        if not self.start:
            self.start = True
            self.pause = False
            self.stop = False
            self.pushButton_3.setIcon(self.icon8)

        elif self.start:
            self.start = False
            self.pause = True
            self.stop = False
            self.pushButton_3.setIcon(self.icon5)
        #print('started: ', self.start, '  stop: ', self.stop, '   pause: ', self.pause, )


    def stop_(self):
        if self.pause:
            self.label.setPixmap(QtGui.QPixmap("./Img01"))
            self.position = 0
            self.set_position()
            self.stop = False
            self.start = False
        else:
            self.stop = True
            self.start = False
            self.pause = False

        print(self.computer_vision.points , self.crop)
        self.computer_vision.points = []
        self.crop = False

        print('Loop break')

    def position_changed(self):
        self.horizontalSlider.setValue(self.position)

    def set_position(self):
        self.horizontalSlider.setValue(self.position)

    def text_box(self):
        self.ML_label = self.lineEdit.text().lower()
        self.computer_vision.ml_label = self.ML_label
        print(self.ML_label)

    def text_clear(self):
        self.ML_label = 'None'
        print('Clear')
        self.lineEdit.clear()

    def setPhoto(self, image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image, width=550)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))




    def update(self, img):
        """ This function will update the photo according to the
            current values of blur and brightness and set it to photo label.
        """

        # Here we add display text to the image
        text = 'FPS: ' + str(self.computer_vision.FPS)
        # img = ps.putBText(img, text, text_offset_x=20, text_offset_y=30, vspace=20, hspace=10, font_scale=1.0,
        #                   background_RGB=(10, 20, 222), text_RGB=(255, 255, 255))
        # text = str(time.strftime("%H:%M %p"))
        # img = ps.putBText(img, text, text_offset_x=img.shape[1] - 180, text_offset_y=30, vspace=20,
        #                   hspace=10,
        #                   font_scale=1.0, background_RGB=(228, 20, 222), text_RGB=(255, 255, 255))
        # text = f"Label: {self.ML_label}"
        # img = ps.putBText(img, text, text_offset_x=80, text_offset_y=425, vspace=20, hspace=10, font_scale=1.0,
        #                   background_RGB=(20, 210, 4), text_RGB=(255, 255, 255))
        self.setPhoto(img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "Open"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1.0 x"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1.5 x"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2.0 x"))
        self.pushButton_7.setText(_translate("MainWindow", "Full Screen"))
        self.pushButton_8.setText(_translate("MainWindow", "Color Options"))
import icons01_rc


class MainWindow(QMainWindow, QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.ui.centralwidget.setMouseTracking(True)
        self.ui.frame.setMouseTracking(True)
        self.ui.frame_2.setMouseTracking(True)
        self.ui.frame_4.setMouseTracking(True)
        self.ui.label.setMouseTracking(True)
        self.crop_points = []

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        print('x: ', x)
        print('y: ', y)
        if self.ui.crop:
            self.crop_points.append((x, y))
            if len(self.crop_points) > 1:
                self.ui.computer_vision.points = self.crop_points
                # self.ui.computer_vision.create_rectangle( self.crop_points)
                self.crop_points = []
                self.ui.crop = False
    def keyPressEvent(self, e):  # doesnt work when app is in background
        if e.key() == Qt.key_Escape:
            self.close()
            print(1)

    def closeEvent(self, event):
        self.stylusProximityControlOff()
        self.deleteLater()

