# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/frontend/UI/editWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_Widget(object):
    def setupUi(self, edit_Widget):
        edit_Widget.setObjectName("edit_Widget")
        edit_Widget.resize(279, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(edit_Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.droneIdText = QtWidgets.QTextEdit(edit_Widget)
        self.droneIdText.setMaximumSize(QtCore.QSize(16777215, 25))
        self.droneIdText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.droneIdText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.droneIdText.setObjectName("droneIdText")
        self.horizontalLayout_2.addWidget(self.droneIdText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(edit_Widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.flightTimeText = QtWidgets.QTextEdit(edit_Widget)
        self.flightTimeText.setMaximumSize(QtCore.QSize(16777215, 25))
        self.flightTimeText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.flightTimeText.setObjectName("flightTimeText")
        self.horizontalLayout_3.addWidget(self.flightTimeText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.editLineButton = QtWidgets.QPushButton(edit_Widget)
        self.editLineButton.setObjectName("editLineButton")
        self.verticalLayout.addWidget(self.editLineButton)
        self.line_2 = QtWidgets.QFrame(edit_Widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(edit_Widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editJsonTextBrowser = QtWidgets.QTextBrowser(edit_Widget)
        self.editJsonTextBrowser.setObjectName("editJsonTextBrowser")
        self.verticalLayout.addWidget(self.editJsonTextBrowser)
        self.editCleanTextButton = QtWidgets.QPushButton(edit_Widget)
        self.editCleanTextButton.setObjectName("editCleanTextButton")
        self.verticalLayout.addWidget(self.editCleanTextButton)
        self.line = QtWidgets.QFrame(edit_Widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.editExportButton = QtWidgets.QPushButton(edit_Widget)
        self.editExportButton.setObjectName("editExportButton")
        self.verticalLayout.addWidget(self.editExportButton)

        self.retranslateUi(edit_Widget)
        QtCore.QMetaObject.connectSlotsByName(edit_Widget)

    def retranslateUi(self, edit_Widget):
        _translate = QtCore.QCoreApplication.translate
        edit_Widget.setWindowTitle(_translate("edit_Widget", "edit"))
        self.label_2.setText(_translate("edit_Widget", "Drone ID."))
        self.label_3.setText(_translate("edit_Widget", "Flight Time"))
        self.editLineButton.setText(_translate("edit_Widget", "EditLine"))
        self.label.setText(_translate("edit_Widget", "Export Info. (JSON)"))
        self.editCleanTextButton.setText(_translate("edit_Widget", "Clean"))
        self.editExportButton.setText(_translate("edit_Widget", "ExportToJSONFile"))
