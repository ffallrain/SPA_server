# SPA Database

## 1. Data construction
## 2. Database filling
**We use python API to interact with MySQL.**

### 2.1 Creating tables
The tutorial is [**HERE**](https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html).

We will create one table to store only structure information which do not contain water property at all. It is actually an index.

**TABLE SYSTEM_INFORMATION**

> index|pdb_id|binding_site_defination|chain|resolution|alternative_pose|number_of_hydration_sites|register_date
> -|-|-|-|-|-|-|-
> INT|CHAR|CHAR|CHAR|FLOAT|CHAR|INT|DATE
> 1|1az8|INH|A|2.1|A|23|data

Here's the code :
```
CREATE TABLE test (
    index_number INT(6) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    pdb_id CHAR(4) NOT NULL,
    chain CHAR(1) DEFAULT "A",
    binding_site_definition CHAR(3),
    resolution FLOAT(4,2),  
    alternative_pose CHAR(1),
    number_of_hydration_sites INT(4) DEFAULT 0 ,
    register_date TIMESTAMP ) ;
```

Resulting table :
```
+---------------------------+------------+------+-----+-------------------+-----------------------------+
| Field                     | Type       | Null | Key | Default           | Extra                       |
+---------------------------+------------+------+-----+-------------------+-----------------------------+
| index_number              | int(6)     | NO   | PRI | NULL              | auto_increment              |
| pdb_id                    | char(4)    | NO   |     | NULL              |                             |
| chain                     | char(1)    | YES  |     | A                 |                             |
| binding_site_definition   | char(3)    | YES  |     | NULL              |                             |
| resolution                | float(4,2) | YES  |     | NULL              |                             |
| alternative_pose          | char(1)    | YES  |     | NULL              |                             |
| number_of_hydration_sites | int(4)     | YES  |     | 0                 |                             |
| register_date             | timestamp  | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+---------------------------+------------+------+-----+-------------------+-----------------------------+
```




And another table of original SPA water information:

**TABLE WATER_CLUSTER**
>
> index|water_index|water_type|occ|rt|coords|vdw_sol|ele_sol|vdw_rec|ele_rec|t_s|o_s|spa_g
> -|-|-|-|-|-|-|-|-|-|-|-|-|-
>INT|INT|CHAR|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT|FLOAT

Command :
> ```
>       CREATE TABLE water_cluster
>       ( index_number INT(6) NOT NULL,
>       water_index INT(4) NOT NULL,
>       water_type CHAR(3) DEFAULT "SOL",
>       occ FLOAT(4.2),
>       rt FLOAT(4.2),
>       o_x FLOAT(8.3),
>       o_y FLOAT(8.3),
>       o_z FLOAT(8.3),
>       h1_x FLOAT(8.3),
>       h1_y FLOAT(8.3),
>       h1_z FLOAT(8.3),
>       h2_x FLOAT(8.3),
>       h2_y FLOAT(8.3),
>       h2_z FLOAT(8.3),
>       vdw_sol FLOAT,
>       ele_sol FLOAT,
>       vdw_rec FLOAT,
>       ele_rec FLOAT,
>       t_s FLOAT,
>       o_s FLOAT,
>       spa_g FLOAT,
>       register_date TIMESTAMP
>       ) ;
> ```

Result table:
> ```
> +---------------+-----------+------+-----+-------------------+-----------------------------+
> | Field         | Type      | Null | Key | Default           | Extra                       |
> +---------------+-----------+------+-----+-------------------+-----------------------------+
> | index_number  | int(6)    | NO   | PRI | NULL              |                             |
> | water_index   | int(4)    | NO   |     | NULL              |                             |
> | water_type    | char(3)   | YES  |     | SOL               |                             |
> | occ           | float     | YES  |     | NULL              |                             |
> | rt            | float     | YES  |     | NULL              |                             |
> | o_x           | float     | YES  |     | NULL              |                             |
> | o_y           | float     | YES  |     | NULL              |                             |
> | o_z           | float     | YES  |     | NULL              |                             |
> | h1_x          | float     | YES  |     | NULL              |                             |
> | h1_y          | float     | YES  |     | NULL              |                             |
> | h1_z          | float     | YES  |     | NULL              |                             |
> | h2_x          | float     | YES  |     | NULL              |                             |
> | h2_y          | float     | YES  |     | NULL              |                             |
> | h2_z          | float     | YES  |     | NULL              |                             |
> | vdw_sol       | float     | YES  |     | NULL              |                             |
> | ele_sol       | float     | YES  |     | NULL              |                             |
> | vdw_rec       | float     | YES  |     | NULL              |                             |
> | ele_rec       | float     | YES  |     | NULL              |                             |
> | t_s           | float     | YES  |     | NULL              |                             |
> | o_s           | float     | YES  |     | NULL              |                             |
> | spa_g         | float     | YES  |     | NULL              |                             |
> | register_date | timestamp | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
> +---------------+-----------+------+-----+-------------------+-----------------------------+
> ```

**Job status**

Command:

> create table job_status (job_index int(6) NOT NULL, name char(8) , register_date timestamp, status char(8) DEFAULT "submit", index_number int(6)  );

Result table:

>``` MySQL [test]> describe job_status;
>+---------------+-----------+------+-----+-------------------+-----------------------------+
> | Field         | Type      | Null | Key | Default           | Extra                       |
> +---------------+-----------+------+-----+-------------------+-----------------------------+
> | job_index     | int(6)    | NO   |     | NULL              |                             |
> | name          | char(8)   | YES  |     | NULL              |                             |
> | register_date | timestamp | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
> | status        | char(8)   | YES  |     | submit            |                             |
> | index_number  | int(6)    | YES  |     | NULL              |                             |
> +---------------+-----------+------+-----+-------------------+-----------------------------+
> ```



### 2.2 Inserting data

**Syntax is at [HERE](https://www.tutorialspoint.com/mysql/mysql-insert-query.htm)**

We write a python script to insert data.

## 3. HTML API

###   3.1 Using Jmol applet as graphic tool.
* __Adventage__ : It can be asserted into web page easily
    * It supports most graphic rendering options
    * User don't need Java runtime environment to assess it's full ability. ( While Jmol requires Java)
    * Public free
*  __Disadventage__:
    * You need to learn Javascript ( which is a new programming language ) to employ JSmol
    * The graphic is not very beautiful ( compare to Chimera or Pymol )

### 3.1.2 How to assert a JSmol viewer on your webpage ?
1. Download Jmol from SourceForge
2. Extract the tarball to you server path. e.g. /www/applet/Jmol
3. Add *"<!DOCTYPE html>"* at the head of you html file.
4. Source Jmol.min.js
  ```    
      <script type="text/javascript" src="/applet/jsmol/JSmol.min.js"></script>
  ```
5. Define inital parameters
```
    <script type="text/javascript">
        var Info0;
        var jmolApplet0;
        function jmolApplet0_isReady() {
            Jmol.script(jmolApplet0,";select [INH]; hide [INH] ;selectionHalos ON; select protein or nucleic; cartoons only;select none; set windowCentered TRUE;center [    SOL];zoom IN ;");
        }
        var Info0 = {
            width: 600,
            height: 600,
            debug: false,
            color: "white",
            addSelectionOptions: false,
            serverURL: "/applet/jsmol.php",
            use: "HTML5",
            j2sPath: "/applet/jsmol/j2s",
            src: "/pdb/a.pdb",
            readyFunction: jmolApplet0_isReady,
            script: null,//script,
            disableInitialConsole: false,
            language: "en_US",
        };
    </script>
```
    More information at : [__Here__](http://wiki.jmol.org/index.php/Jmol_JavaScript_Object/Info)

    *"function jmolApplet0_isReady()"* defines the scripts to be run when applet initialized.
6.  Add this to where you want to place the applet:
```
      <script type="text/javascript">
          Jmol.getApplet("jmolApplet0", Info0);
      </script>
```
    Here *jmolApplet0* is the name of the applet, you will use it when you want to manipulate an applet

### 3.1.3 How to control JSmol applet ?
** 1. Define functions.  Using Jmol.script( applet, script ) to run scripts. *e.g.* **
```
            function highlight_water(applet,water) {
                if ( states[water] == undefined || states[water] == false ) {
                    Jmol.script(applet,";select ADD [SOL]"+water);  // HERE is
                    states[water] = true;
                }
                else {
                    Jmol.script(applet,";select REMOVE [SOL]"+water);
                    states[water] = false;
                }
            };
```

** 2. Write triggers to call the functions. *e.g.* **
```
      <tr onClick="javascript:highlight_water(jmolApplet0,3);togglecolor(this)">
```

Here we use onClick event on tr object.

## 3.2  Using CGI to generate dynamic webpage.

###    3.2.1 What is a CGI ?

**Common Gateway Interaction.** It will run script on host side ( while HTML and Javascript including Jmol all run on client side. ). Mostly, host will not allow all files to be executed.

Usually CGI scripts are only allowed in a directory, e.g. /www/cgi-bin.

CGI will return a flat HTML file to client.

### 3.2.2 Python CGI interface
CGI module and CGITB module is used.

```
import cgi
import cgitb
cgitb.enable(display=0, logdir="/log/cgi_test.log")
```

Use GET to fetch parameters from client :
* client code :
```
 <form action="/cgi-bin/search_by_single_pdbid.cgi" method="post" name=
     "protein_pdbid" enctype="multipart/form-data" target="_blank">
       <p><input type="text" name="pdbid" /> &nbsp;&nbsp;&nbsp; <input type=
       "submit" name="search_id" value="GO" /></p>
 </form>
```
_note 'pdbid' is the POST name._
**Preview**:
 <form action="/cgi-bin/search_by_single_pdbid.cgi" method="post" name=
     "protein_pdbid" enctype="multipart/form-data" target="_blank">
       <p><input type="text" name="pdbid" /> &nbsp;&nbsp;&nbsp; <input type=
       "submit" name="search_id" value="GO" /></p>
 </form>

* server code:
```
    form = cgi.FieldStorage()
    user = form.getfirst("pdbid", "")    # This way it's safe.
    for item in form.getlist("item"):
        do_something(item)
```
**Note**: using form.getfirst("itemname","") is a more safe way.

## 3.3 Link to MySQL database by Python API
### 3.3.1 Python module
**mysql.connector** Official website with document [**HERE**](https://dev.mysql.com/doc/)
### 3.3.2 Link
* By function style :

```
    import mysql.connector

    cnx = mysql.connector.connect(user='scott', password='tiger',
                                  host='127.0.0.1',
                                  database='employees')
    cnx.close()
```

* By OO style:

```

    from mysql.connector import (connection)

    cnx = connection.MySQLConnection(user='scott', password='tiger',
                                     host='127.0.0.1',
                                     database='employees')
    cnx.close()
```

### 3.3.3 Query
After connecting to a MySQL database, we create a cursor object. By execute commands with cursor, we can fetch results. (Which is from cursor, too)

```
cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()
```
