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

#print 'Content-type:text/html\r\n\r\n'

conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db = MySQLdb.connect(host,user,passw,dbs)

cursor = db.cursor()

mode_id = 1

sql_mode = """select mode from system_settings where id = '%s'""" %(mode_id)

try:
   cursor.execute(sql_mode)
   result_mode = cursor.fetchall()


   for row_mode in result_mode:
       mode_type = row_mode[0]
      


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

#map {
  height: 70%;
  width: 100%;
  margin: 0px;
  padding: 0px
}

    </style>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<script>
$(document).ready(function(){    
    loadstation();
});

function loadstation(){
    $("#station_data").load("search_device.py");
    setTimeout(loadstation, 1000);
}
</script>

<style>

.form-control::-webkit-input-placeholder { color: black; }  /* WebKit, Blink, Edge */
.form-control:-moz-placeholder { color: black; }  /* Mozilla Firefox 4 to 18 */
.form-control::-moz-placeholder { color: black; }  /* Mozilla Firefox 19+ */
.form-control:-ms-input-placeholder { color: black; }  /* Internet Explorer 10-11 */
.form-control::-ms-input-placeholder { color: black; }  /* Microsoft Edge */

.form-control:focus {
  border-color: black !important;
  box-shadow: 0 0 5px black !important;
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
                 <li class="active">
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
                    <a class="navbar-brand" href=""> Search Device </a>
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
 

           <br><br>

        <div class="content">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-12">
                        <div class="card" style="height:600px;">

                              <div id="map"></div>

                <div class="header" align="center">
                                <h4 class="title"> Search Device </h4> 
                                   <hr>

             <form action="" method="post" enctype="multipart/form-data" class="form-horizontal">

            <div class="input-group col-xs-8" style="background-color:black;">
             <span class="input-group-addon"> <i class="glyphicon glyphicon-user"></i></span>
             <input id="search" type="text" class="form-control" name="search" 
                    style="height: 60px; font-size: 70px;" autofocus>
            <button hidden type="submit_search" name="submit"></button>
           </div>
             </div>
         </form>

         </div>

        </div></div></div></div></div>

        </div>


     
                
                </div>
            </div>
        </div>

    </div>
</div>



"""
   form = cgi.FieldStorage()


   if form.getvalue('search'):
      search = form.getvalue('search')

      sql_search = """SELECT GROUP_CONCAT(CONCAT(all_info))
                   AS 'combined_all_info'
                   FROM devices where device_id = '%s' """ %(search)

   sql_search2 = """SELECT latitude,longitude FROM devices where device_id = '%s' """ %(search)

   cursor.execute(sql_search)
   result_search = cursor.fetchall()

   cursor.execute(sql_search2)
   result_search2 = cursor.fetchall()

   for row_search in result_search:
       all_info = row_search[0]

   for row_search2 in result_search2:
       lat = row_search2[0]
       lng = row_search2[1]

       print """

<script>
     
function initMap() {
  var uluru = {lat: """+str(lat)+""", lng: """+str(lng)+"""};
  var map = new google.maps.Map(document.getElementById('map'), {
    mapTypeId: 'hybrid',
    zoom: 8,
    center: uluru
  });
  var infoWin = new google.maps.InfoWindow();
  // Add some markers to the map.
  // Note: The code uses the JavaScript Array.prototype.map() method to
  // create an array of markers based on a given 'locations' array.
  // The map() method here has nothing to do with the Google Maps API.
  var markers = locations.map(function(location, i) {
    var marker = new google.maps.Marker({
      position: location
    });
    google.maps.event.addListener(marker, 'click', function(evt) {
      infoWin.setContent(location.info);
      infoWin.open(map, marker);
    })
    return marker;
  });

  // markerCluster.setMarkers(markers);
  // Add a marker clusterer to manage the markers.
  var markerCluster = new MarkerClusterer(map, markers, {
    imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
  });

}
var locations = ["""+str(all_info)+""" ,];

google.maps.event.addDomListener(window, 'load', initMap);

    </script>
"""

except:

       print "Error: unable to fecth data"

# disconnect from server
db.close()



print """

    <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
    </script>

   <!-- hack the api key for cluster -->
  <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&callback=initMap"></script>


    <script src="assets/js/jquery-1.10.2.js" type="text/javascript"></script>
	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<script src="assets/js/bootstrap-checkbox-radio.js"></script>

	<script src="assets/js/chartist.min.js"></script>

    <script src="assets/js/bootstrap-notify.js"></script>


	<script src="assets/js/paper-dashboard.js"></script>

	<script src="assets/js/demo.js"></script>

</body>

</html>
"""
