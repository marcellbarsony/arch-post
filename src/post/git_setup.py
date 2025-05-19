import logging
import subprocess
import sys


"""
GitHub setup with SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh
"""

def auth_login(gh_token: str):
    cmd = ["gh", "auth", "login", "--with-token"]
    try:
        subprocess.run(cmd, check=True, input=gh_token.encode())
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
    else:
        logging.info(cmd)

def auth_status():
    cmd = ["gh", "auth", "status"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        sys.exit(1)
    else:
        logging.info(cmd)

def pubkey_add(user: str, git_pubkey: str):
    cmd = ["gh", "ssh-key", "add", f"/home/{user}/.ssh/id_ed25519.pub", "-t", git_pubkey]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
    else:
        logging.info(cmd)

def known_hosts():
    cmd = "ssh-keyscan github.com >> ~/.ssh/known_hosts"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
    else:
        logging.info(cmd)

def ssh_test():
    cmd = ["ssh", "-T", "git@github.com"]
    res = subprocess.run(cmd)
    if res.returncode in [0, 1]:
        logging.info(cmd)
    else:
        logging.error(f"{cmd}\nReturn: {res}")
        sys.exit(res.returncode)

def config(gh_user: str, gh_mail: str):
    cmds = [
        ["git", "config", "--global", "user.name", f"'{gh_user}'"],
        ["git", "config", "--global", "user.email", f"'{gh_mail}'"],
        ["git", "config", "--global", "init.defaultBranch", "main"]
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)
        else:
            logging.info(cmd)
