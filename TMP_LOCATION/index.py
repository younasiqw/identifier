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
import requests
import json
import cgi, cgitb 
#cgitb.enable()  # for troubleshooting
import MySQLdb
import time
import uuid
import mode
import devices_blocked
from connect import CONNECTION


print """
<html>
<head>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<script>
$(document).ready(function(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showLocation);
    }else{ 
        $('#location').html('Geolocation is not supported by this browser.');
    }
});

function showLocation(position)
         {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    $.ajax({
        type:'POST',
        url:'index.py',
        data:'latitude='+latitude+'&longitude='+longitude,
        success:function(msg)
             {
            if(msg)
              {
               $("#location").html(msg)
                  }
             else
               {
                $("#location").html('Not Available');
                  }
              }
            });
           }



</script>

<style>
body
{
background: #69503C url(img/radar2.gif);
background-repeat: no-repeat;
background-size: 30% 50%;
background-position: 50% 40%; 
}


.blink_me {
  animation: blinker 2s linear infinite;
  color: white;
  font-weight: bold;
  font-size: 50px;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}

</style>

</head>

<body bg>

   <p hidden>Your Location: <span id="location"></span></p> 


    <div class="blink_me" align="center"> SEARCH LOCATION </div>

</body>
</html>
"""


device_id =  cgi.escape(os.environ["REMOTE_ADDR"])
last_ip   =  cgi.escape(os.environ["REMOTE_ADDR"])
fingerprint = uuid.uuid4().hex 

data = cgi.FieldStorage()

latitude = data['latitude'].value
longitude = data['longitude'].value

send_url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=" + latitude +"," + longitude + "&sensor=true/false"
request = requests.get(send_url)
json = json.loads(request.text)

address = json['results'][0]['formatted_address']

all_info = "{ lat: " + latitude + ", " + "lng: " + longitude + ", " + "info: " + "''" + "Device Fingerprint: " + device_id  + " <br> " + "Address: " + address + "''" + " }" 


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db = MySQLdb.connect(host,user,passw,dbs)


cursor = db.cursor()

sql = """ select * from system_settings where mode = 'on' """

try:
   cursor.execute(sql)
   results = cursor.fetchall()

   for row in results:
       mode = row[1]
       time_of_renewal = row[2]
       time_of_renewal = float(time_of_renewal)

       sql_norm_dev = """insert into devices(device_id, last_ip, latitude, longitude, address, fingerprint, all_info) values ('%s','%s','%s','%s','%s','%s','%s')"""%(device_id,last_ip,latitude,longitude,address,fingerprint, all_info)

       sql_back_dev = """insert into backup_devices(device_id, last_ip, latitude, longitude, address, fingerprint, all_info) values ('%s','%s','%s','%s','%s','%s','%s')"""%(device_id,last_ip,latitude,longitude,address,fingerprint,all_info)

       cursor.execute(sql_norm_dev)
       cursor.execute(sql_back_dev)

       time.sleep(time_of_renewal)

   db.commit()
   
   #print "Content-type: text/plain\r\n\r\n",
   #print "Insert data ok"

except:
   db.rollback()
   db.close()
 
   #print "Content-type: text/plain\r\n\r\n",
   #print "Insert data error"



# disconnect from server
db.close()
