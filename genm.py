#!/usr/bin/python3
import smtplib
import sqlite3
def SendMail():
    connection = sqlite3.connect("EASY.db",timeout=10)
    RST = connection.execute("SELECT * FROM HOST")
    TRS = connection.execute("SELECT * FROM TARGET")
    for itms in RST:
        ems = itms[0]
        eml = itms[1]
        psw = itms[2]
    for tr in TRS:
        target = tr[0]
        if len(itms) != str(0):
            try:
                server = smtplib.SMTP(ems, 587)
                server.starttls()
                server.login(eml, psw)
                msg = "HI There...Your system memory/cpu is almost full please check!!!!"
                server.sendmail(eml, target, msg)
                server.quit()
            except: ConnectionAbortedError
        else:
            return 0


