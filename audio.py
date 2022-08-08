# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import Qt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 112)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_28 = QtWidgets.QFrame(self.centralwidget)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_28)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_2.addWidget(self.pushButton_27, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_28)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_28, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        filename = 'test.mp3'
        fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
        url = QtCore.QUrl.fromLocalFile(fullpath)
        content = QtMultimedia.QMediaContent(url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(self.playlist.Loop)
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playing Audio"))
        self.pushButton_27.setText(_translate("MainWindow", "Return to Screen"))
        self.label.setText(_translate("MainWindow", "The Audio is Now being Played"))

        self.pushButton_27.clicked.connect(self.close)
        self.player.play()

    def close(self):
        self.player.stop()
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("logo.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())