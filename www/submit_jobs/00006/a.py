#!/usr/bin/python
import sys,os
import fpdb

lig = fpdb.fPDB(sys.argv[1]).topology.residues[0]
lig.generate_OPLS_parameters()
lig.write_pdb("INH.pdb")
