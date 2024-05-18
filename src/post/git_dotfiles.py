import getpass
import logging
import os
import subprocess
import sys


"""Docstring for Dotfiles"""

def remove():
    cmd = f"rm -rf /home/{getpass.getuser()}/.config"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)

def clone(gh_user: str):
    dir = f"/home/{getpass.getuser()}/.config"
    cmd = f"git clone git@github.com:{gh_user}/dotfiles.git {dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        sys.exit(1)

def cfg(gh_user: str):
    dir = f"/home/{getpass.getuser()}/.config"
    cmd = f"git remote set-url origin git@github.com:{gh_user}/dotfiles.git"
    try:
        os.chdir(dir)
        logging.info(dir)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
