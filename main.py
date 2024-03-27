#!/usr/bin/env python3
"""
Author : Marcell Barsony
Date   : January 2023
"""


import argparse
import configparser
import getpass
import os
import sys
import logging

from src.post import AURhelper
from src.post import Bitwarden
from src.post import Customization
from src.post import DisplayManager
from src.post import Dotfiles
from src.post import GitSetup
from src.post import Git
# from src.post import JavaScript # TODO
# from src.post import Network # TODO
from src.post import Pacman
from src.post import Pipewire
from src.post import Progs
from src.post import Python
from src.post import Rust
from src.post import SSHagent
from src.post import TimeDate
# from src.post import WiFi  # TODO
from src.post import XDGStandard
from src.post import Shell


class Main():

    def __init__(self):
        self.cwd = os.getcwd()
        self.user = getpass.getuser()

    def run(self):
        self.systime()
        self.network()
        self.pacman()
        self.rust()
        self.aur()
        self.password_manager()
        self.ssh()
        self.git()
        self.shell()
        self.audio()
        self.display()
        self.xdg()
        self.customize()
        self.languages()

    @staticmethod
    def systime():
        # TODO: time setup check
        i = TimeDate()
        i.ntp()
        i.timezone(timezone)

    @staticmethod
    def network():
        # TODO: network setup
        pass

    @staticmethod
    def pacman():
        p = Pacman()
        p.keyring()

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
        r = Bitwarden()
        r.install(aurhelper)
        r.register(bw_mail, bw_lock)

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

        p = Progs(self.user, gh_user)
        p.clone()
        p.cfg()

        for repo in repositories:
            r = Git(self.user, gh_user, repo)
            r.repo_clone()
            r.repo_chdir()
            r.repo_cfg()

    def shell(self):
        s = Shell(self.user)
        s.change()
        s.config()
        s.tools()

    @staticmethod
    def audio():
        p = Pipewire()
        p.service()

    @staticmethod
    def display():
        l = DisplayManager(displayman)
        l.install(aurhelper)
        l.service()

    def xdg(self):
        x = XDGStandard(self.user)
        x.mkdir_tmp()
        x.remove_dirs()
        x.remove_files()
        x.move_rust()
        x.remove_self()

    def customize(self):
        c = Customization()
        c.background(self.user)
        c.spotify()
        c.steam()

    def languages(self):
        p = Python()
        dirs = {
            f".local/git/arch",
            f".local/git/arch-post",
            f".local/git/arch-tools"
            }
        for dir in dirs:
            p.chdir(dir)
            p.venv_init()
            p.venv_activate()
            p.pip_upgrade()
            p.pip_install()
            p.venv_deactivate()

        # TODO: test and refactor
        # TODO: add .local/bin
        # dir = f"/home/{self.user}/.local/share/python/debugpy"
        # p.chdir(dir)
        # p.venv_init()
        # p.venv_activate()
        # p.pip_upgrade()
        # p.pip_install_debugpy()
        # p.venv_deactivate()

        # j = JavaScript()
        # j.npm_install()



if __name__ == "__main__":

    """ Check permissions """
    if os.getuid == 0:
        print("[-] Executed as root: UID=0")
        sys.exit(1)

    """ Initialize Argparse """
    parser = argparse.ArgumentParser(
        prog="python3 arch-post.py",
        description="Arch post-install setup",
        epilog="TODO"
    )
    args = parser.parse_args()

    """ Initialize Logging """
    logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w",
                        format="%(levelname)-7s :: %(module)s - %(funcName)s - %(lineno)d :: %(message)s")

    """ Initialize Global variables """
    config = configparser.ConfigParser()
    config.read("config.ini")

    aurhelper = config.get("aur", "helper")
    bw_mail = config.get("bitwarden", "mail")
    bw_lock = config.get("bitwarden", "lock")
    git_mail = config.get("bitwarden_data", "github_mail")
    git_user = config.get("bitwarden_data", "github_user")
    git_token = config.get("bitwarden_data", "github_token")
    spotify_client_id = config.get("bitwarden_data", "spotify_client_id")
    spotify_secret = config.get("bitwarden_data", "spotify_client_secret")
    spotify_device_id = config.get("bitwarden_data", "spotify_device_id")
    spotify_mail = config.get("bitwarden_data", "spotify_mail")
    spotify_user = config.get("bitwarden_data", "spotify_user")
    displayman = config.get("displayman", "displayman")
    git_pubkey = config.get("github",  "pubkey")
    network_ip = config.get("network", "ip")
    network_port = config.get("network", "port")
    network_toggle = config.get("network", "wifi")
    network_key = config.get("network", "wifi_key")
    network_ssid = config.get("network", "wifi_ssid")
    repositories = config.get("repositories", "repositories").split(", ")
    ssh_key = config.get("ssh", "key")
    timezone = config.get("timezone", "timezone")

    """ Run script """
    m = Main()
    m.run()
