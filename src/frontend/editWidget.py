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
        edit_Widget.resize(232, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(edit_Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.areaClassComboBox = QtWidgets.QComboBox(edit_Widget)
        self.areaClassComboBox.setObjectName("areaClassComboBox")
        self.areaClassComboBox.addItem("")
        self.areaClassComboBox.addItem("")
        self.areaClassComboBox.addItem("")
        self.horizontalLayout.addWidget(self.areaClassComboBox)
        self.editAreasButton = QtWidgets.QPushButton(edit_Widget)
        self.editAreasButton.setObjectName("editAreasButton")
        self.horizontalLayout.addWidget(self.editAreasButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(edit_Widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
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
        self.areaClassComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(edit_Widget)

    def retranslateUi(self, edit_Widget):
        _translate = QtCore.QCoreApplication.translate
        edit_Widget.setWindowTitle(_translate("edit_Widget", "edit"))
        self.areaClassComboBox.setItemText(0, _translate("edit_Widget", "Zone 1 (red)"))
        self.areaClassComboBox.setItemText(1, _translate("edit_Widget", "Zone 2 (orange)"))
        self.areaClassComboBox.setItemText(2, _translate("edit_Widget", "Zone 3 (black)"))
        self.editAreasButton.setText(_translate("edit_Widget", "EditAreas"))
        self.editLineButton.setText(_translate("edit_Widget", "EditLine"))
        self.label.setText(_translate("edit_Widget", "Areas Info. (JSON)"))
        self.editCleanTextButton.setText(_translate("edit_Widget", "Clean"))
        self.editExportButton.setText(_translate("edit_Widget", "ExportToJSONFile"))
