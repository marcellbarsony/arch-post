import logging
import os
import subprocess
import sys


class Git():

    """Repository setup"""

    def __init__(self, user: str, gh_user: str, repo: str):
        self.repo = repo
        self.dir = f"/home/{user}/.local/git/{repo}"
        self.gh_user = gh_user

    def repo_clone(self):
        cmd = f"git clone git@github.com:{self.gh_user}/{self.repo}.git {self.dir}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                logging.warning(f"already exists: {self.repo}")
                pass
            else:
                logging.error(f"{cmd}: {repr(err)}")
                sys.exit(1)

    def repo_chdir(self):
        try:
            os.chdir(self.dir)
            logging.info(self.dir)
        except Exception as err:
            logging.error(f"{self.dir}: {err}")
            sys.exit(1)

    def repo_cfg(self):
        cmd = f"git remote set-url origin git@github.com:{self.gh_user}/{self.repo}.git"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)

class Dotfiles():

    """Docstring for Dotfiles"""

    def __init__(self, user: str, gh_user: str):
        self.dir = f"/home/{user}/.config"
        self.gh_user = gh_user

    def remove(self):
        cmd = f"rm -rf {self.dir}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Dotfiles :: {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Dotfiles :: {cmd}: {err}")
            sys.exit(1)

    def clone(self):
        cmd = f"git clone git@github.com:{self.gh_user}/dotfiles.git {self.dir}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Dotfiles :: {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Dotfiles :: {cmd}: {repr(err)}")
            sys.exit(1)

    def cfg(self):
        cmd = f"git remote set-url origin git@github.com:{self.gh_user}/dotfiles.git"
        try:
            os.chdir(self.dir)
            logging.info(f"Dotfiles :: chdir - {self.dir}")
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"Dotfiles :: {cmd}: {err}")
            sys.exit(1)


class Progs():

    """Docstring for Progs"""

    def __init__(self, user: str, gh_user: str):
        self.dir = f"/home/{user}/.local/bin"
        self.gh_user = gh_user

    def clone(self):
        cmd = f"git clone git@github.com:{self.gh_user}/arch-progs.git {self.dir}"
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Progs - {cmd}")
        except subprocess.CalledProcessError as err:
            logging.error(f"Progs - {cmd}: {repr(err)}")
            sys.exit(1)

    def cfg(self):
        cmd = f"git remote set-url origin git@github.com:{self.gh_user}/arch-progs.git"
        try:
            os.chdir(self.dir)
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logging.info(f"Progs - cmd")
        except subprocess.CalledProcessError as err:
            logging.error(f"Progs - {cmd}: {err}")
            sys.exit(1)
