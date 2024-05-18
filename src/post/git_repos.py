import getpass
import logging
import os
import subprocess
import sys


def repo_clone(gh_user: str, repo: str):
    dir = f"/home/{getpass.getuser()}/.local/git/{repo}"
    cmd = f"git clone git@github.com:{gh_user}/{repo}.git {dir}"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.warning(f"already exists: {repo}")
            pass
        else:
            logging.error(f"{cmd}\n{repr(err)}")
            sys.exit(1)

def repo_chdir(repo: str):
    dir = f"/home/{getpass.getuser()}/.local/git/{repo}"
    try:
        os.chdir(dir)
        logging.info(dir)
    except Exception as err:
        logging.error(f"{dir}: {err}")
        sys.exit(1)

def repo_cfg(gh_user: str, repo: str):
    cmd = f"git remote set-url origin git@github.com:{gh_user}/{repo}.git"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
