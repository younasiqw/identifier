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

<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>


<style>


body
{
width: 100%;
display: inline; 
}




.form-body
{
background: black;
padding:20px;

margin-left: auto;
margin: right: auto;
height: 400px;
width: 100%;
}


.login-form{
    background:;
	padding:20px;
	border-top:3px solid#3e4043;
}
.innter-form{
	padding-top:50px;
}
.final-login li{
	width:100%;
}

.nav-tabs {
    border-bottom: none !important;
}

.nav-tabs>li{
	color:#222 !important;
}
.nav-tabs>li.active>a, .nav-tabs>li.active>a:hover, .nav-tabs>li.active>a:focus {
    color: #fff;
    background-color: #212120;
    border: none !important;
    border-bottom-color: transparent;
	border-radius:none !important;
}
.nav-tabs>li>a {
    margin-right: 2px;
    line-height: 1.428571429;
    border: none !important;
    border-radius:none !important;
	text-transform:uppercase;
	font-size:16px;
}

.sa-innate-form input[type=text], input[type=password], input[type=file], textarea, select, email{
        font-size:30px;
	padding:10px;
	border:1px solid#ccc;
	outline:none;
	width:100%;
	margin:8px 0;
	
}
.sa-innate-form input[type=submit]{
    border:1px solid#e64b3b;
	background:#212120;
	color:#fff;
	padding:10px 25px;
	font-size:14px;
	margin-top:5px;
	}
	.sa-innate-form input[type=submit]:hover{
	border:1px solid#db3b2b;
	background:#212120;
	color:#fff;
	}
	
	.sa-innate-form button{
	border:1px solid#212120;
	background:#212120;
	color:#fff;
	padding:10px 25px;
	font-size:14px;
	margin-top:5px;
	}
	.sa-innate-form button:hover{
	border:1px solid#141A00;
	background:#141A00;
	color:#fff;
	}
    .sa-innate-form p{
        font-size:13px;
        padding-top:10px;
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
                <li class="active">
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
                    <a class="navbar-brand" href=""> Remote Control </a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav navbar-right">
                        <li>
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="ti-panel"></i>
				<p>Stats</p>
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
                        <div class="card" style="height: 600px;">
                            <div class="header">
                                <h4 class="title" align="center"> Remote Control For Devices </h4>
                                <div align="center"> 
                                 <p class="category"> Remote devices management system </p>
                                </div>
                            </div>


<br>
<br>


<div class="form-body">

    <ul class="nav nav-tabs final-login">
        <li class="active">
             <a data-toggle="tab" href="#sectionA"> 
               <i class="fa fa-sitemap"></i>
               <i class="fa fa-sliders"></i>
               <i class="fa fa-shield"></i>
                Administrator 
             </a>
             </li>

          <li>
          <a data-toggle="tab" href="#sectionB">  
            <i class="fa fa-desktop"></i>
            <i class="fa fa-tablet"></i> 
            <i class="fa fa-mobile"></i> 
              Devices 
          </a>
        </li>
 
    </ul>

    <div class="tab-content">
        <div id="sectionA" class="tab-pane fade in active">
        <div class="innter-form">
            <form action="__ROOT__/allow_administrator.py" method="post" class="sa-innate-form" >
             <i class="fa fa-user"></i>
            <label> IP OF USER </label>    
            <input type="text" name="ip_allow" placeholder="GET IP">
            <button type="submit" name="submit_allow" style="width:100%;"> 
	      <span class="glyphicon glyphicon-user""></span>
              Add administrator 
              <span class="glyphicon glyphicon-user"></span>
            </button>
            </form>
            </div>


            <div class="clearfix"></div>
        </div>


        <div id="sectionB" class="tab-pane fade">
	 <div class="innter-form">
            <form action="__ROOT__/block_device.py" method="post" class="sa-innate-form" method="post">
             <i class="fa fa-user"></i>
            <label> IP OF DEVICE </label>    
            <input type="text" name="ip_block" placeholder="GET DEVICE IP">
            <button type="submit" name="submit_block" style="width:100%;"> 
	      <span class="glyphicon glyphicon-user""></span>
               BLOCK DEVICE 
              <span class="glyphicon glyphicon-user"></span>
            </button>
            </form>
            </div>
        </div>
    </div>
    </div>
    </div>
    </div>
    </div>

           

                    
                            </div>
                        </div>
                    </div>




        

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

