import logging
import os
import subprocess
import sys


"""
Zsh setup
https://wiki.archlinux.org/title/Zsh
"""

def change():
    os.system("clear")
    cmd = ["chsh", "-s", "/usr/bin/zsh"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, err)
        sys.exit(1)
    else:
        logging.info(cmd)

def config(user: str):
    src = f"/home/{user}/.config/zsh/global/"
    dst = "/etc/zsh/"
    for file in os.listdir(src):
        src_file = os.path.join(src, file)
        dst_file = os.path.join(dst, file)
        cmds = [
            ["sudo", "cp", "-r", src_file, dst_file],
            ["sudo", "chmod", "644", dst_file]
        ]
        for cmd in cmds:
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as err:
                logging.error("%s\n%s", cmd, err)
                sys.exit(1)
            else:
                logging.info(cmd)

def tools(user: str):
    repos = {"marlonrichert/zsh-autocomplete": "zsh-autocomplete"}
    for repo, dir in repos.items():
        dst = f"/home/{user}/.local/src/{dir}"
        cmd = ["git", "clone", "--depth", "1", f"git@github.com:{repo}.git", dst]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as err:
            logging.error("%s\n%s", cmd, err)
            sys.exit(1)
        else:
            logging.info(cmd)
