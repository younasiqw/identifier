#!/usr/bin/python

#
# Copyright (c) 2018 Barchampas Gerasimos <makindosx@gmail.com>.
# identifier is a program for locating computers tablets and mobile phones.
#
# identifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
#
# identifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License, version 3,
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#

import os
import sys
import cgi, cgitb 
import MySQLdb
import requests
sys.path.insert(0, '__DEV__/')
import administrator
from connect import CONNECTION


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db_mode = MySQLdb.connect(host,user,passw,dbs)


cursor_mode = db_mode.cursor()

mode_id = 1

sql_mode = """select mode from system_settings where id = '%s'""" %(mode_id)

try:
   cursor_mode.execute(sql_mode)
   result_mode = cursor_mode.fetchall()


   for row_mode in result_mode:
       mode_type = row_mode[0]
      

except:

       print "Error: unable to fecth data"

# disconnect from server
db_mode.close()



print """
<!doctype html>
<html lang="en">
<head>

	<meta charset="utf-8" />
	<link rel="icon" type="image/png" sizes="96x96" href="assets/img/favicon.png">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<title> Devices Location </title>

	<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Paper Dashboard core CSS    -->
    <link href="assets/css/paper-dashboard.css" rel="stylesheet"/>

    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet" />

    <!--  Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Muli:400,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/themify-icons.css" rel="stylesheet">
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


<style>

#backup
{
height: 80px;
width: 200px;
background-color: #141A00;
color: white;

}


#backup:hover
{
height: 80px;
width: 200px;
background-color: #212120;
color: white;
}


#set_time
{
height: 41px;
width: 150px;
background-color: #141A00;
color: white;

}


#set_time:hover
{
height: 41px;
width: 150px;
background-color: #212120;
color: white;
}


</style>


</head>
<body>

      <div class="wrapper">
	<div class="sidebar" data-background-color="black" data-active-color="danger">


    	<div class="sidebar-wrapper">
            <div class="logo">
                <a href="index.py" class="simple-text">
                   Identifier
                </a>
            </div>

            <ul class="nav">
                <li>
                    <a href="index.py">
                        <i class="fa fa-desktop"></i>
                        <p>Desktop</p>
                    </a>
                </li>
                 <li>
                    <a href="search_device.py">
                        <i class="fa fa-tablet"></i>
                        <p>Search Device</p>
                    </a>
                </li>
                <li>
                    <a href="devices_locations.py">
                        <i class="fa fa-microchip""></i>
                        <p>Devices Locations</p>
                    </a>
                </li>
               <li>
                    <a href="all_locations.py">
                        <i class="fa fa-globe"></i>
                        <p>All Locations</p>
                    </a>
                </li>
                <li>
                    <a href="remote_control.py">
                        <i class="fa fa-plug"></i>
                        <p>Remote control</p>
                    </a>
                </li>             
                <li>
                     <a href="task_manager.py">
                        <i class="fa fa-tasks"></i>
                        <p> Task Manager </p>
                    </a>
                </li>
                  <li class="active">
                    <a href="settings.py">
                         <i class="fa fa-cogs"></i>
                        <p>Settings</p>
                    </a>
                </li>
            </ul>
    	</div>
    </div>


    <div class="main-panel">
		<nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar bar1"></span>
                        <span class="icon-bar bar2"></span>
                        <span class="icon-bar bar3"></span>
                    </button>
                    <a class="navbar-brand" href="#"> Settings </a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav navbar-right">
                        <li> 
                           <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                               <i class="ti-panel"></i>
			       <p> Mode """+str(mode_type)+""" </p>
                           </a>
                        </li>

                        <li class="dropdown">

                              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                  <i class="fa fa-connectdevelop"></i>
				  <p> Interfaces </p>
				  <b class="caret"></b>
                              </a>

                     <ul class="dropdown-menu">
                      <li><a href="index.py"> Desktop <i class="fa fa-desktop"></i> </a></li>
                      <li><a href="search_device.py"> Search Device <i class="fa fa-tablet"></i> </a></li>
                      <li><a href="devices_locations.py"> Devices Locations <i class="fa fa-microchip"></i> </a></li>
                      <li><a href="all_locations.py"> All Locations <i class="fa fa-globe"></i> </a></li>
                      <li><a href="remote_control.py"> Remote Control <i class="fa fa-plug"></i> </a></li>
                      <li><a href="task_manager.py"> Task Manager <i class="fa fa-tasks"></i> </a></li>
                      <li><a href="settings.py"> Settings <i class="fa fa-cogs"></i> </a></li>
                     </ul>

                        </li>

			<li class="dropdown">
                         <a href="#" class="dropdown-toggle" data-toggle="dropdown">
			    <i class="fa fa-power-off"></i>
			    <p lass="notification"> Power </p>
                            <b class="caret"></b>
                            </a>
              
                            <ul class="dropdown-menu">
                               <li><a href="__ROOT__/power_on.py"> Power on </a></li>
                               <li><a href="__ROOT__/power_off.py"> Power off </a></li>
                             </ul>
                        </li>

                    </ul>

                </div>
            </div>
        </nav>


        <div class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12">
                        <div class="card" style="height:600px;">
                            <div class="header" align="center">
                                <h4 class="title"> System settings </h4> 
                                   <hr>
                                <p class="category"> Time of Renewal </p>
                            </div>

                           <div class="content all-icons" align="center">

                              <form action="" mathod="post">
                   <select class="form-control" name="time_of_renewal"
                        style="width:300px; color:white; background:#141A00; display:inline">
                             
                               <option value="1"> Live (send locations real time) </option> 
                               <option value="10"> 10 Seconds </option>
                               <option value="30"> 30 Seconds </option>
                               <option value="60"> 1  Minute </option>
                               <option value="120"> 2  Minutes </option>
                               <option value="300"> 5  Minutes </option>
                               <option value="600"> 10 Minutes </option>
                               <option value="900"> 15 Minutes </option>
                               <option value="1800"> 30 Minutes </option>
                               <option value="3600"> 1 Hour </option>
                             </select>

                           <button type="submit" name="set_time_renewal" value="Set_time_enabled" 
                               id="set_time">
                             Set time
                              <i class="ti-timer"></i>
                             </button>
                            </form>

                               <br><br><br><br> 

                            <div class="header" align="center">
                                   <hr>
                                <p class="category"> Backup for all locations </p>
                                   <br>
                            </div>

                           <form action="__SRC__/backup.py" target="_blank">'
                            <button type="submit" name="backup" id="backup" value="ready_for_use">
                              Backup Locations 
                             <i class="fa fa-download"></i> 
                           </button>  
                          </form>

                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!--
        <footer class="footer">
            <div class="container-fluid">
                <nav class="pull-left">
                    <ul>

                        <li>
                            <a href="http://www.creative-tim.com">
                                Creative Tim
                            </a>
                        </li>
                        <li>
                            <a href="http://blog.creative-tim.com">
                               Blog
                            </a>
                        </li>
                        <li>
                            <a href="http://www.creative-tim.com/license">
                                Licenses
                            </a>
                        </li>
                    </ul>
                </nav>
				<div class="copyright pull-right">
                    &copy; <script>document.write(new Date().getFullYear())</script>, made with <i class="fa fa-heart heart"></i> by <a href="http://www.creative-tim.com">Creative Tim</a>
                </div>
            </div>
        </footer>
          -->

    </div>
</div>


</body>

    <!--   Core JS Files   -->
    <script src="assets/js/jquery-1.10.2.js" type="text/javascript"></script>
	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<!--  Checkbox, Radio & Switch Plugins -->
	<script src="assets/js/bootstrap-checkbox-radio.js"></script>

	<!--  Charts Plugin -->
	<script src="assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="assets/js/bootstrap-notify.js"></script>

    <!--  Google Maps Plugin    -->
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js"></script>

    <!-- Paper Dashboard Core javascript and methods for Demo purpose -->
	<script src="assets/js/paper-dashboard.js"></script>

	<!-- Paper Dashboard DEMO methods, don't include it in your project! -->
	<script src="assets/js/demo.js"></script>


</html>
"""


form = cgi.FieldStorage() 


if form.getvalue('time_of_renewal'):
   time_of_renewal = form.getvalue('time_of_renewal')
   mode = form.getvalue('mode')

#else:
  # time_of_renewal = ""
  # mode  = ""
   #os._exit(1)


db = MySQLdb.connect(host,user,passw,dbs)

cursor = db.cursor()

sql = """ update system_settings set time_of_renewal = '%s' where id = '1' """ %(time_of_renewal)

try:

   cursor.execute(sql)
   db.commit()

   if os.environ['REQUEST_URI'] != '/identification/settings.py':
      print '''<script>
            alert('The time has been activated');
           </script>
            <script>location.href='settings.py'</script>'''
      
     # print os.environ["REQUEST_URI"]


   #else:
   #   print '''<script>
   #         alert('The time has not been activated');
   #        </script>'''

except:
  
   db.rollback()

db.close()

