import os
import shutil
import subprocess
import sys


class Git():

    """Repository setup"""

    @staticmethod
    def repo_clone(user, github_user, repo, dir):
        cmd = f'git clone git@github.com:{github_user}/{repo}.git /home/{user}/{dir}'
        try:
            subprocess.run(cmd, shell=True)
            print('[+] REPO clone', repo)
        except Exception as err:
            print('[-] REPO clone', err)
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
    def repo_cfg(github_user, repo):
        cmd = f'git remote set-url origin git@github.com:{github_user}/{repo}.git'
        try:
            subprocess.run(cmd, shell=True)
            print('[+] GIT clone', repo)
        except Exception as err:
            print('[-] GIT clone', err)
            sys.exit(1)


class Dotfiles():

    """Dotfiles setup"""

    @staticmethod
    def move(user):
        src_list = [
            f'/home/{user}/.config/rbw',
            f'/home/{user}/.config/gh'
            ]
        dst = '/tmp'
        for src in src_list:
            shutil.copytree(src, dst)
        shutil.rmtree(f'/home/{user}/.config')

    @staticmethod
    def move_back(user):
        src_list = [
            '/tmp/rbw',
            '/tmp/gh'
        ]
        dst = f'/home/{user}/.config'
        for src in src_list:
            shutil.copytree(src, dst)
