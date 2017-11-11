#!/usr/bin/python
import mysql.connector as mc
import sys,os
import fSPA
import fmysql_lib

t = sys.argv[1]

fmysql_lib.list_query(t =t )
