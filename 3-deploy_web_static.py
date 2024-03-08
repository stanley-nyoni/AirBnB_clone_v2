#!/usr/bin/python3

"""
Fabric script that distributes an archive to my web servers
"""

import os
from fabric.api import put, run, env
from datetime import datetime


env.hosts = ['3.85.33.147', '100.25.13.217']
env.user = 'ubuntu'


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
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_name_no_ext = file_name.split(".")[0]
        remote_path = "/data/web_static/releases/{}".format(file_name_no_ext)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(remote_path))
        run("sudo tar -xzf /tmp/{} -C {}/".format(file_name, remote_path))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(remote_path, remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(remote_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
