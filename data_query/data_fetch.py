#!/usr/bin/python
import mysql.connector as mc
import sys,os
import fSPA

#### parse arguments
pdb_id = sys.argv[1][:4]
chain = sys.argv[2][0]
ligname = sys.argv[3]


#### Link to database
host = "k203"
database = "test"
user = "flexsite"
password = "123"

if True: # link to database
    cnx = mc.MySQLConnection( user=user, password=password, host=host, database=database )
    cursor = cnx.cursor()

if True: # fetch from system_information 
    update = True
    query = """SELECT index_number, pdb_id,chain,binding_site_definition, resolution, number_of_hydration_sites, register_date
            FROM system_information 
            WHERE pdb_id = '%s' AND chain = '%s' AND binding_site_definition = '%s' 
            """
    query = query%(pdb_id,chain,ligname)
    cursor.execute( query,() )
    answer = cursor.fetchall() 
    N_result = len(answer)
    if N_result <= 0 :
        sys.stderr.write( "##### ERROR, no entry %s %s %s \n"%(pdb_id,chain,ligname))
        sys.exit()
    else:
        a = answer[-1]
        index = a[0]
        water_number = a[5]
    
if True: # get water information
    for water_index in range(water_number+1):
        query = ('''
                SELECT index_number, water_index, occ, vdw_sol, vdw_rec, ele_sol, ele_rec, t_s, o_s, spa_g 
                FROM water_cluster
                WHERE index_number = %d 
                '''
        )
        
        query = query%( index, )
        
    
if True: # close database
    cursor.close()
    cnx.close()

