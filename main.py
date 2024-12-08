#!/usr/bin/env python3


# Imports {{{
import argparse
import configparser
import getpass
import os
import sys
import logging

from src.post import aur
from src.post import bitwarden
from src.post import custom
from src.post import git_setup
from src.post import git_repos
from src.post import pacman
from src.post import pipewire
from src.post import python
from src.post import rust
from src.post import shell
from src.post import ssh
from src.post import systime
from src.post import xdg
# }}}

# System Time {{{
def set_system_time():
    systime.ntp()
    systime.time_zone(timezone)
# }}}

# Pacman {{{
def set_pacman():
    pacman.explicit_keyring()
    pacman.update()
# }}}

# Rust {{{
def set_rust():
    rust.toolchain()
# }}}

# AUR {{{
def set_aur():
    aur.mkdir(aur_dir)
    aur.clone(aur_dir, aur_helper)
    aur.mkpkg(aur_dir, cwd)
    aur.remove(aur_dir)
# }}}

# Password Manager {{{
def set_bitwarden():
    bitwarden.config(bw_mail, bw_lock)
    bitwarden.register()
    bitwarden.sync()
# }}}

# SSH {{{
def set_ssh():
    gh_mail = bitwarden.rbw_get("github", git_mail)

    ssh.config(home, ssh_dir)
    ssh.service_set(home, ssh_dir)
    ssh.service_start()
    ssh.key_gen(home, ssh_key, gh_mail)
    ssh.key_add()
# }}}

# GIT {{{
def set_git():
    gh_token = bitwarden.rbw_get("github", git_token)
    gh_mail = bitwarden.rbw_get("github", git_mail)
    gh_user = bitwarden.rbw_get("github", git_user)

    git_setup.auth_login(gh_token)
    git_setup.auth_status()
    git_setup.pubkey_add(git_pubkey)
    git_setup.known_hosts()
    git_setup.ssh_test()
    git_setup.config(gh_user, gh_mail)

def set_git_repos():
    gh_user = bitwarden.rbw_get("github", git_user)

    for repo in repositories:
        if repo == "dotfiles":
            dst = f"{home}/.config"
            git_repos.remove(dst)
        else:
            dst = f"{home}/.local/git/{repo}"
        git_repos.repo_clone(gh_user, repo, dst)
        git_repos.repo_chdir(dst)
        git_repos.repo_cfg(gh_user, repo)
# }}}

# Shell {{{
def set_shell():
    shell.change()
    shell.config()
    shell.tools()
# }}}

# Audio {{{
def set_pipewire():
    pipewire.service()
# }}}

# Customize {{{
def customize():
    custom.wallpapers(home)
    custom.spotify()
# }}}

# Python {{{
def set_python():
    dirs = {
        ".local/bin",
        ".local/git/arch",
        ".local/git/arch-post",
        ".local/git/arch-tools",
    }
    for dir in dirs:
        python.chdir(home, dir)
        python.venv_init()
        python.venv_activate()
        # python.pip_upgrade()
        # python.pip_install()
        python.venv_deactivate()

    dir = ".local/share/python"
    python.chdir(home, dir)
    python.venv_init_debugpy()
    python.venv_activate()
    python.pip_install_debugpy()
    python.venv_deactivate()
# }}}

# XDG {{{
def set_xdg():
    xdg.move_rust(home)
    xdg.remove_dirs(home)
    xdg.remove_files(home)
    xdg.remove_self(home)
    xdg.open()
# }}}


if __name__ == "__main__":

    # Check {{{
    if os.getuid == 0:
        print(":: [-] :: Executed as root :: UID=0")
        sys.exit(1)
    # }}}

    # Argparse {{{
    parser = argparse.ArgumentParser(
        prog="python3 arch-post.py",
        description="Arch post-install setup",
        epilog="TODO"
    )
    args = parser.parse_args()
    # }}}

    # Logging {{{
    logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w",
        format="%(levelname)-7s :: %(module)s - %(funcName)s - %(lineno)d :: %(message)s")
    # }}}

    # Config {{{
    config = configparser.ConfigParser()
    config.read("config.ini")

    # AUR
    aur_helper        = config.get("aur", "helper")

    # Bitwarden
    bw_mail           = config.get("bitwarden", "mail")
    bw_lock           = config.get("bitwarden", "lock")
    git_mail          = config.get("bitwarden_data", "github_mail")
    git_user          = config.get("bitwarden_data", "github_user")
    git_token         = config.get("bitwarden_data", "github_token")
    spotify_client_id = config.get("bitwarden_data", "spotify_client_id")
    spotify_secret    = config.get("bitwarden_data", "spotify_client_secret")
    spotify_device_id = config.get("bitwarden_data", "spotify_device_id")
    spotify_mail      = config.get("bitwarden_data", "spotify_mail")
    spotify_user      = config.get("bitwarden_data", "spotify_user")

    # GitHub
    git_pubkey        = config.get("github",  "pubkey")

    # Network
    network_ip        = config.get("network", "ip")
    network_port      = config.get("network", "port")
    network_toggle    = config.get("network", "wifi")
    network_key       = config.get("network", "wifi_key")
    network_ssid      = config.get("network", "wifi_ssid")

    # Repositories
    repositories      = config.get("repositories", "repositories").split(", ")

    # SSH
    ssh_key           = config.get("ssh", "key")

    # Timezone
    timezone          = config.get("timezone", "zone")

    for section in config.sections():
        for key, value in config.items(section):
            if not key.strip():
                print(":: [-] :: ConfigParser :: Empty key")
                raise ValueError(f"Empty key found :: [{section}]")
            if not value.strip():
                print(":: [-] :: ConfigParser :: Empty value")
                raise ValueError(f"Empty value '{key}' in section [{section}]")
    # }}}

    # Global variables {{{
    cwd = os.getcwd()
    user = getpass.getuser()

    home = f"/home/{user}"
    aur_dir = f"/home/{user}/.local/src/{aur_helper}/"
    ssh_dir = f"{cwd}/src/ssh"
    # }}}

    # Run {{{
    set_system_time()
    set_pacman()
    set_rust()
    set_aur()
    set_bitwarden()
    set_ssh()
    set_git()
    set_git_repos()
    set_shell()
    # set_pipewire()
    customize()
    set_python()
    set_xdg()
    # }}}
