#!/usr/bin/env python3
"""
Author  : Name Surname <mail@domain.com>
Date    : 2023-03
"""


import argparse
import configparser
import getpass
from post.s01_network import *
from post.s02_init import *
from post.s03_aur import *
from post.s04_bitwarden import *
from post.s05_ssh import *
from post.s06_repositories import *
from post.s07_install import *
from post.s08_shell import *
from post.s09_services import *
from post.s10_customization import *
from post.s11_languages import *


def main():

    def NetConf():
        while True:
            #Network.wifi_activate(network_toggle)
            #Network.wifi_connect(network_ssid, network_key)
            status = Network.check(network_ip, network_port)
            if status == True:
                break

    def Init():
        Initialize.timezone(timezone)
        #Initialize.install(dependencies)

    def AurHelper():
        dir = Aur.clone(user, aur_helper)
        Aur.makepkg(dir)

    def PasswordManager():
        #Bitwarden.rbw_register(bw_mail, bw_url, bw_lock)
        global github_email
        global github_user
        github_email = Bitwarden.rbw_get('github', gh_mail)
        github_user = Bitwarden.rbw_get('github', gh_user)

    def SSH():
        SecureShell.kill()
        SecureShell.start()
        SecureShell.keygen(user, ssh_key, github_email.rstrip('\n'), dir)

    def Repositories():
        for repo in repositories:
            dir = f'.local/git/{repo}'
            Git.repo_clone(user, github_user, repo, dir)
            Git.repo_chdir(user, dir)
            Git.repo_cfg(github_user, repo)

    def Configuration():
        repo = 'dotfiles'
        dir = '.config'
        Dotfiles.move(user)
        Git.repo_clone(user, github_user, repo, dir)
        Git.repo_chdir(user, dir)
        Git.repo_cfg(github_user, dir)
        Dotfiles.move_back(user)

    def Installation():
        Install.install(packages)
        # Install.install(audio)
        # Install.install(aur)
        # Install.install(display)
        # Install.install(fonts)
        # Install.install(hacking)
        # Install.install(pacman)

    def Shell():
        # Shell.change(shell)
        Shell.config(user)
        Shell.tools(user)

    def Services():
        Services.enable()

    def Customization():
        Customization.background()
        Customization.fonts()
        Customization.pacman()
        Customization.spotify()
        Customization.xdg_dirs()

    def Languages():
        Python.venv()
        Python.modules(python_modules)
        Ruby.install()
        Ruby.gems()

    NetConf()
    Init()
    AurHelper()
    PasswordManager()
    SSH()
    #Repositories()
    #Configuration()
    #Installation()
    #Shell()
    #Services()
    #Customization()
    #Languages()


if __name__ == '__main__':
    """ Initialize argparse """

    parser = argparse.ArgumentParser(
                prog='python3 setup.py',
                description='Arch post install',
                epilog='TODO'  # TODO
                )
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read('cfg/config.ini')

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
    network_ip =        config.get('network','ip')
    network_port =      config.get('network','port')
    network_toggle =    config.get('network','wifi')
    network_key =       config.get('network','wifi_key')
    network_ssid =      config.get('network','wifi_ssid')
    repositories =      config.get('repositories','repositories').split(', ')
    ssh_key =           config.get('ssh','key')
    timezone =          config.get('timezone', 'timezone')

    config.read('cfg/config_packages.ini')

    python = config.get('packages', 'coreutils').split(', ')
    # TODO: check & add

    user = getpass.getuser()

    main()
