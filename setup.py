#!/usr/bin/python
import sys,os
import mysql.connector as mc

mydb = mc.connect(
    host = 'localhost',
    user = 'fuqy',
    passwd = '',
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE SPA_database")

