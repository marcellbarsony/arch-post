import logging
import os
import shutil
import subprocess
import sys
from .bitwarden import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Git():

    """Repository setup"""

    def __init__(self, user, gh_user):
        self.user = user
        self.gh_user = gh_user

    def repoClone(self, repo: str, dir: str):
        github_user = Bitwarden().rbwGet('github', self.gh_user)
        cmd = f'git clone git@github.com:{github_user}/{repo}.git /home/{self.user}/{dir}'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.info(f'Clone {repo}')
        except Exception as err:
            logger.error(f'Clone {repo} {err}')
            sys.exit(1)

    def repoChdir(self, dir: str):
        dst = f'/home/{self.user}/{dir}'
        try:
            os.chdir(dst)
            logger.info(f'directory {dst}')
        except Exception as err:
            logger.error(f'directory {dst} {err}')
            sys.exit(1)

    def repoCfg(self, repo: str):
        github_user = Bitwarden().rbwGet('github', self.gh_user)
        cmd = f'git remote set-url origin git@github.com:{github_user}/{repo}.git'
        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
            logger.error(f'Set-url {repo}')
        except Exception as err:
            logger.error(f'Set-url {repo} {err}')
            sys.exit(1)


class Dotfiles():

    """Dotfiles setup"""

    def __init__(self, user):
        self.user = user

    def move(self):
        src_dir = f'/home/{self.user}/.config'
        dst_dir = f'/tmp'
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isfile(item_path):
                shutil.move(item_path, dst_dir)
            else:
                shutil.move(item_path, os.path.join(dst_dir, item))

    def moveBack(self):
        src_dir = f'/tmp'
        dst_dir = f'/home/{self.user}/.config'
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isfile(item_path):
                shutil.move(item_path, dst_dir)
            else:
                shutil.move(item_path, os.path.join(dst_dir, item))
