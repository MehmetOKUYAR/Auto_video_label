# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MEHMET/Desktop/auto_label/auto_label.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 288)
        MainWindow.setMinimumSize(QtCore.QSize(350, 280))
        MainWindow.setMaximumSize(QtCore.QSize(358, 288))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 2, 1, 1, 1)
        self.pushButton_loadVideo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadVideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_loadVideo.setObjectName("pushButton_loadVideo")
        self.gridLayout.addWidget(self.pushButton_loadVideo, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_frame = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frame.setObjectName("lineEdit_frame")
        self.gridLayout.addWidget(self.lineEdit_frame, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_classname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_classname.setObjectName("lineEdit_classname")
        self.gridLayout.addWidget(self.lineEdit_classname, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "default : 0"))
        self.pushButton_loadVideo.setText(_translate("MainWindow", "load video path"))
        self.label_2.setText(_translate("MainWindow", "Save per frame"))
        self.lineEdit_frame.setPlaceholderText(_translate("MainWindow", "default : 1"))
        self.label.setText(_translate("MainWindow", "Name start :"))
        self.label_3.setText(_translate("MainWindow", "Auto Video Labeling"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_4.setText(_translate("MainWindow", "Class Name :"))

