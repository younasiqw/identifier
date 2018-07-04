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
      
       if mode_type == 'off':
          os._exit(1)

except:

       print "Error: unable to fecth data"

# disconnect from server
db_mode.close()
