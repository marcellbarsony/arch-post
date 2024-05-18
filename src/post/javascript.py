import logging
import subprocess
# import sys


"""Docstring for JavaScript NPM setup"""

def npm_install():
    """https://www.npmjs.com/package/live-server"""
    cmd = f"npm install -g live-server"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        # sys.exit(1)
