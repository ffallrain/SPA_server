#!/usr/bin/python
import sys,os

for line in open(sys.argv[1]):
    line = line.strip()
    items = line.split("_")
    pdbid = items[0]
    chain = items[1]
    summary_file = "/data/SSD/spa_results/%s.spa/SPA.summary"%line
    os.system( "./data_submit.py %s %s %s 000 0.0 0"%(summary_file, pdbid, chain,) )
    print(">>>>> Done: ", line)
    
