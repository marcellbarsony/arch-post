import getpass
import logging
import subprocess
import sys


"""
GitHub setup with SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh
"""

def auth_login(gh_token: str):
    cmd = "gh auth login --with-token"
    try:
        subprocess.run(cmd, shell=True, check=True, input=gh_token.encode())
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{err}")
        sys.exit(1)
    else:
        logging.info(cmd)

def auth_status():
    cmd = "gh auth status"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        sys.exit(1)
    else:
        logging.info(cmd)

def pubkey(git_pubkey: str):
    cmd = f"gh ssh-key add /home/{getpass.getuser()}/.ssh/id_ed25519.pub -t {git_pubkey}"
    try:
        subprocess.run(cmd, shell=True, check=True)
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
    cmd = "ssh -T git@github.com"
    res = subprocess.run(cmd, shell=True)
    if res.returncode in [0, 1]:
        logging.info(cmd)
    else:
        logging.error(f"{cmd}\nReturn: {res}")
        sys.exit(res.returncode)

def config(gh_user: str, gh_mail: str):
    cmds = [
        f"git config --global user.name '{gh_user}'",
        f"git config --global user.email '{gh_mail}'",
        "git config --global init.defaultBranch main"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)
        else:
            logging.info(cmd)
