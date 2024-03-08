#!/usr/bin/python3

"""
Fabric script that distributes an archive to my web servers
"""

import os
from fabric.api import put, run, env


env.hosts = ['3.85.33.147', '100.25.13.217']
env.user = 'ubuntu'


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
        return True
    except Exception as e:
        return False
