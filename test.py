from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

import sys
import time


class ChannelModifier(QWidget):


    def __init__(self):
        super(ChannelModifier, self).__init__()
        loadUi("ChannelModifier.ui", self)

        self.setFixedSize(500, 500)
        #self.af = af
        # self.play = False
        self.posLabel.setText("0:00")
        self.start_time = 0
        self.elapsed_time = 0

        if self.af.get_thumb_path():
            self.thumb.setPixmap(QPixmap(self.af.get_thumb_path()))
        else:
            self.thumb.setText(self.af.get_title())

        self.player = QMediaPlayer()
        url = QUrl.fromLocalFile(self.af.get_path())
        self.content = QMediaContent(url)
        self.player.setMedia(self.content)
        self.player.positionChanged.connect(self.change_position)
        self.player.durationChanged.connect(self.change_duration)

        self.playPauseButton.clicked.connect(self.play_pause_player)
        self.stopButton.clicked.connect(self.stop_player)
        self.volumeSlider.valueChanged.connect(self.change_volume)
        self.posSlider.sliderMoved.connect(self.set_position)


    def set_time_label(self):
        t = self.elapsed_time
        dur_in_secs = self.af.get_duration()[0] * 60 + self.af.get_duration()[1]
        while t < dur_in_secs:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.posLabel.setText(timer)
            time.sleep(1)
            t += 1


    def change_position(self, position):
        self.posSlider.setValue(position)


    def change_duration(self, duration):
        self.posSlider.setRange(0, duration)
        # self.player.duration() = 217286 in millisecs!!


    def set_position(self, position):
        self.player.setPosition(position)


    def stop_player(self):
        self.player.stop()
        self.posLabel.setText("0:00")
        self.start_time = 0
        self.elapsed_time = 0


    def change_volume(self):
        vol = self.volumeSlider.value()
        self.player.setVolume(vol)


from PyQt5 import QtCore, QtGui, QtWidgets

# ChannelModifier.py
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(302, 261)
        self.playPauseButton = QtWidgets.QPushButton(Form)
        self.playPauseButton.setGeometry(QtCore.QRect(10, 170, 111, 41))
        self.playPauseButton.setObjectName("playPauseButton")
        self.thumb = QtWidgets.QLabel(Form)
        self.thumb.setGeometry(QtCore.QRect(20, 20, 211, 131))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.thumb.setFont(font)
        self.thumb.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(165, 165, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "font: 75 14pt \"Cantarell\";")
        self.thumb.setText("")
        self.thumb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.thumb.setObjectName("thumb")
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(130, 170, 111, 41))
        self.stopButton.setObjectName("stopButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 10, 26, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.volumeSlider = QtWidgets.QSlider(self.layoutWidget)
        self.volumeSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.volumeSlider.setObjectName("volumeSlider")
        self.verticalLayout.addWidget(self.volumeSlider)
        self.volumeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.verticalLayout.addWidget(self.volumeLabel)
        self.posLabel = QtWidgets.QLabel(Form)
        self.posLabel.setGeometry(QtCore.QRect(195, 230, 51, 21))
        self.posLabel.setText("")
        self.posLabel.setObjectName("posLabel")
        self.posSlider = QtWidgets.QSlider(Form)
        self.posSlider.setGeometry(QtCore.QRect(9, 230, 181, 24))
        self.posSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.posSlider.setObjectName("posSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playPauseButton.setText(_translate("Form", "Play/Pause"))
        self.stopButton.setText(_translate("Form", "Stop"))
        self.volumeLabel.setText(_translate("Form", "Vol"))