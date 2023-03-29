#!/usr/bin/env python3
"""
Author : FName SName <mail@domain.com>
Date   : 2023-03
"""


import argparse
import configparser
import getpass
from post.s01_pacman import *
from post.s02_init import *
from post.s03_network import *
from post.s04_aur import *
from post.s05_bitwarden import *
from post.s06_ssh import *
from post.s07_git import *
from post.s08_git_repos import *
from post.s09_install import *
from post.s10_shell import *
from post.s11_services import *
from post.s12_customization import *
from post.s13_languages import *


class Main():

    """Arch post-installation setup"""

    @staticmethod
    def Initialize():
        Pacman.dependencies()

        dmidata = Initialize.dmi_data()
        Initialize.timezone(timezone)
        Initialize.sys_clock()

        while True:
            if dmidata != 'virtualbox' and 'vmware':
                Network.wifi_activate(network_toggle)
                Network.wifi_connect(network_ssid, network_key)
            status = Network.check(network_ip, network_port)
            if status == True:
                break

    @staticmethod
    def Aur():
        aur_dir = Helper.directory(user, aur_helper)
        Helper.clone(aur_helper, aur_dir)
        Helper.makepkg(aur_dir)

    @staticmethod
    def PasswordManager():
        while True:
            status = Bitwarden.rbw_register(bw_mail, bw_url, bw_lock)
            if status == True:
                break

    @staticmethod
    def SSH():
        SecureShell.kill()
        SecureShell.start()
        SecureShell.keygen(user, ssh_key, gh_mail)
        SecureShell.add(user)

    @staticmethod
    def GitSetup():
        GitHub.auth_login(gh_token)
        GitHub.auth_status()
        GitHub.add_pubkey(user, gh_pubkey)
        GitHub.test()
        GitHub.known_hosts()

        for repo in repositories:
            dir = f'.local/git/{repo}'
            Git.repo_clone(user, gh_user, repo, dir)
            Git.repo_chdir(user, dir)
            Git.repo_cfg(gh_user, repo)

        repo = 'dotfiles'
        dir = '.config'
        Dotfiles.move(user)
        Git.repo_clone(user, gh_user, repo, dir)
        Git.repo_chdir(user, dir)
        Git.repo_cfg(gh_user, dir)
        Dotfiles.move_back(user)

    @staticmethod
    def Installation():
        # Install.install(packages)
        # Install.install(audio)
        # Install.install(aur)
        # Install.install(display)
        # Install.install(fonts)
        # Install.install(hacking)
        # Install.install(pacman)
        pass

    @staticmethod
    def Shell():
        Shell.change(shell)
        Shell.config(user)
        Shell.tools(user)

    @staticmethod
    def Services():
        Services.enable()

    @staticmethod
    def Customization():
        Customization.background(user)
        Customization.fonts()
        Customization.login_manager()
        Customization.pacman()
        Customization.pipewire()
        Customization.wayland()
        Customization.spotify()
        Customization.xdg_dirs()

    @staticmethod
    def Languages():
        Python.venv()
        #Python.modules(python_modules)
        Ruby.install()
        Ruby.gems()



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
    shell =             config.get('shell', 'shell')
    ssh_key =           config.get('ssh','key')
    timezone =          config.get('timezone', 'timezone')

    config.read('cfg/config_packages.ini')

    python = config.get('packages', 'coreutils').split(', ')
    # TODO: check & add

    user = getpass.getuser()

    Main.Initialize()
    Main.Aur()
    Main.PasswordManager()
    Main.SSH()
    #Main.GitSetup()
    #Main.Installation()
    #Main.Shell()
    #Main.Services()
    #Main.Customization()
    #Main.Languages()
