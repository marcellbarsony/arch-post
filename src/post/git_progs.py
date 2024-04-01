import bitwarden
import getpass
import logging
import os
import subprocess
import sys


"""Docstring for Progs"""

def clone(git_user: str):
    dir = f"/home/{getpass.getuser()}/.local/bin"
    gh_user = bitwarden.rbw_get("github", git_user)
    cmd = f"git clone git@github.com:{gh_user}/arch-progs.git {dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(f"Progs - {cmd}")
    except subprocess.CalledProcessError as err:
        logging.error(f"Progs - {cmd}: {repr(err)}")
        sys.exit(1)

def cfg(git_user: str):
    dir = f"/home/{getpass.getuser()}/.local/bin"
    gh_user = bitwarden.rbw_get("github", git_user)
    cmd = f"git remote set-url origin git@github.com:{gh_user}/arch-progs.git"
    try:
        os.chdir(dir)
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(f"Progs - cmd")
    except subprocess.CalledProcessError as err:
        logging.error(f"Progs - {cmd}: {err}")
        sys.exit(1)
