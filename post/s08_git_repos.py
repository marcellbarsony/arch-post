import os
import shutil
import subprocess
import sys
from .s05_bitwarden import *


class Git():

    """Repository setup"""

    @staticmethod
    def repo_clone(user, gh_user, repo, dir):
        github_user = Bitwarden.rbw_get('github', gh_user)
        cmd = f'git clone git@github.com:{github_user}/{repo}.git /home/{user}/{dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] REPO clone', repo)
        except Exception as err:
            print('[-] REPO clone', repo, err)
            sys.exit(1)

    @staticmethod
    def repo_chdir(user, dir):
        dst = f'/home/{user}/{dir}'
        try:
            os.chdir(dst)
            print('[+] REPO directory', dst)
        except Exception as err:
            print('[-] REPO directory', err)
            sys.exit(1)

    @staticmethod
    def repo_cfg(gh_user, repo):
        github_user = Bitwarden.rbw_get('github', gh_user)
        cmd = f'git remote set-url origin git@github.com:{github_user}/{repo}.git'
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] REPO set-url', repo)
        except Exception as err:
            print('[-] REPO set-url', repo, err)
            sys.exit(1)


class Dotfiles():

    """Dotfiles setup"""

    @staticmethod
    def move(user):
        src_list = [ f'/home/{user}/.config/rbw', f'/home/{user}/.config/gh' ]
        dst = '/tmp'
        for src in src_list:
            shutil.copytree(src, dst)
        shutil.rmtree(f'/home/{user}/.config')

    @staticmethod
    def move_back(user):
        src_list = [ '/tmp/rbw', '/tmp/gh' ]
        dst = f'/home/{user}/.config'
        for src in src_list:
            shutil.copytree(src, dst)
