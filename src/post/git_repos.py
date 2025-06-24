import logging
import subprocess
import sys

def repo_clone(gh_user: str, repo: str, dst: str):
    cmd = ["git", "clone", f"git@github.com:{gh_user}/{repo}.git", dst]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        if err.returncode == 128:
            logging.warning("already exists", repo)
            pass
        else:
            logging.error("%s\n%s", cmd, repr(err))
            sys.exit(1)

def repo_cfg(gh_user: str, repo: str):
    cmd = ["git", "remote", "set-url", "origin", f"git@github.com:{gh_user}/{repo}.git"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
        sys.exit(1)

def remove(dst: str):
    cmd = ["rm", "-rf", dst]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
        sys.exit(1)

def dotfiles_clone(gh_user: str, dst: str):
    cmd = ["git", "clone", f"git@github.com:{gh_user}/dotfiles.git", dst]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, repr(err))
        sys.exit(1)
