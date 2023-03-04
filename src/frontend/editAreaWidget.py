# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/frontend/UI/editAreaWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editArea_Widget(object):
    def setupUi(self, editArea_Widget):
        editArea_Widget.setObjectName("editArea_Widget")
        editArea_Widget.resize(279, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(editArea_Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(editArea_Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.areaNameTextEdit = QtWidgets.QTextEdit(editArea_Widget)
        self.areaNameTextEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.areaNameTextEdit.setObjectName("areaNameTextEdit")
        self.horizontalLayout_2.addWidget(self.areaNameTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(editArea_Widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.areaInfoTextBrowser = QtWidgets.QTextBrowser(editArea_Widget)
        self.areaInfoTextBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.areaInfoTextBrowser.setReadOnly(False)
        self.areaInfoTextBrowser.setObjectName("areaInfoTextBrowser")
        self.verticalLayout.addWidget(self.areaInfoTextBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.areaClassComboBox = QtWidgets.QComboBox(editArea_Widget)
        self.areaClassComboBox.setObjectName("areaClassComboBox")
        self.areaClassComboBox.addItem("")
        self.areaClassComboBox.addItem("")
        self.areaClassComboBox.addItem("")
        self.horizontalLayout.addWidget(self.areaClassComboBox)
        self.editAreasButton = QtWidgets.QPushButton(editArea_Widget)
        self.editAreasButton.setObjectName("editAreasButton")
        self.horizontalLayout.addWidget(self.editAreasButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(editArea_Widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(editArea_Widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editJsonTextBrowser = QtWidgets.QTextBrowser(editArea_Widget)
        self.editJsonTextBrowser.setObjectName("editJsonTextBrowser")
        self.verticalLayout.addWidget(self.editJsonTextBrowser)
        self.editCleanTextButton = QtWidgets.QPushButton(editArea_Widget)
        self.editCleanTextButton.setObjectName("editCleanTextButton")
        self.verticalLayout.addWidget(self.editCleanTextButton)
        self.line = QtWidgets.QFrame(editArea_Widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.editExportButton = QtWidgets.QPushButton(editArea_Widget)
        self.editExportButton.setObjectName("editExportButton")
        self.verticalLayout.addWidget(self.editExportButton)

        self.retranslateUi(editArea_Widget)
        self.areaClassComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(editArea_Widget)

    def retranslateUi(self, editArea_Widget):
        _translate = QtCore.QCoreApplication.translate
        editArea_Widget.setWindowTitle(_translate("editArea_Widget", "edit"))
        self.label_2.setText(_translate("editArea_Widget", "Name"))
        self.label_3.setText(_translate("editArea_Widget", "Description"))
        self.areaClassComboBox.setItemText(0, _translate("editArea_Widget", "Zone 1 (red)"))
        self.areaClassComboBox.setItemText(1, _translate("editArea_Widget", "Zone 2 (orange)"))
        self.areaClassComboBox.setItemText(2, _translate("editArea_Widget", "Zone 3 (black)"))
        self.editAreasButton.setText(_translate("editArea_Widget", "EditAreas"))
        self.label.setText(_translate("editArea_Widget", "Export Info. (JSON)"))
        self.editCleanTextButton.setText(_translate("editArea_Widget", "Clean"))
        self.editExportButton.setText(_translate("editArea_Widget", "ExportToJSONFile"))
