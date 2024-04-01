import bitwarden
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
        logging.info(f"Dotfiles :: {cmd}")
    except subprocess.CalledProcessError as err:
        logging.error(f"Dotfiles :: {cmd}: {err}")
        sys.exit(1)

def clone(git_user: str):
    dir = f"/home/{getpass.getuser()}/.config"
    gh_user = bitwarden.rbw_get("github", git_user)
    cmd = f"git clone git@github.com:{gh_user}/dotfiles.git {dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(f"Dotfiles :: {cmd}")
    except subprocess.CalledProcessError as err:
        logging.error(f"Dotfiles :: {cmd}: {repr(err)}")
        sys.exit(1)

def cfg(git_user: str):
    dir = f"/home/{getpass.getuser()}/.config"
    gh_user = bitwarden.rbw_get("github", git_user)
    cmd = f"git remote set-url origin git@github.com:{gh_user}/dotfiles.git"
    try:
        os.chdir(dir)
        logging.info(f"Dotfiles :: chdir - {dir}")
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"Dotfiles :: {cmd}: {err}")
        sys.exit(1)
