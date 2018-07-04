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
from connect import CONNECTION


device_id =  cgi.escape(os.environ["REMOTE_ADDR"])


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db = MySQLdb.connect(host,user,passw,dbs)


cursor = db.cursor()

sql = """ select device_id from devices_blocked"""

try:
   cursor.execute(sql)
   results = cursor.fetchall()

   for row in results:
       device_id2 = row[0]
 
       if device_id == device_id2:
          print 'This device is blocked '
          os._exit(1) 
       
   

except:

   db.rollback()

db.close()
