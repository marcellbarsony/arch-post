#!/usr/bin/env python3
"""
Author : FName SName <mail@domain.com>
Date   : 2023 May
"""


import argparse
import configparser
import getpass
import os
import sys

from src.post import AURhelper
from src.post import Bitwarden
from src.post import Customization
from src.post import GitSetup
from src.post import Git
from src.post import Dotfiles
from src.post import SysTime
from src.post import Mirrorlist
from src.post import Network  # TODO
from src.post import SSHagent
from src.post import Pacman
from src.post import Pipewire
from src.post import Rust
from src.post import DisplayManager
from src.post import WiFi  # TODO
from src.post import Zsh
from src.post import XDGStandard


class Main():

    """Arch post-installation setup"""

    def __init__(self):
        self.cwd = os.getcwd()
        self.user = getpass.getuser()

    @staticmethod
    def systime():
        i = SysTime()
        i.time()
        i.timezone(timezone)

    @staticmethod
    def network():
        print('TODO: Network connection')
        pass

    @staticmethod
    def pacman():
        p = Pacman()
        p.keyring()
        m = Mirrorlist()
        m.backup()
        m.update()

    def rust(self):
        r = Rust()
        r.toolchain()

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
            user_in = input('Failed to authenticate. Retry? Y/N ')
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

        d = Dotfiles(self.user, gh_user)
        d.remove()
        d.clone()
        d.cfg()

        for repo in repositories:
            r = Git(self.user, gh_user, repo)
            r.repo_clone()
            r.repo_chdir()
            r.repo_cfg()

    def shell(self):
        z = Zsh(self.user)
        z.chsh()
        z.config()
        z.tools()

    @staticmethod
    def audio():
        p = Pipewire()
        p.service()

    @staticmethod
    def display():
        l = DisplayManager(displayman)
        l.install(aurhelper)
        l.service()

    def customize(self):
        c = Customization()
        c.background(self.user)
        c.spotify()

    def xdg(self):
        x = XDGStandard(self.user)
        x.xdg_force()
        x.xdg_remove(self.user)
        x.home()
        x.rust()


if __name__ == '__main__':

    """Initialize argparse"""

    uid = os.getuid()
    if uid == 0:
        print(f'[-] Executed as root (UID={uid})')
        sys.exit(1)

    parser = argparse.ArgumentParser(
                prog='python3 arch-post.py',
                description='Arch post-install setup',
                epilog='TODO'
                )
    args = parser.parse_args()

    """Initialize global variables"""

    config = configparser.ConfigParser()
    config.read('_config.ini')

    aurhelper =         config.get('aur', 'helper')
    bw_mail =           config.get('bitwarden', 'mail')
    bw_lock =           config.get('bitwarden', 'lock')
    git_mail =          config.get('bitwarden_data', 'github_mail')
    git_user =          config.get('bitwarden_data', 'github_user')
    git_token =         config.get('bitwarden_data', 'github_token')
    spotify_client_id = config.get('bitwarden_data', 'spotify_client_id')
    spotify_secret =    config.get('bitwarden_data', 'spotify_client_secret')
    spotify_device_id = config.get('bitwarden_data', 'spotify_device_id')
    spotify_mail =      config.get('bitwarden_data', 'spotify_mail')
    spotify_user =      config.get('bitwarden_data', 'spotify_user')
    displayman =        config.get('displayman', 'displayman')
    git_pubkey =        config.get('github', 'pubkey')
    network_ip =        config.get('network','ip')
    network_port =      config.get('network','port')
    network_toggle =    config.get('network','wifi')
    network_key =       config.get('network','wifi_key')
    network_ssid =      config.get('network','wifi_ssid')
    repositories =      config.get('repositories','repositories').split(', ')
    ssh_key =           config.get('ssh','key')
    timezone =          config.get('timezone', 'timezone')

    m = Main()
    m.systime()
    m.network()
    m.rust()
    m.pacman()
    m.aur()
    m.password_manager()
    m.ssh()
    m.git()
    m.shell()
    m.audio()
    m.display()
    m.customize()
    m.xdg()
