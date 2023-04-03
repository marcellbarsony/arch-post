#!/usr/bin/env python3
"""
Author : FName SName <mail@domain.com>
Date   : 2023-03
"""


import argparse
import configparser
import getpass
from post import Initialize
from post import WiFi
from post import Network
from post import AurHelper
from post import Bitwarden
from post import SecureShell
from post import GitSetup
from post import Git
from post import Dotfiles


class Main():

    """Arch post-installation setup"""

    @staticmethod
    def Initialize():
        # Pacman().dependencies()

        init = Initialize()
        dmidata = init.dmi_data()
        init.timezone(timezone)
        init.sys_clock()

        while True:
            if dmidata != 'virtualbox' and 'vmware':
                WiFi().toggle(network_toggle)
                WiFi().connect(network_ssid, network_key)
            if Network().check(network_ip, network_port):
                break

    @staticmethod
    def Aur():
        pikaur = AurHelper(user, aur_helper)
        pikaur.makedir()
        pikaur.clone()
        pikaur.makepkg()

    @staticmethod
    def PasswordManager():
        rbw = Bitwarden()
        rbw.install(aur_helper)
        while True:
            status = rbw.register(bw_mail, bw_url, bw_lock)
            if status == True:
                break

    @staticmethod
    def SSH():
        ssh = SecureShell()
        ssh.kill()
        ssh.start()
        ssh.keygen(user, ssh_key, gh_mail)
        ssh.add(user)

    @staticmethod
    def Git():
        github = GitSetup()
        github.auth_login(gh_token)
        github.auth_status()
        github.add_pubkey(user, gh_pubkey)
        github.test()
        github.known_hosts()

        git = Git(user, gh_user)
        for repo in repositories:
            dir = f'.local/git/{repo}'
            git.repo_clone(repo, dir)
            git.repo_chdir(dir)
            git.repo_cfg(repo)

        repo = 'dotfiles'
        dir = '.config'
        dots = Dotfiles(user)
        dots.move()
        git.repo_clone(repo, dir)
        git.repo_chdir(dir)
        git.repo_cfg(repo)
        dots.move_back()

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
        Shell().change(shell)
        Shell().config(user)
        Shell().tools(user)

    @staticmethod
    def Services():
        Services().enable()

    @staticmethod
    def Customization():
        Customization().background(user)
        Customization().fonts()
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
    #Main.PasswordManager()
    #Main.SSH()
    #Main.GitSetup()
    #Main.Installation()
    #Main.Shell()
    #Main.Services()
    #Main.Customization()
    #Main.Languages()
