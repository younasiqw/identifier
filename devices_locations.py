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


db = MySQLdb.connect(host,user,passw,dbs)

cursor = db.cursor()

mode_id = 1

sql_mode = """select mode from system_settings where id = '%s'""" %(mode_id)

sql_devices = """select * from devices order by instant desc""" 

try:
   cursor.execute(sql_mode)
   result_mode = cursor.fetchall()


   for row_mode in result_mode:
       mode_type = row_mode[0]

   cursor.execute(sql_devices)
   result_devices = cursor.fetchall()


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

    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <link href="assets/css/paper-dashboard.css" rel="stylesheet"/>

    <link href="assets/css/demo.css" rel="stylesheet" />

    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Muli:400,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/themify-icons.css" rel="stylesheet">
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


<style>


* {box-sizing: border-box} /* for th's width; display purpose */

table 
{
width: 100%;
display: block; /* to enable vertical scrolling */
max-height: 500px; /* e.g. */
overflow-y: scroll; /* keeps the scrollbar even if it doesn't need it; display purpose */
}

table, td {
  border-collapse: collapse;
}

th
{
background-color: #EEEDE9;
}


th, td {
  width: 20.33%; /* to enable "word-break: break-all" */
}


#map 
{
height: 100%;
}

      
html, body 
{
height: 100%;
margin: 0;
padding: 0;
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
                <li class="active">
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
                  <li>
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
                    <a class="navbar-brand" href="#"> Devices Locations </a>
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
                        <div class="card">
                            <div class="header">
                                <h4 class="title" align="center"> Locations of devices </h4>
                                <p class="category" align="center"> Here is all the information about the devices </p>
                           </div>

                            <div class="content table-responsive table-full-width">
                                <table class="table table-striped">
                                    <thead>
                                        <th> Instant </th>
                                    	<th> Device ID </th>
                                    	<th> Last IP </th>
                                    	<th> Fingerprint </th>
                                    	<th> Location (lat, lon)</th>
                                        <th> On The Map </th>
                                        <th> Delete Devices </th>
                                    </thead>
                                  <tbody>"""
                                   
   


   for row_devices in result_devices:
       delete_device_id = row_devices[0]
       instant  = row_devices[3]
       device_id = row_devices[1]
       last_ip   = row_devices[2]
       fingerprint = row_devices[7] 
       location  = row_devices[4] + ' , ' + row_devices[5]
       location_on_map = row_devices[4] + ',' + row_devices[5] + '-' + row_devices[1] + '-' + row_devices[6]

       print ' <tr>'
       print'  <td>%s' %(instant) 
       print'  </td>'
       print'  <td>%s' %(device_id)
       print'  </td>'
       print'  <td>%s' %(last_ip)
       print'  </td>'
       print'  <td>%s' %(fingerprint)
       print'  </td>'
       print'  <td>%s' %(location)
       print'  </td>'
       print'  <td> ' 
       print' <form action="devices_locations_map.py" target="_blank">'
       print' <button type="submit" name="map_location" class="btn btn-primary btn-md" value="%s"> View Device <i class="fa fa-eye"></i> </button>'%(location_on_map)
       print' </form>'
       print'  </td>' 
       print'  <td>'
       print' <form action="__ROOT__/delete_device.py">'
       print' <button type="submit" name="delete_device_id" class="btn btn-dangerous btn-md" value="%s"> Delete Device <i class="fa fa-trash"></i> </button>'%(delete_device_id)
       print' </form>'
       print'  </td>'
       print' </tr>'
       print'</tbody>' 


except:

       print "Error: unable to fecth data"

# disconnect from server
db.close()
       
print """
                       </table>

                            </div>
                        </div>
                    </div>


    <div align="center">
     <form action="__ROOT__/delete_devices.py">
       <button type="submit" name="delete_devices" class="btn btn-dangerous btn-md" value="all"> 
          Delete all devices locations <i class="fa fa-trash"></i> 
       </button>
     </form>
   </div>


    </div>
</div>


</body>

    
    <script src="assets/js/jquery-1.10.2.js" type="text/javascript"></script>
	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<script src="assets/js/bootstrap-checkbox-radio.js"></script>

	<script src="assets/js/chartist.min.js"></script>

    <script src="assets/js/bootstrap-notify.js"></script>

    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js"></script>

	<script src="assets/js/paper-dashboard.js"></script>

	<script src="assets/js/demo.js"></script>


</html>
"""

