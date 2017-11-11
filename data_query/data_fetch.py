#!/usr/bin/python
import mysql.connector as mc
import sys,os
import fSPA
import fmysql_lib

#### parse arguments
pdbid = sys.argv[1][:4]
chain = sys.argv[2][0]
ligname = sys.argv[3]

fmysql_lib.fetch_query(pdbid = pdbid, chain = chain, ligname = ligname )


