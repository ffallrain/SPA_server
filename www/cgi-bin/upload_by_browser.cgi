#!/usr/bin/python
import sys,os
import cgi
import cgitb
import fpdb
cgitb.enable(display=0, logdir="/log/cgi_test.log")

if True:
    head = '''
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <title>Protein</title>
      <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
      <meta name="viewport" content="width=device-width"/>
      <meta charset="utf-8">

      <script type="text/javascript" src="/applet/jsmol/JSmol.min.js"></script>
        <script type="text/javascript"> 
            var Info0;
            var jmolApplet0;
            function jmolApplet0_isReady() {
                Jmol.script(jmolApplet0,";select [INH]; hide [INH] ;selectionHalos ON; select protein or nucleic; cartoons only;select none; set windowCentered TRUE;center [SOL];zoom IN ;");
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
                readyFunction: jmolApplet0_isReady,
                script: null,//script,
                disableInitialConsole: false,
                language: "en_US",
            };
            var states = new Object();
            function highlight_water(applet,water) {
                if ( states[water] == undefined || states[water] == false ) {
                    Jmol.script(applet,";select ADD [SOL]"+water);
                    states[water] = true;
                }
                else {
                    Jmol.script(applet,";select REMOVE [SOL]"+water);
                    states[water] = false;
                }
            };
            
            function togglecolor(a) {
                if ( a['highlighted'] ) {
                    a.style.backgroundColor = document.body.style.backgroundColor ;
                    a['highlighted'] = false ;
                }
                else {
                    a.style.backgroundColor = "#66FF99" ;
                    a['highlighted'] = true ;
                }
                
            }
                
        </script>
    </head>
    '''
    body_top = '''
        <body bgcolor="#F4F5F7" width="80%" align="center"> <!-- banner -->
          <table width="100%" height=60 border="0" cellspacing="0" cellpadding="0" bgcolor="#1c488c" align="center">
            <tr height = 20 >
              <td width="5%"></td>

              <style>
              a{
                  color:white;
                  text-decoration:none; 
              }
              </style>

              <td align="center" valign="middle" width="12%"><a href="%20index.html" class=
              " navText"><span class="STYLE2">SPA-Databse</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Introduction.html"
              class="navText"><span class="STYLE9" >Introduction</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Search.html" class=
              " navText"><span class="STYLE9">Search</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Browse.html" class=
              " navText"><span class="STYLE9">Browse</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Download.html" class=
              " navText"><span class="STYLE9">Download</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Methods.html" class=
              " navText"><span class="STYLE9">Methods</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20FAQ.html" class=
              " navText"><span class="STYLE9">FAQ</span></a></td>

              <td align="center" valign="middle" width="8%"><a href="%20Links.html" class=
              " navText"><span class="STYLE9">Links</span></a></td>

              <td width="27%"></td>
            </tr>
          </table>

          <table width="100%" height="10%" border="0" cellspacing="0" cellpadding="0" align= "center"> <!-- Search banner --> 
            <tr>
              <td width="5%"></td>

              <td width="8%" align="center" valign="middle"><img src="/img/logo.png" width=
              "70%" height="30%" border="0" /></td>

              <td width="12%" align="center" valign="middle" nowrap="nowrap"> <span class=
              "STYLE10">SPA-Database </span></td>

              <td width="20%"></td>

              <td>
                <form action="/cgi-bin/search_by_single_pdbid.cgi" method="post" name=
                    "protein_pdbid" enctype="multipart/form-data" target="_blank">
                      <p><input type="text" name="pdbid" /> &nbsp;&nbsp;&nbsp; <input type=
                      "submit" name="search_id" value="GO" /></p>
                </form>
              </td>

              <td width="10%"></td>
            </tr>
          </table>
        '''
    body_bottom = '''
        </body>
        </html>
    '''

dir_path='submit_jobs'
job_index_file = "%s/jobindex.data"%dir_path

index = int(open(job_index_file).read()) + 1
with open(job_index_file,'w') as ofp :
    ofp.write("%d\n"%index)
an = "%05d"%index

if True:
    print head
    print body_top
    print "<h2>\n"
    print "Your files have been uploaded.\n"
    print "</h2>\n"
    print "<br>\n"
    print "<h3>\n"
    print "Your job accession number is <a href=tmp.html> %s </a>. \n"%an
    print "</h3>\n"

    print """
      <table width="90%"  height=600 cellspacing="1" cellpadding="0" align="center" frame="hsides" rules="cols"> <!-- graphic applet & water data -->
          <tr>
            <td width="5%" align="center" valign='top'><font size="4.5" color="#0099FF">  
            </td>
            <td width="45%" align="center" valign='top'><font size="4.5" color="#0099FF">  <!-- Applet 0 -->
                <script type="text/javascript">
                    Jmol.getApplet("jmolApplet0", Info0);
                </script>
            </td>
    """
    print """
    <script>
                Jmol.script(jmolApplet0,";load \"PDB::/pdb/a.pdb\"; ");
    </script>
    """

if True:
    form = cgi.FieldStorage()
    keys = form.keys()

    try:
        os.mkdir("%s/%s"%(dir_path,an))
        with open("%s/%s/rec.pdb"%(dir_path,an),'w') as ofp:
            ofp.write( form.getfirst('rec','') )

        with open("%s/%s/lig.pdb"%(dir_path,an),'w') as ofp:
            ofp.write( form.getfirst('lig','') )

    except:
        pass

if True:
    rec = fpdb.fPDB("%s/%s/rec.pdb"%(dir_path,an))
    lig = fpdb.fPDB("%s/%s/lig.pdb"%(dir_path,an)).topology.residues[0]

    his_list = list()
    for resi in rec.topology.residues:
        if resi.name in ("HIS","HID","HIP","HIE") and fpdb.dist_resi_resi(lig,resi)<10:
            his_list.append(resi)

if True:
    print '''
        <td width="45" align="center"><font size="4.5" color="#0099FF"> <!-- table data 1 -->
          <div style="overflow:scroll;height:600px">
              <table class="tg" scrolling="yes" height = 600 >
                <tr>
                  <th class="tg-amwm">Water No.</th>
                  <th class="tg-amwm">SPA energy ( kcal/mol )</th>
                  <th class="tg-amwm">Occupancy</th>
                </tr>
    '''
    ofp = open("/tmp/a",'w')
    for his in his_list:
        ofp.write("YES\n") 
        print '''
                <tr onClick="javascript:highlight_water(jmolApplet0,1);togglecolor(this)">
                  <td class="tg-baqh">1</td>
                  <td class="tg-baqh">-3.4  </td>
                  <td class="tg-baqh">100%</td>
                </tr>
        '''
    ofp.close()

print body_bottom

