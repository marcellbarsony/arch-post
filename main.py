#!/usr/bin/env python3
"""
Author : FName SName <mail@domain.com>
Date   : 2023 April
"""


import argparse
import configparser
import getpass
import sys

from post import AurHelper
from post import Bitwarden
from post import Customization
from post import Dotfiles
from post import GitSetup
from post import Git
from post import Initialize
from post import Network
from post import OpenSSH
from post import Pacman
from post import Python
from post import Ruby
from post import Rust
from post import Services
from post import WiFi
from post import Zsh


class Main():

    """Arch post-installation setup"""

    @staticmethod
    def initialize():
        install = Pacman()
        install.dependencies()

        init = Initialize()
        init.timezone(timezone)
        init.sys_clock()

        while True:
            if Network().check(network_ip, network_port):
                break
            else:
                WiFi().toggle(network_toggle)
                WiFi().connect(network_ssid, network_key)

    @staticmethod
    def aurHelper():
        pikaur = AurHelper(user, aur_helper)
        pikaur.makedir()
        pikaur.clone()
        pikaur.makepkg()

    @staticmethod
    def passwordManager():
        rbw = Bitwarden()
        rbw.install(aur_helper)
        while True:
            if rbw.register(bw_mail, bw_lock):
                break
            # TODO: Check algorithm
            user_in = input(f'Failed to authenticate. Retry? Y/N ')
            if user_in.upper() == 'N':
                sys.exit(1)

    @staticmethod
    def ssh():
        agent = OpenSSH(user)
        agent.keygen(ssh_key, gh_mail)

    @staticmethod
    def git():
        github = GitSetup()
        github.authLogin(gh_token)
        github.authStatus()
        github.addPubkey(user, gh_pubkey)
        github.knownHosts()
        github.test()
        github.config(gh_user, gh_mail)

        git = Git(user, gh_user)
        for repo in repositories:
            dir = f'src/{repo}'
            git.repoClone(repo, dir)
            git.repoChdir(dir)
            git.repoCfg(repo)

        dots = Dotfiles(user)
        repo = 'dotfiles'
        dir = '.config'
        dots.move()
        git.repoClone(repo, dir)
        git.repoChdir(dir)
        git.repoCfg(repo)
        dots.moveBack()

    @staticmethod
    def installation():
        pacman = Pacman()
        pacman.install()
        #AurHelper.install(package)

    @staticmethod
    def setZsh():
        zsh = Zsh(user)
        zsh.set()
        zsh.config()
        #zsh.tools()

    @staticmethod
    def systemd():
        systemctl = Services()
        systemctl.enable()

    @staticmethod
    def customize():
        c = Customization()
        c.background(user)
        c.login_manager()
        #c.pacman()
        c.pipewire()
        c.wayland()
        c.spotify()
        c.xdgDirs()

    @staticmethod
    def development():
        python = Python()
        python.venv()
        #python.modules(python_modules)
        ruby = Ruby()
        ruby.install()
        ruby.gems()
        rust = Rust()


if __name__ == '__main__':
    """ Initialize argparse """

    parser = argparse.ArgumentParser(
                prog='python3 setup.py',
                description='Arch post install',
                epilog='TODO'  # TODO
                )
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read('config.ini')

    aur_helper =        config.get('aur', 'helper')
    bw_mail =           config.get('bitwarden', 'mail')
    bw_url =            config.get('bitwarden', 'url')
    bw_lock =           config.get('bitwarden', 'lock')
    gh_mail =           config.get('bitwarden_data', 'github_mail')
    gh_user =           config.get('bitwarden_data', 'github_user')
    gh_token =          config.get('bitwarden_data', 'github_token')
    spotify_client_id = config.get('bitwarden_data', 'spotify_client_id')
    spotify_secret =    config.get('bitwarden_data', 'spotify_client_secret')
    spotify_device_id = config.get('bitwarden_data', 'spotify_device_id')
    spotify_mail =      config.get('bitwarden_data', 'spotify_mail')
    spotify_user =      config.get('bitwarden_data', 'spotify_user')
    dependencies =      config.get('dependencies', 'dependencies')
    gh_pubkey =         config.get('github', 'pubkey')
    network_ip =        config.get('network','ip')
    network_port =      config.get('network','port')
    network_toggle =    config.get('network','wifi')
    network_key =       config.get('network','wifi_key')
    network_ssid =      config.get('network','wifi_ssid')
    repositories =      config.get('repositories','repositories').split(', ')
    ssh_key =           config.get('ssh','key')
    timezone =          config.get('timezone', 'timezone')

    user = getpass.getuser()

    Main.initialize()
    Main.aurHelper()
    Main.passwordManager()
    Main.ssh()
    Main.git()
    Main.installation()
    Main.setZsh()
    #Main.systemd()
    Main.customize()
    #Main.development()
