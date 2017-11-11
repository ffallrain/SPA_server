#!/usr/bin/python
import mysql.connector as mc
import sys,os
import fSPA

#### Link to database
host = "k203"
database = "test"
user = "flexsite"
password = "123"

def fetch_query(pdbid,chain,ligname):
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
        query = ('''
                SELECT index_number, water_index, occ, vdw_sol, vdw_rec, ele_sol, ele_rec, t_s, o_s, spa_g 
                FROM water_cluster
                WHERE index_number = %d 
                '''
        )
        
        query = query%( index, )
        cursor.execute( query,() )
        answer = cursor.fetchall() 
        if len(answer) <= 0 :
            sys.stderr.write( "##### ERROR, no entry %s %s %s \n"%(pdb_id,chain,ligname))
            sys.exit()

        waters = dict()
        keys = list()
        for a in answer :
            key = a[1]
            waters[key] = a 
            if key not in keys:
                keys.append(key)

        for key in keys:
            print key,waters[key]
            
        
    if True: # close database
        cursor.close()
        cnx.close()

def list_query(t):
    cnx = mc.MySQLConnection( user=user, password=password, host=host, database=database )
    cursor = cnx.cursor()

    if t == 'system': # fetch from system_information 
        update = True
        query = """SELECT index_number, pdb_id,chain,binding_site_definition, resolution, number_of_hydration_sites, register_date
                FROM system_information 
                """
        query = query
        cursor.execute( query,() )
        answer = cursor.fetchall() 
        N_result = len(answer)
        if N_result <= 0 :
            sys.stderr.write( ">>>>> No entry\n")
            sys.exit()
        else:
            for a in answer :
                print a
        
    if t == 'water' : # get water information
        query = ('''
                SELECT index_number, water_index, occ, vdw_sol, vdw_rec, ele_sol, ele_rec, t_s, o_s, spa_g 
                FROM water_cluster
                '''
        )
        
        cursor.execute( query,() )
        answer = cursor.fetchall() 
        N_result = len(answer)
        if N_result <= 0 :
            sys.stderr.write( ">>>>> No entry\n")
            sys.exit()
        else:
            for a in answer :
                print a

    cursor.close()
    cnx.close()

def submit_query( infile, pdbid, chain, ligname, resolution, alternative_pose ):
    pdb_id = pdbid

    #### Read SPA.summary
    summary = fSPA.fSPA_summary(infile)
    number_of_waters = len(summary.waters)

    if True: # link to database
        cnx = mc.MySQLConnection( user=user, password=password, host=host, database=database )
        cursor = cnx.cursor()

    #### register system_information and get index
    if True: # check if there's already such an entry 
        update = True
        query = """SELECT pdb_id,chain,binding_site_definition,register_date
                FROM system_information 
                WHERE pdb_id = '%s' AND chain = '%s' AND binding_site_definition = '%s' 
                """
        query = query%(pdb_id,chain,ligname)
        cursor.execute( query,() )
        answer = cursor.fetchall() 
        N_result = len(answer)
        for a in answer:
            pass
        if N_result >= 1:
            update = True
        else:
            update = False

    if not update: # insert a new entry 
        query = ('''
                INSERT INTO system_information 
                (pdb_id, binding_site_definition, chain, resolution, number_of_hydration_sites) 
                VALUES 
                ("%s", "%s", "%s", %f, %d)
        ''')

        data = (pdb_id,ligname,chain,resolution,number_of_waters)
        query = query%data

        cursor.execute( query,() )
        for result in cursor.stored_results():
            print result.fetchall()

    else: # update exist entry
        query = ('''
                UPDATE system_information 
                SET resolution = %f, alternative_pose = "%s", number_of_hydration_sites = %d 
                WHERE pdb_id = '%s' AND chain = '%s' AND binding_site_definition = '%s' 
        ''')

        data = (resolution,alternative_pose,number_of_waters,pdb_id, chain, ligname)
        query = query%data

        cursor.execute( query,() )
        for result in cursor.stored_results():
            print result.fetchall()

    if True: # Get index, use it to make 
        query = """SELECT index_number,pdb_id,chain,binding_site_definition,register_date
                FROM system_information 
                WHERE pdb_id = '%s' AND chain = '%s' AND binding_site_definition = '%s' 
                """
        query = query%(pdb_id,chain,ligname)
        cursor.execute( query,() )
        answer = cursor.fetchall() 
        N_result = len(answer)
        if N_result <=0 :
            sys.stderr.write("##### ERROR cannot find registered entry !\n")
            cursor.close()
            cnx.close()
            sys.exit()
        else:
            index = int( answer[0][0] )
        
    if True: # insert entries in water_cluster
        for water in summary.waters :
            water_index = water.index
            o_x,o_y,o_z = water.atoms[0].posi
            h1_x,h1_y,h1_z = water.atoms[1].posi
            h2_x,h2_y,h2_z = water.atoms[2].posi
            vdw_sol = water.vdw_sol
            vdw_rec = water.vdw_rec
            ele_sol = water.ele_sol
            ele_rec = water.ele_rec
            t_s     = water.trans_entropy
            o_s     = water.orient_entropy
            spa_g   = water.spa_energy
            occ     = water.occ
            rt      = water.residence_t
            water_type = "SOL"

            query = ('''
                    INSERT INTO water_cluster
                    (index_number, water_index, water_type, occ, rt, 
                     o_x, o_y, o_z, h1_x, h1_y, h1_z, h2_x, h2_y, h2_z,
                     vdw_sol, vdw_rec, ele_sol, ele_rec, 
                     t_s, o_s, spa_g )
                    VALUES
                    (%d, %d, "%s", %f, %f,
                    %f, %f, %f, %f, %f, %f, %f, %f, %f,
                    %f, %f, %f, %f,
                    %f, %f, %f )
                    '''
            )
            
            query = query%( index, water_index, water_type, occ, rt, o_x, o_y, o_z, h1_x, h1_y, h1_z, h2_x, h2_y, h2_z, vdw_sol, vdw_rec, ele_sol, ele_rec, t_s, o_s, spa_g )
            
            cursor.execute( query, () )
            for result in cursor.stored_results():
                print result.fetchall()
        
    if True: # close database
        cursor.close()
        cnx.close()


