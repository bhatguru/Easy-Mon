#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from emailconf import*
from DBview import*
import genm
import time
import sqlite3
class SubUiClass(QtWidgets.QMainWindow,Ui_configuration):
    def __init__(self, parent = None):
        super(SubUiClass, self).__init__(parent)
        self.setupUi(self)
        self.hostsave.setDisabled(True)
        self.targetbtn.setDisabled(True)
        self.smtpline.textChanged.connect(self.disablebtn)
        self.emailine.textChanged.connect(self.disablebtn)
        self.passwdline.textChanged.connect(self.disablebtn)
        self.hostsave.clicked.connect(self.hstsavebtn)
        self.hostedit.clicked.connect(self.heopen)
        self.targetbtn.clicked.connect(self.targetsavebtn)
        self.Tedit.clicked.connect(self.topen)
        self.emailln.textChanged.connect(self.tdisble)
        self.intervalsln.textChanged.connect(self.tdisble)
        self.chkn()
        self.ckck()


    def chkn(self):
        connection = sqlite3.connect("EASY.db")
        chkn = connection.execute("SELECT * FROM TARGET")

        if len(chkn.fetchall()) == 0:
            self.tdisble()
            self.Tedit.setDisabled(True)
            self.emailln.setDisabled(False)
            self.spinBoxthreshold.setDisabled(False)
            self.intervalsln.setDisabled(False)
        else:
            self.emailln.setDisabled(True)
            self.spinBoxthreshold.setDisabled(True)
            self.intervalsln.setDisabled(True)
        connection.close()

    def ckck(self):
        connection = sqlite3.connect("EASY.db")
        chk = connection.execute("SELECT * FROM HOST")
        if len(chk.fetchall()) == 0:
            self.disablebtn()
            self.hostedit.setDisabled(True)
            self.smtpline.setDisabled(False)
            self.emailine.setDisabled(False)
            self.passwdline.setDisabled(False)
        else:
            self.hostedit.setDisabled(False)
            self.smtpline.setDisabled(True)
            self.emailine.setDisabled(True)
            self.passwdline.setDisabled(True)
        connection.close()
    def hstsavebtn(self):
        server = self.smtpline.text()
        email = self.emailine.text()
        password = self.passwdline.text()
        Stt = [server, email, password]
        for i in Stt:
            if i > str(0):
                self.ckck()
                self.insertTable(server,email,password)
                self.successfull()
                self.emailine.clear()
                self.smtpline.clear()
                self.passwdline.clear()
            else:
                self.InvalidInfo()

    def successfull(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("All Information Saved Successfully...!!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def InvalidInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Invalid Information..!! Please fill all the details")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def errormsg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Plese Configure Host and Target Information Properly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def insertTable(self,server,email,password):
        connection = sqlite3.connect("EASY.db")
        connection.execute("INSERT INTO HOST(smtpsrv,email,password)VALUES(?,?,?)", (server, email, password))
        connection.commit()
        connection.close()

    def tdisble(self):
        temail = self.emailln.text()
        threshold = self.spinBoxthreshold.text()
        interval = self.intervalsln.text()
        if temail > str(0) and threshold > str(0) and interval > str(0):
            self.targetbtn.setDisabled(False)
        else:
            self.targetbtn.setDisabled(True)

    def targetsavebtn(self):
        temail = self.emailln.text()
        threshold = self.spinBoxthreshold.text()
        interval = self.intervalsln.text()
        Ttt = [temail, threshold, interval]
        for i in Ttt:
            if i > str(0):
                self.insertT(temail,threshold,interval)
                self.successfull()
                self.spinBoxthreshold.clear()
                self.intervalsln.clear()
                self.emailln.clear()
                self.tdisble()
            else:
                self.InvalidInfo()

    def insertT(self,temail,threshold,interval):
        connection = sqlite3.connect("EASY.db")
        connection.execute("INSERT INTO TARGET(email,threshold,interval)VALUES(?,?,?)",(temail,threshold,interval))
        connection.commit()
        connection.close()
    def heopen(self):
        self.hewindow = QtWidgets.QWidget()
        self.ui = Ui_emaildata()
        self.ui.setupUi(self.hewindow)
        self.hewindow.show()

    def topen(self):
        self.tewindow = QtWidgets.QWidget()
        self.ui = Ui_targetdata()
        self.ui.setupUi(self.tewindow)
        self.tewindow.show()

    def disablebtn(self):
        server = self.smtpline.text()
        email = self.emailine.text()
        password = self.passwdline.text()

        if server >str(0) and email>str(0) and password > str(0):
            self.hostsave.setDisabled(False)
        else:
            self.hostsave.setDisabled(True)

if __name__ == '__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = SubUiClass()
    app.show()
    a.exec_()
