#!/usr/bin/python3
"""
fab script to compress files from
web_static directory to a .tgz
compressed files
"""
from fabric.api import *
import datetime


def do_pack():
    """
    a fab funtion that takes the
    web_static folder and compress it
    and return path of the compressed file
    else return None
    """
    now = datetime.datetime.now()
    ymd = f"{now.year}{now.month}{now.day}"
    archiveFileName = f"web_static_{ymd}{now.hour}{now.minute}{now.second}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{archiveFileName} web_static")
    if result.succeeded:
        return local(f"realpath {archiveFileName}")
    return None
