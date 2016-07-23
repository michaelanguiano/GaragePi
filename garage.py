#!/usr/bin/python

import os
import sys
import subprocess
import cgi


# cycle relay on and off to open/close garage door
args = ["/usr/bin/sudo", "/home/manguiano/Dropbox/Documents/Scripts/Bash/Devantech.sh"]
subprocess.call(args)

#door_status = "DOOR OPEN"
# door_status = "Garage"
# font_size = "400%"

# print """\
# <html>
# <body>
# <img src="http://192.168.1.79:8080/shot.jpg" alt="Photo" width="500" height="400" /><br>
# <form method="get" action="garage.py">
# <input type="submit" value="%s" style="font-face: 'Comic Sans MS'; font-size: %s; color: green; background-color: #FFFFC0; border: 3pt ridge lightgrey; height: 500px; width: 500px">
# </form>
# </body>
# </html>
# """ % (door_status, font_size)

print """\
<html>
<head>
<meta http-equiv="refresh" content="0; url=index.garage.html">
</head>
</html>
"""
