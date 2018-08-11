#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TargetDatabase View.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
class Ui_targetdata(object):
    def setupUi(self, targetdata):
        targetdata.setObjectName("targetdata")
        targetdata.setFixedSize(339, 147)
        self.Tdelete = QtWidgets.QPushButton(targetdata)
        self.Tdelete.setGeometry(QtCore.QRect(280, 110, 51, 28))
        self.Tdelete.setObjectName("Tdelete")
        self.Tdelete.clicked.connect(self.DeleteData)
        self.comboBox = QtWidgets.QComboBox(targetdata)
        self.comboBox.setGeometry(QtCore.QRect(100, 110, 180, 28))
        self.comboBox.setObjectName("comboBox1")
        self.TtableWidget = QtWidgets.QTableWidget(targetdata)
        self.TtableWidget.setGeometry(QtCore.QRect(10, 10, 321, 91))
        self.TtableWidget.setRowCount(2)
        self.TtableWidget.setColumnCount(3)
        self.TtableWidget.setHorizontalHeaderLabels(["Email ", "Threshold", "Intervals"])
        self.TtableWidget.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.TtableWidget.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.TtableWidget.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.TtableWidget.setObjectName("TtableWidget")
        self.PullData()
        connection = sqlite3.connect("EASY.db")
        data = connection.execute("SELECT * FROM TARGET")
        for item in data:
            a = item[0]
            self.comboBox.addItem(a)

        self.retranslateUi(targetdata)
        QtCore.QMetaObject.connectSlotsByName(targetdata)

    def DeleteData(self):
        connection = sqlite3.connect("EASY.db")
        intr = self.comboBox.currentText()
        if intr > str(0):
            connection.execute("DELETE FROM TARGET WHERE email = ?", (intr,))
            connection.commit()
            self.successfull()
            self.PullData()
            self.comboBox.clear()
            connection.close()
        else:
            self.InvalidInfo()

    def successfull(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Row Deleted Successfully...!!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def InvalidInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Sorry No Data Exists")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def PullData(self):
        connection = sqlite3.connect("EASY.db")
        Query = "SELECT * FROM TARGET"
        result = connection.execute(Query)
        self.TtableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.TtableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TtableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def retranslateUi(self, targetdata):
        _translate = QtCore.QCoreApplication.translate
        targetdata.setWindowTitle(_translate("targetdata", "Target_edit"))
        self.Tdelete.setText(_translate("targetdata", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    targetdata = QtWidgets.QWidget()
    ui = Ui_targetdata()
    ui.setupUi(targetdata)
    targetdata.show()
    sys.exit(app.exec_())

