import logging
import subprocess


"""Docstring for JavaScript NPM setup"""

def npm_install():
    """https://www.npmjs.com/package/live-server"""
    cmd = f"npm install -g live-server"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.warning(f"{cmd}\n{repr(err)}")
        pass
    else:
        logging.info(cmd)
