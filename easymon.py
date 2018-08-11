#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easymon.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_CPUinfo(object):
    def setupUi(self, CPUinfo):
        CPUinfo.setObjectName("CPUinfo")
        CPUinfo.setFixedSize(328, 199)
        CPUinfo.setWindowIcon(QtGui.QIcon("icon.png"))
        self.formWidget = QtWidgets.QWidget(CPUinfo)
        self.formWidget.setGeometry(QtCore.QRect(20, 90, 281, 81))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setObjectName("formLayout")
        self.memory = QtWidgets.QProgressBar(self.formWidget)
        self.memory.setStyleSheet("color: rgb(9, 229, 17);")
        self.memory.setProperty("value", 24)
        self.memory.setObjectName("memory")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.memory)
        self.label = QtWidgets.QLabel(self.formWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cpu = QtWidgets.QProgressBar(self.formWidget)
        self.cpu.setStyleSheet("color: rgb(0, 255, 64);")
        self.cpu.setProperty("value", 24)
        self.cpu.setObjectName("cpu")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cpu)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.frame = QtWidgets.QFrame(CPUinfo)
        self.frame.setGeometry(QtCore.QRect(10, 30, 311, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.notifybutton = QtWidgets.QPushButton(self.frame)
        self.notifybutton.setGeometry(QtCore.QRect(250, 0, 61, 28))
        self.notifybutton.setObjectName("notifybutton")
        self.frame.raise_()
        self.formWidget.raise_()

        self.retranslateUi(CPUinfo)
        QtCore.QMetaObject.connectSlotsByName(CPUinfo)


    def retranslateUi(self, CPUinfo):
        _translate = QtCore.QCoreApplication.translate
        CPUinfo.setWindowTitle(_translate("CPUinfo", "EASY-MON"))
        self.label.setText(_translate("CPUinfo", "Memory"))
        self.label_2.setText(_translate("CPUinfo", "CPU "))
        self.notifybutton.setText(_translate("CPUinfo", "Notify Me"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CPUinfo = QtWidgets.QWidget()
    ui = Ui_CPUinfo()
    ui.setupUi(CPUinfo)
    CPUinfo.show()
    sys.exit(app.exec_())

