#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailconf.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from TargetDatabaseview import *
from DBview import*
import time
import sys
import sqlite3
class Ui_configuration(object):
    def setupUi(self, configuration):
        configuration.setObjectName("configuration")
        configuration.setFixedSize(361, 249)
        self.Notification = QtWidgets.QTabWidget(configuration)
        self.Notification.setGeometry(QtCore.QRect(0, 0, 361, 241))
        self.Notification.setObjectName("Notification")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formWidget = QtWidgets.QWidget(self.tab)
        self.formWidget.setGeometry(QtCore.QRect(9, 40, 341, 111))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setObjectName("formLayout")
        self.labelsmtp = QtWidgets.QLabel(self.formWidget)
        self.labelsmtp.setObjectName("labelsmtp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelsmtp)
        self.smtpline = QtWidgets.QLineEdit(self.formWidget)
        self.smtpline.setObjectName("smtpline")
        self.smtpline.setPlaceholderText("smtp.gmail.com")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.smtpline)
        ##################input validation##########################################
        servr_regx = QtCore.QRegExp('^(smtp\.[a-zA-Z.-\S]+.([a-zA-z]{2,4}))')
        validator = QtGui.QRegExpValidator(servr_regx)
        self.smtpline.setValidator(validator)
        #############################################################################
        self.emaillbl = QtWidgets.QLabel(self.formWidget)
        self.emaillbl.setObjectName("emaillbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.emaillbl)
        self.emailine = QtWidgets.QLineEdit(self.formWidget)
        self.emailine.setObjectName("emailine")
        self.emailine.setPlaceholderText("Email Address")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.emailine)
        ############################################################################
        emlad_regx = QtCore.QRegExp('^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.([a-zA-z]{2,4}))')
        validator = QtGui.QRegExpValidator(emlad_regx)
        self.emailine.setValidator(validator)
        ###############################################################################
        self.passlabl = QtWidgets.QLabel(self.formWidget)
        self.passlabl.setObjectName("passlabl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passlabl)
        self.passwdline = QtWidgets.QLineEdit(self.formWidget)
        self.passwdline.setObjectName("passwdline")
        self.passwdline.setPlaceholderText("Password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwdline)
        ##############################################################################
        self.passwdline.setEchoMode(QtWidgets.QLineEdit.Password)
        passwd_regx = QtCore.QRegExp(r'([a-zA-Z0-9._@]*)')
        validator = QtGui.QRegExpValidator(passwd_regx)
        self.passwdline.setValidator(validator)
        ################################################################################
        self.hostsave = QtWidgets.QPushButton(self.tab)
        self.hostsave.setGeometry(QtCore.QRect(300, 150, 41, 28))
        self.hostsave.setObjectName("hostsave")
        self.hostedit = QtWidgets.QPushButton(self.tab)
        self.hostedit.setGeometry(QtCore.QRect(250, 150, 41, 28))
        self.hostedit.setObjectName("hostedit")
        self.hostedit.setText("EDIT")
        self.hrefresh = QtWidgets.QPushButton(self.tab)
        self.hrefresh.setGeometry(QtCore.QRect(185, 150, 58, 28))
        self.hrefresh.setObjectName("hRefresh")
        self.hrefresh.setText("REFRESH")
        self.hrefresh.clicked.connect(self.ckck)
        self.Notification.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.targetbtn = QtWidgets.QPushButton(self.tab_2)
        self.targetbtn.setGeometry(QtCore.QRect(290, 140, 41, 28))
        self.targetbtn.setObjectName("targetbtn")
        self.formWidget1 = QtWidgets.QWidget(self.tab_2)
        self.formWidget1.setGeometry(QtCore.QRect(30, 40, 311, 101))
        self.Tedit = QtWidgets.QPushButton(self.tab_2)
        self.Tedit.setGeometry(QtCore.QRect(240, 140, 41, 28))
        self.Tedit.setObjectName("Tedit")
        self.Tedit.setText("EDIT")
        ########################################################################################
        self.Trefresh = QtWidgets.QPushButton(self.tab_2)
        self.Trefresh.setGeometry(QtCore.QRect(175, 140, 58, 28))
        self.Trefresh.setObjectName("Refresh")
        self.Trefresh.setText("REFRESH")
        self.Trefresh.clicked.connect(self.chkn)
        ##########################################################################################
        self.formWidget1.setObjectName("formWidget1")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formWidget1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.emllbl = QtWidgets.QLabel(self.formWidget1)
        self.emllbl.setObjectName("emllbl")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.emllbl)
        self.emailln = QtWidgets.QLineEdit(self.formWidget1)
        self.emailln.setObjectName("emailln")
        self.emailln.setPlaceholderText("Email Address")
        eml_regx = QtCore.QRegExp('^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.([a-zA-z]{2,4}))')
        validator = QtGui.QRegExpValidator(eml_regx)
        self.emailln.setValidator(validator)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emailln)
        self.thlbl = QtWidgets.QLabel(self.formWidget1)
        self.thlbl.setObjectName("thlbl")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.thlbl)
        self.spinBoxthreshold = QtWidgets.QSpinBox(self.formWidget1)
        self.spinBoxthreshold.setObjectName("spinBoxthreshold")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxthreshold)
        self.intervallbl = QtWidgets.QLabel(self.formWidget1)
        self.intervallbl.setObjectName("intervallbl")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.intervallbl)
        self.intervalsln = QtWidgets.QLineEdit(self.formWidget1)
        self.intervalsln.setObjectName("intervalsln")
        self.intervalsln.setMaxLength(5)
        intr_regx = QtCore.QRegExp('^(\d\d\d\d\d)')
        validator = QtGui.QRegExpValidator(intr_regx)
        self.intervalsln.setValidator(validator)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.intervalsln)
        self.formWidget.raise_()
        self.targetbtn.raise_()
        self.Notification.addTab(self.tab_2, "")
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


        self.retranslateUi(configuration)
        self.Notification.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(configuration)

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
            self.Tedit.setDisabled(False)
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
        connection = sqlite3.connect("EASY.db",timeout=10)
        connection.execute("INSERT INTO HOST(smtpsrv,email,password)VALUES(?,?,?)", (server, email, password))
        connection.commit()
        connection.close()


    def hstsavebtn(self):
        server = str(self.smtpline.text())
        email = str(self.emailine.text())
        password = str(self.passwdline.text())
        Stt = [server, email, password]
        for i in Stt:
            if i > str(0):
                self.insertTable(server, email, password)
                self.successfull()
                self.emailine.clear()
                self.smtpline.clear()
                self.passwdline.clear()
                self.ckck()
                break
            else:
                self.InvalidInfo()

    def targetsavebtn(self):
        temail = self.emailln.text()
        threshold = self.spinBoxthreshold.text()
        interval = self.intervalsln.text()
        Ttt = [temail, threshold, interval]
        for i in Ttt:
            if i > str(0):
                self.insertT(temail, threshold, interval)
                self.successfull()
                self.spinBoxthreshold.clear()
                self.intervalsln.clear()
                self.emailln.clear()
                self.chkn()
                break
            else:
                self.InvalidInfo()

    def insertT(self,temail,threshold,interval):
        connection = sqlite3.connect("EASY.db",timeout=10)
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

    def tdisble(self):
        temail = self.emailln.text()
        threshold = self.spinBoxthreshold.text()
        interval = self.intervalsln.text()

        if temail >str(0) and threshold >str(0) and interval >str(0):
            self.targetbtn.setDisabled(False)
        else:
            self.targetbtn.setDisabled(True)




    def retranslateUi(self, configuration):
        _translate = QtCore.QCoreApplication.translate
        configuration.setWindowTitle(_translate("configuration", "Email Configuration"))
        self.labelsmtp.setText(_translate("configuration", "SMTP Server"))
        self.emaillbl.setText(_translate("configuration", "EMAIL"))
        self.passlabl.setText(_translate("configuration", "PASSWORD"))
        self.hostsave.setText(_translate("configuration", "SAVE"))
        self.Notification.setTabText(self.Notification.indexOf(self.tab), _translate("configuration", "Host"))
        self.targetbtn.setText(_translate("configuration", "SAVE"))
        self.emllbl.setText(_translate("configuration", "EMAIL"))
        self.thlbl.setText(_translate("configuration", "THRESHOLD(cpu /mem"))
        self.intervallbl.setText(_translate("configuration", "INTERVALS(sec)"))
        self.Notification.setTabText(self.Notification.indexOf(self.tab_2), _translate("configuration", "Target"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    configuration = QtWidgets.QWidget()
    ui = Ui_configuration()
    ui.setupUi(configuration)
    configuration.show()
    sys.exit(app.exec_())

