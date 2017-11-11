#!/usr/bin/python
import mysql.connector as mc
import sys,os
import fSPA

#### parse arguments
infile = sys.argv[1]
pdb_id = sys.argv[2][:4]
chain = sys.argv[3][0]
ligname = sys.argv[4]
resolution = float( sys.argv[5] )
alternative_pose = sys.argv[6][0]

submit_query( infile = infile , pdbid = pdb_id , chain = chain , ligname = ligname , resolution = resolution , alternative_pose = alternative_pose )
