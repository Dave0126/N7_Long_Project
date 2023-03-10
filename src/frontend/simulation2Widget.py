# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/frontend/UI/simulation2Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_simulation2Widget(object):
    def setupUi(self, simulation2Widget):
        simulation2Widget.setObjectName("simulation2Widget")
        simulation2Widget.resize(368, 662)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(simulation2Widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(simulation2Widget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(simulation2Widget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.droneIdTextEdit = QtWidgets.QTextEdit(simulation2Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.droneIdTextEdit.sizePolicy().hasHeightForWidth())
        self.droneIdTextEdit.setSizePolicy(sizePolicy)
        self.droneIdTextEdit.setMaximumSize(QtCore.QSize(1000, 32))
        self.droneIdTextEdit.setPlaceholderText("")
        self.droneIdTextEdit.setObjectName("droneIdTextEdit")
        self.horizontalLayout_5.addWidget(self.droneIdTextEdit)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(simulation2Widget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.flightDateTextEdit = QtWidgets.QTextEdit(simulation2Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flightDateTextEdit.sizePolicy().hasHeightForWidth())
        self.flightDateTextEdit.setSizePolicy(sizePolicy)
        self.flightDateTextEdit.setMaximumSize(QtCore.QSize(1000, 32))
        self.flightDateTextEdit.setPlaceholderText("")
        self.flightDateTextEdit.setObjectName("flightDateTextEdit")
        self.horizontalLayout_4.addWidget(self.flightDateTextEdit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addStartPointPushButton = QtWidgets.QPushButton(simulation2Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addStartPointPushButton.sizePolicy().hasHeightForWidth())
        self.addStartPointPushButton.setSizePolicy(sizePolicy)
        self.addStartPointPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addStartPointPushButton.setMaximumSize(QtCore.QSize(1000, 32))
        self.addStartPointPushButton.setObjectName("addStartPointPushButton")
        self.horizontalLayout_3.addWidget(self.addStartPointPushButton)
        self.addEndPointPushButton = QtWidgets.QPushButton(simulation2Widget)
        self.addEndPointPushButton.setMaximumSize(QtCore.QSize(16777215, 32))
        self.addEndPointPushButton.setObjectName("addEndPointPushButton")
        self.horizontalLayout_3.addWidget(self.addEndPointPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.createPlanPushButton = QtWidgets.QPushButton(simulation2Widget)
        self.createPlanPushButton.setMaximumSize(QtCore.QSize(16777215, 32))
        self.createPlanPushButton.setObjectName("createPlanPushButton")
        self.verticalLayout.addWidget(self.createPlanPushButton)
        self.line = QtWidgets.QFrame(simulation2Widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(simulation2Widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.importDroneFlightPlanButton = QtWidgets.QPushButton(simulation2Widget)
        self.importDroneFlightPlanButton.setObjectName("importDroneFlightPlanButton")
        self.verticalLayout_2.addWidget(self.importDroneFlightPlanButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setTimerSpinBox = QtWidgets.QSpinBox(simulation2Widget)
        self.setTimerSpinBox.setMinimum(1)
        self.setTimerSpinBox.setMaximum(10000)
        self.setTimerSpinBox.setProperty("value", 1000)
        self.setTimerSpinBox.setObjectName("setTimerSpinBox")
        self.horizontalLayout.addWidget(self.setTimerSpinBox)
        self.label_2 = QtWidgets.QLabel(simulation2Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.autoSimStartButton = QtWidgets.QPushButton(simulation2Widget)
        self.autoSimStartButton.setAutoFillBackground(False)
        self.autoSimStartButton.setObjectName("autoSimStartButton")
        self.horizontalLayout_2.addWidget(self.autoSimStartButton)
        self.autoSimPulseOrContinueButton = QtWidgets.QPushButton(simulation2Widget)
        self.autoSimPulseOrContinueButton.setObjectName("autoSimPulseOrContinueButton")
        self.horizontalLayout_2.addWidget(self.autoSimPulseOrContinueButton)
        self.autoSimStopButton = QtWidgets.QPushButton(simulation2Widget)
        self.autoSimStopButton.setObjectName("autoSimStopButton")
        self.horizontalLayout_2.addWidget(self.autoSimStopButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(simulation2Widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.manualPath = QtWidgets.QPushButton(simulation2Widget)
        self.manualPath.setObjectName("manualPath")
        self.horizontalLayout_6.addWidget(self.manualPath)
        self.line_4 = QtWidgets.QFrame(simulation2Widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_6.addWidget(self.line_4)
        self.automatic = QtWidgets.QPushButton(simulation2Widget)
        self.automatic.setObjectName("automatic")
        self.horizontalLayout_6.addWidget(self.automatic)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line_3 = QtWidgets.QFrame(simulation2Widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(simulation2Widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.sim_coordTextBrowser = QtWidgets.QTextBrowser(simulation2Widget)
        self.sim_coordTextBrowser.setObjectName("sim_coordTextBrowser")
        self.verticalLayout_3.addWidget(self.sim_coordTextBrowser)
        self.simExportButton = QtWidgets.QPushButton(simulation2Widget)
        self.simExportButton.setObjectName("simExportButton")
        self.verticalLayout_3.addWidget(self.simExportButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(simulation2Widget)
        QtCore.QMetaObject.connectSlotsByName(simulation2Widget)

    def retranslateUi(self, simulation2Widget):
        _translate = QtCore.QCoreApplication.translate
        simulation2Widget.setWindowTitle(_translate("simulation2Widget", "simluation1"))
        self.label.setText(_translate("simulation2Widget", "Create a FlightPlan automatically"))
        self.label_5.setText(_translate("simulation2Widget", "Drone ID."))
        self.label_6.setText(_translate("simulation2Widget", "Flight Date"))
        self.addStartPointPushButton.setText(_translate("simulation2Widget", "Add Start Point"))
        self.addEndPointPushButton.setText(_translate("simulation2Widget", "Add End Point"))
        self.createPlanPushButton.setText(_translate("simulation2Widget", "Create a FlightPlan"))
        self.label_3.setText(_translate("simulation2Widget", "Automatic sampling"))
        self.importDroneFlightPlanButton.setText(_translate("simulation2Widget", "Import a drone\'s flight plan"))
        self.label_2.setText(_translate("simulation2Widget", "millisecond"))
        self.autoSimStartButton.setText(_translate("simulation2Widget", "Start"))
        self.autoSimPulseOrContinueButton.setText(_translate("simulation2Widget", "Pulse/Continue"))
        self.autoSimStopButton.setText(_translate("simulation2Widget", "Stop"))
        self.manualPath.setText(_translate("simulation2Widget", "Manual Path"))
        self.automatic.setText(_translate("simulation2Widget", "Automatic Path"))
        self.label_4.setText(_translate("simulation2Widget", "Record"))
        self.simExportButton.setText(_translate("simulation2Widget", "Export simulation"))
