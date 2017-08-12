#!/usr/bin/python
import sys,os
import fpdb

infile  = 'a.pdb'

pdb = fpdb.fPDB(infile)

waters = pdb.topology.get_water_residues()


template='''            <tr onClick="javascript:highlight_water(jmolApplet0,%d);togglecolor(this)">
              <td class="tg-baqh">%d</td>
              <td class="tg-baqh">%-6.1f</td>
              <td class="tg-baqh">%.0f%%</td>
            </tr>
'''

for water in waters:
    number = water.index
    occ = water.atoms[0].occ
    bf = water.atoms[0].bf
    print template%(number,number,occ,bf*100)

