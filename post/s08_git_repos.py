import logging
import os
import shutil
import subprocess
import sys
from .s05_bitwarden import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Git():

    """Repository setup"""

    def __init__(self, user, gh_user):
        self.user = user
        self.gh_user = gh_user

    def repo_clone(self, repo: str, dir: str):
        github_user = Bitwarden().rbw_get('github', self.gh_user)
        cmd = f'git clone git@github.com:{github_user}/{repo}.git /home/{self.user}/{dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f'Repository: Clone {repo}')
        except Exception as err:
            logger.error(f'Repository: Clone {repo} {err}')
            sys.exit(1)

    def repo_chdir(self, dir: str):
        dst = f'/home/{self.user}/{dir}'
        try:
            os.chdir(dst)
            logger.info(f'Repository: directory {dst}')
        except Exception as err:
            logger.error(f'Repository: directory {dst} {err}')
            sys.exit(1)

    def repo_cfg(self, repo: str):
        github_user = Bitwarden().rbw_get('github', self.gh_user)
        cmd = f'git remote set-url origin git@github.com:{github_user}/{repo}.git'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.error(f'Repository: Set-url {repo}')
        except Exception as err:
            logger.error(f'Repository: Set-url {repo} {err}')
            sys.exit(1)


class Dotfiles():

    """Dotfiles setup"""

    def __init__(self, user):
        self.user = user

    def move(self):
        src_list = [ f'/home/{self.user}/.config/rbw', f'/home/{self.user}/.config/gh' ]
        dst = '/tmp'
        for src in src_list:
            shutil.copytree(src, dst)
        shutil.rmtree(f'/home/{self.user}/.config')
        logger.info('Dotfiles: Moving dotfiles')

    def move_back(self):
        src_list = [ '/tmp/rbw', '/tmp/gh' ]
        dst = f'/home/{self.user}/.config'
        for src in src_list:
            shutil.copytree(src, dst)
        logger.info('Dotfiles: Moving dotfiles back')
