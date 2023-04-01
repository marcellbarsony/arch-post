import os
import shutil
import subprocess
import sys
from .logger import *
from .s05_bitwarden import *


class Git():

    """Repository setup"""

    def __init__(self):
        self.logger = LogHelper()

    def repo_clone(self, user: str, gh_user: str, repo: str, dir: str):
        github_user = Bitwarden().rbw_get('github', gh_user)
        cmd = f'git clone git@github.com:{github_user}/{repo}.git /home/{user}/{dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.info(f'Repository: Clone {repo}')
        except Exception as err:
            self.logger.error(f'Repository: Clone {repo} {err}')
            sys.exit(1)

    def repo_chdir(self, user: str, dir: str):
        dst = f'/home/{user}/{dir}'
        try:
            os.chdir(dst)
            self.logger.info(f'Repository: directory {dst}')
        except Exception as err:
            self.logger.error(f'Repository: directory {dst} {err}')
            sys.exit(1)

    def repo_cfg(self, gh_user: str, repo: str):
        github_user = Bitwarden().rbw_get('github', gh_user)
        cmd = f'git remote set-url origin git@github.com:{github_user}/{repo}.git'
        try:
            subprocess.run(cmd, shell=True, check=True)
            self.logger.error(f'Repository: Set-url {repo}')
        except Exception as err:
            self.logger.error(f'Repository: Set-url {repo} {err}')
            sys.exit(1)


class Dotfiles():

    """Dotfiles setup"""

    def __init__(self):
        self.logger = LogHelper()

    def move(self, user: str):
        src_list = [ f'/home/{user}/.config/rbw', f'/home/{user}/.config/gh' ]
        dst = '/tmp'
        for src in src_list:
            shutil.copytree(src, dst)
        shutil.rmtree(f'/home/{user}/.config')
        self.logger.info('Dotfiles: Moving dotfiles')

    def move_back(self, user: str):
        src_list = [ '/tmp/rbw', '/tmp/gh' ]
        dst = f'/home/{user}/.config'
        for src in src_list:
            shutil.copytree(src, dst)
        self.logger.info('Dotfiles: Moving dotfiles back')
