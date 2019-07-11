#!/usr/bin/python
import mysql.connector as mc

db = mc.connect( host = 'localhost',
                 user = 'fuqy',
                 passwd = '123',
                 database = 'SPA_database',
)

mycursor = db.cursor()
mycursor.execute("""CREATE TABLE system_information 
                    ( index_number INT NOT NULL AUTO_INCREMENT , 
                      pdb_id CHAR(4),
                      chain CHAR(1),
                      binding_site_definition VARCHAR(3),
                      resolution FLOAT,
                      number_of_hydration_sites SMALLINT,
                      alternative_pose CHAR(1),
                      register_date  TIMESTAMP , 
                      PRIMARY KEY ( index_number )
                    )
""")
            
mycursor.execute("""CREATE TABLE water_cluster
                    ( primary_key_number INT NOT NULL AUTO_INCREMENT , 
                      index_number INT,
                      water_index SMALLINT,
                      water_type CHAR(3),
                      occ FLOAT,
                      vdw_sol FLOAT,
                      vdw_rec FLOAT,
                      ele_sol FLOAT,
                      ele_rec FLOAT,
                      t_s FLOAT,
                      o_s FLOAT,
                      spa_g FLOAT,
                      rt FLOAT,
                      o_x FLOAT,
                      o_y FLOAT,
                      o_z FLOAT,
                      h1_x FLOAT,
                      h1_y FLOAT,
                      h1_z FLOAT,
                      h2_x FLOAT,
                      h2_y FLOAT,
                      h2_z FLOAT,
                      PRIMARY KEY ( primary_key_number ),
                      FOREIGN KEY ( index_number ) REFERENCES system_information(index_number) 
                    );
""")
            
