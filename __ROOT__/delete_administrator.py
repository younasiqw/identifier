#!/usr/bin/python

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
import administrator
from connect import CONNECTION

form = cgi.FieldStorage() 


if form.getvalue('delete_administrator'):
   delete_administrator = form.getvalue('delete_administrator')


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs



db = MySQLdb.connect(host,user,passw,dbs)

cursor = db.cursor()

sql_delete_admin = """ UPDATE administrator SET ALLOW_IP_LIST = REPLACE(ALLOW_IP_LIST, '%s', '')""" %(delete_administrator)

try:

   cursor.execute(sql_delete_admin)
   db.commit()

   

   if os.environ['REQUEST_URI'] != '__ROOT__/delete_administrator.py':
      print '''<script>
            alert('The administrator was deleted from the system');
           </script>
            <script>location.href='/task_manager.py'</script>'''
      
     # print os.environ["REQUEST_URI"]


   #else:
   #   print '''<script>
   #         alert('The time has not been activated');
   #        </script>'''

except:
  
   db.rollback()

db.close()

