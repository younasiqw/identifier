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
import cgi, cgitb 
import MySQLdb
import requests
import administrator
from connect import CONNECTION


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db = MySQLdb.connect(host,user,passw,dbs)

cursor = db.cursor()

mode = "on"
#time_of_renewal = "60"

sql = """ update system_settings set mode = '%s' where id = '1' """ %(mode)

try:

   cursor.execute(sql)
   db.commit()

   if os.environ['REQUEST_URI'] != 'identification/__ROOT__/power_on.py':
      print '''<script>
            alert('The mode has been activated');
           </script>
            <script>location.href='/identification/index.py'</script>'''
      

except:
  
   db.rollback()

db.close()

