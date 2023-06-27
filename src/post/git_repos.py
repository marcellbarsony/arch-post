import logging
import os
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Git():

    """Repository setup"""

    def __init__(self, user: str, gh_user: str, repo: str):
        self.repo = repo
        self.dir = f'/home/{user}/.local/got/{repo}'
        self.gh_user = gh_user

    def repo_clone(self):
        cmd = f'git clone git@github.com:{self.gh_user}/{self.repo}.git {self.dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Clone {self.repo}')
        except subprocess.CalledProcessError as err:
            if err.returncode == 128:
                logger.warning(f'Directory exists: {self.repo}')
                pass
            else:
                logger.error(f'Clone {self.repo}')
                print(repr(err))
                sys.exit(1)

    def repo_chdir(self):
        try:
            os.chdir(self.dir)
        except Exception as err:
            logger.error(f'chdir >> {self.dir} {err}')
            sys.exit(1)

    def repo_cfg(self):
        cmd = f'git remote set-url origin git@github.com:{self.gh_user}/{self.repo}.git'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Set-url {self.repo}')
        except subprocess.CalledProcessError as err:
            logger.error(f'Set-url {self.repo} {err}')
            sys.exit(1)

class Dotfiles():

    """Docstring for Dotfiles"""

    def __init__(self, user: str, gh_user: str):
        self.dir = f'/home/{user}/.config'
        self.gh_user = gh_user

    def remove(self):
        cmd = f'rm -rf {self.dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Remove existing config')
        except subprocess.CalledProcessError as err:
            logger.error(f'Remove existing config {err}')
            sys.exit(1)

    def clone(self):
        cmd = f'git clone git@github.com:{self.gh_user}/dotfiles.git {self.dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Clone')
        except subprocess.CalledProcessError as err:
            logger.error('Clone')
            print(repr(err))
            sys.exit(1)

    def cfg(self):
        cmd = f'git remote set-url origin git@github.com:{self.gh_user}/dotfiles.git'
        try:
            os.chdir(self.dir)
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Config')
        except subprocess.CalledProcessError as err:
            logger.error(f'Config {err}')
            sys.exit(1)


class Progs():

    """Docstring for Progs"""

    def __init__(self, user: str, gh_user: str):
        self.dir = f'/home/{user}/.local/bin'
        self.gh_user = gh_user

    def clone(self):
        cmd = f'git clone git@github.com:{self.gh_user}/arch-progs.git {self.dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info('Clone')
        except subprocess.CalledProcessError as err:
            logger.error('Clone')
            print(repr(err))
            sys.exit(1)

    def cfg(self):
        cmd = f'git remote set-url origin git@github.com:{self.gh_user}/arch-progs.git'
        try:
            os.chdir(self.dir)
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Config')
        except subprocess.CalledProcessError as err:
            logger.error(f'Config {err}')
            sys.exit(1)
