#!/usr/bin/python3

"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""

import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """"Generate the achieve file"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        file_size = os.path.getsize(file)
        print(f"web_static packed: {file} -> {file_size}Bytes")
        return file
    except:
        return None
