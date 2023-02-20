# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation1Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_simulation1Widget(object):
    def setupUi(self, simulation1Widget):
        simulation1Widget.setObjectName("simulation1Widget")
        simulation1Widget.resize(330, 662)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(simulation1Widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(simulation1Widget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.latTextEdit = QtWidgets.QTextEdit(simulation1Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latTextEdit.sizePolicy().hasHeightForWidth())
        self.latTextEdit.setSizePolicy(sizePolicy)
        self.latTextEdit.setMaximumSize(QtCore.QSize(1000, 32))
        self.latTextEdit.setPlaceholderText("LAT")
        self.latTextEdit.setObjectName("latTextEdit")
        self.verticalLayout.addWidget(self.latTextEdit)
        self.lngTextEdit = QtWidgets.QTextEdit(simulation1Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lngTextEdit.sizePolicy().hasHeightForWidth())
        self.lngTextEdit.setSizePolicy(sizePolicy)
        self.lngTextEdit.setMaximumSize(QtCore.QSize(1000, 32))
        self.lngTextEdit.setObjectName("lngTextEdit")
        self.verticalLayout.addWidget(self.lngTextEdit)
        self.coordPushButton = QtWidgets.QPushButton(simulation1Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coordPushButton.sizePolicy().hasHeightForWidth())
        self.coordPushButton.setSizePolicy(sizePolicy)
        self.coordPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.coordPushButton.setMaximumSize(QtCore.QSize(1000, 40))
        self.coordPushButton.setObjectName("coordPushButton")
        self.verticalLayout.addWidget(self.coordPushButton)
        self.line = QtWidgets.QFrame(simulation1Widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(simulation1Widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(simulation1Widget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(simulation1Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.autoSimStartButton = QtWidgets.QPushButton(simulation1Widget)
        self.autoSimStartButton.setObjectName("autoSimStartButton")
        self.horizontalLayout.addWidget(self.autoSimStartButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(simulation1Widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(simulation1Widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.sim_coordTextBrowser = QtWidgets.QTextBrowser(simulation1Widget)
        self.sim_coordTextBrowser.setObjectName("sim_coordTextBrowser")
        self.verticalLayout_3.addWidget(self.sim_coordTextBrowser)
        self.simExportButton = QtWidgets.QPushButton(simulation1Widget)
        self.simExportButton.setObjectName("simExportButton")
        self.verticalLayout_3.addWidget(self.simExportButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(simulation1Widget)
        QtCore.QMetaObject.connectSlotsByName(simulation1Widget)

    def retranslateUi(self, simulation1Widget):
        _translate = QtCore.QCoreApplication.translate
        simulation1Widget.setWindowTitle(_translate("simulation1Widget", "simluation1"))
        self.label.setText(_translate("simulation1Widget", "Enter a coordinate ( LAT & LNG ):"))
        self.lngTextEdit.setPlaceholderText(_translate("simulation1Widget", "LNG"))
        self.coordPushButton.setText(_translate("simulation1Widget", "OK"))
        self.label_3.setText(_translate("simulation1Widget", "Auto Simple"))
        self.label_2.setText(_translate("simulation1Widget", "millisecond"))
        self.autoSimStartButton.setText(_translate("simulation1Widget", "Start"))
        self.label_4.setText(_translate("simulation1Widget", "Record"))
        self.simExportButton.setText(_translate("simulation1Widget", "Export simulation"))
