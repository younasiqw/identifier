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
from connect import CONNECTION

#print 'Content-type:text/html\r\n\r\n'

IP = cgi.escape(os.environ["REMOTE_ADDR"])


conn = CONNECTION("", "", "", "")

host  =  conn.host
user  =  conn.user
passw =  conn.passw
dbs   =  conn.dbs


db = MySQLdb.connect(host,user,passw,dbs)


cursor = db.cursor()


sql = """select ALLOW_IP_LIST from administrator where id ='1' """

try:
   cursor.execute(sql)
   result = cursor.fetchall()
   

   for   row in result:

         ALLOW_IP_LIST = row[0]   

         if IP not in ALLOW_IP_LIST:
             print """
<html>
<head>

<style>
@import 'https://fonts.googleapis.com/css?family=Inconsolata';

html {
  min-height: 100%;
}

body {
  box-sizing: border-box;
  height: 100%;
  background-color: #000000;
  background-image: radial-gradient(#11581E, #041607);
  font-family: 'Inconsolata', Helvetica, sans-serif;
  font-size: 1.5rem;
  color: rgba(128, 255, 128, 0.8);
  text-shadow:
      0 0 1ex rgba(51, 255, 51, 1),
      0 0 2px rgba(255, 255, 255, 0.8);
}

.overlay {
  pointer-events: none;
  position: absolute;
  width: 100%;
  height: 100%;
  background:
      repeating-linear-gradient(
      180deg,
      rgba(0, 0, 0, 0) 0,
      rgba(0, 0, 0, 0.3) 50%,
      rgba(0, 0, 0, 0) 100%);
  background-size: auto 4px;
  z-index: 99;
}

.overlay::before {
  content: "";
  pointer-events: none;
  position: absolute;
  display: block;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(
      0deg,
      transparent 0%,
      rgba(32, 128, 32, 0.2) 2%,
      rgba(32, 128, 32, 0.8) 3%,
      rgba(32, 128, 32, 0.2) 3%,
      transparent 100%);
  background-repeat: no-repeat;
  animation: scan 7.5s linear 0s infinite;
}

@keyframes scan {
  0%        { background-position: 0 -100vh; }
  35%, 100% { background-position: 0 100vh; }
}

.terminal {
  box-sizing: inherit;
  position: absolute;
  height: 100%;
  width: 1000px;
  max-width: 100%;
  padding: 4rem;
  text-transform: uppercase;
}

.output {
  color: rgba(128, 255, 128, 0.8);
  text-shadow:
      0 0 1px rgba(51, 255, 51, 0.4),
      0 0 2px rgba(255, 255, 255, 0.8);
}

.output::before {
  content: "> ";
}

/*
.input {
  color: rgba(192, 255, 192, 0.8);
  text-shadow:
      0 0 1px rgba(51, 255, 51, 0.4),
      0 0 2px rgba(255, 255, 255, 0.8);
}

.input::before {
  content: "$ ";
}
*/

a {
  color: #fff;
  text-decoration: none;
}

a::before {
  content: "[";
}

a::after {
  content: "]";
}

.errorcode {
  color: white;
}
</style>

</head>

<body>

<div class="overlay"></div>
<div class="terminal">
  <h1>Error <span class="errorcode">404</span></h1>
  <p class="output"> Access to the location tracking system is prohibited </p>
</div>


</body>
</html>
"""
             os._exit(1)

         #else: 
          #   print ''

             


except:
       db.close()
