#!/usr/bin/env python3
"""
Author : FName SName <mail@domain.com>
Date   : 2023 April
"""


import argparse
import configparser
import getpass
import os
import sys

from src.lang import Python
from src.lang import Ruby
#from src.lang import Rust

from src.post import AURhelper
from src.post import Bitwarden
from src.post import Customization
from src.post import GitSetup
from src.post import Git
from src.post import Dotfiles
from src.post import Initialize
from src.post import Network
from src.post import SSHagent
from src.post import Pacman
from src.post import Systemd
from src.post import WiFi
from src.post import Zsh
from src.post import Finalize


class Main():

    """Arch post-installation setup"""

    def __init__(self):
        self.cwd = os.getcwd()
        self.user = getpass.getuser()
        self.sudo = Initialize.get_sudo(self.user)

    @staticmethod
    def init():
        i = Initialize()
        i.sys_timezone(timezone)
        i.sys_clock()

        while True:
            if Network().check(network_ip, network_port):
                break
            else:
                w = WiFi()
                w.toggle(network_toggle)
                w.connect(network_ssid, network_key)

    def aur(self):
        a = AURhelper(self.user, aurhelper)
        a.make_dir()
        a.clone()
        a.make_pkg()

    @staticmethod
    def password_manager():
        rbw = Bitwarden()
        rbw.install(aurhelper)
        while True:
            if rbw.register(bw_mail, bw_lock):
                break
            user_in = input(f'Failed to authenticate. Retry? Y/N ')
            if user_in.upper() == 'N':
                sys.exit(1)

    def ssh(self):
        a = SSHagent(self.user, self.cwd)
        a.config()
        a.service_set()
        a.service_start()
        a.key_gen(ssh_key, git_mail)
        a.key_add()

    def git(self):
        g = GitSetup()
        gh_user = g.get_user(git_user)
        g.auth_login(git_token)
        g.auth_status()
        g.add_pubkey(self.user, git_pubkey)
        g.known_hosts()
        g.ssh_test()
        g.config(gh_user, git_mail)

        for repo in repositories:
            r = Git(self.user, gh_user, repo)
            r.repo_clone()
            r.repo_chdir()
            r.repo_cfg()

        d = Dotfiles(self.user, gh_user)
        d.temp_dir()
        d.move()
        d.repo_clone()
        d.repo_chdir()
        d.repo_cfg()
        d.move_back()

    def installation(self):
        p = Pacman()
        p.explicit_keyring()

    def zshell(self):
        z = Zsh(self.user)
        z.chsh()
        z.config()
        z.tools()

    @staticmethod
    def systemd():
        d = Systemd()
        d.enable()

    def customize(self):
        c = Customization()
        c.background(self.user)
        c.pipewire()
        c.wayland()
        c.spotify()
        c.xdg_dirs(self.user)

    @staticmethod
    def development():
        py = Python()
        py.venv()
        #py.modules(python_modules)
        ruby = Ruby()
        ruby.install()
        ruby.gems()
        #rust = Rust()

    def finalize(self):
        f = Finalize(self.user)
        f.clean_home()


if __name__ == '__main__':
    """ Initialize argparse """

    uid = os.getuid()
    if uid == 0:
        print(f'[-] Executed as root (UID={uid})')
        sys.exit(1)

    parser = argparse.ArgumentParser(
                prog='python3 setup.py',
                description='Arch post install',
                epilog='TODO'  # TODO
                )
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read('_config.ini')

    aurhelper =        config.get('aur', 'helper')
    bw_mail =           config.get('bitwarden', 'mail')
    bw_url =            config.get('bitwarden', 'url')
    bw_lock =           config.get('bitwarden', 'lock')
    git_mail =           config.get('bitwarden_data', 'github_mail')
    git_user =           config.get('bitwarden_data', 'github_user')
    git_token =          config.get('bitwarden_data', 'github_token')
    spotify_client_id = config.get('bitwarden_data', 'spotify_client_id')
    spotify_secret =    config.get('bitwarden_data', 'spotify_client_secret')
    spotify_device_id = config.get('bitwarden_data', 'spotify_device_id')
    spotify_mail =      config.get('bitwarden_data', 'spotify_mail')
    spotify_user =      config.get('bitwarden_data', 'spotify_user')
    dependencies =      config.get('dependencies', 'dependencies')
    git_pubkey =         config.get('github', 'pubkey')
    network_ip =        config.get('network','ip')
    network_port =      config.get('network','port')
    network_toggle =    config.get('network','wifi')
    network_key =       config.get('network','wifi_key')
    network_ssid =      config.get('network','wifi_ssid')
    repositories =      config.get('repositories','repositories').split(', ')
    ssh_key =           config.get('ssh','key')
    timezone =          config.get('timezone', 'timezone')


    m = Main()
    m.init()
    m.aur()
    m.password_manager()
    m.ssh()
    m.git()
    m.zshell()
    m.installation()
    #m.systemd()
    m.customize()
    #m.development()
    m.finalize()
