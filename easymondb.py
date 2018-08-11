#!/usr/bin/python3
import sqlite3

def connectdb():
    connection = sqlite3.connect("EASY.db")

def createTable():
    a = connectdb()
    try:
        a.connection.execute("CREATE TABLE IF NOT EXISTS HOST(SMTPSRV TEXT NOT NULL PRIMARY KEY,EMAIL TEXT,PASSWORD TEXT)")
        a.connection.execute("CREATE TABLE TARGET(EMAIL TEXT,THRESHOLD INT,INTERVAL INT)")
        a.connection.commit()
    except: print("\nTable already Exists\n")


def insertTable( ):
    connection = sqlite3.connect("EASY.db")
    connection.execute("INSERT INTO HOST(smtpsrv,email,password)VALUES(?,?,?)",(server,email,password))
    print('first row inserted')
    connection.commit()

def Deleterow():
    connection = sqlite3.connect("EASY.db")
    intr = 'gurubhat27@gmail.com'
    connection.execute("DELETE FROM TARGET WHERE email = ?", (intr,))
    connection.commit()

def viewdata():
    connection = sqlite3.connect("EASY.db")
    result = connection.execute("SELECT * FROM HOST")
    for data in result:
        print ("smtpsrv : ",data[0])
        print ("Email : ",data[1])
        print ("Password : ",data[2])
    rs = connection.execute("SELECT * FROM TARGET")
    ab = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(ab.fetchall())

    for elements in rs:
        print("Email :",elements[0])
        print("Threshold : ",elements[1])
        print("Intervals : ",elements[2])
    connection.close()
Deleterow()
viewdata()
