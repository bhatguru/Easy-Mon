# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseView.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from emailconf import *
import sqlite3
class Ui_emaildata(object):
    def setupUi(self, emaildata):
        emaildata.setObjectName("emaildata")
        emaildata.setFixedSize(339, 147)
        self.tableWidget = QtWidgets.QTableWidget(emaildata)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 321, 91))
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Smtp ", "Email", "Password"])
        self.tableWidget.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.tableWidget.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.tableWidget.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.tableWidget.setObjectName("tableWidget")
        self.formWidget = QtWidgets.QWidget(emaildata)
        self.formWidget.setGeometry(QtCore.QRect(10, 100, 321, 41))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.formWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.formWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.DeleteData)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.formWidget.raise_()
        self.tableWidget.raise_()
        self.LoadData()
        connection = sqlite3.connect("EASY.db")
        data = connection.execute("SELECT * FROM HOST")
        for item in data:
            a = item[0]
            self.comboBox.addItem(a)

        self.retranslateUi(emaildata)
        QtCore.QMetaObject.connectSlotsByName(emaildata)

    def retranslateUi(self, emaildata):
        _translate = QtCore.QCoreApplication.translate
        emaildata.setWindowTitle(_translate("emaildata", "Host_edit"))
        self.pushButton.setText(_translate("emaildata", "Delete"))

    def LoadData(self):
        connection = sqlite3.connect("EASY.db")
        Query = "SELECT * FROM HOST"
        result = connection.execute(Query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()


    def DeleteData(self):
        connection = sqlite3.connect("EASY.db")
        smtpsv = self.comboBox.currentText()
        if smtpsv > str(0):
            connection.execute("DELETE FROM HOST WHERE smtpsrv = ?",(smtpsv,))
            connection.commit()
            self.successfull()
            self.LoadData()
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emaildata = QtWidgets.QWidget()
    ui = Ui_emaildata()
    ui.setupUi(emaildata)
    emaildata.show()
    sys.exit(app.exec_())

