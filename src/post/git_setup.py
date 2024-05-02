import getpass
import logging
import subprocess
import sys
import bitwarden


"""
GitHub setup with SSH
https://docs.github.com/en/authentication/connecting-to-github-with-ssh
"""

def auth_login(git_token: str):
    cmd = "gh auth login --with-token"
    gh_token = bitwarden.rbw_get("github", git_token)
    try:
        subprocess.run(cmd, shell=True, check=True, input=gh_token.encode())
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)

def auth_status():
    cmd = "gh auth status"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {repr(err)}")
        sys.exit(1)

def pubkey(git_pubkey: str):
    cmd = f"gh ssh-key add /home/{getpass.getuser()}/.ssh/id_ed25519.pub -t {git_pubkey}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)

def known_hosts():
    cmd = "ssh-keyscan github.com >> ~/.ssh/known_hosts"
    try:
        subprocess.run(cmd, shell=True, check=True)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}: {err}")
        sys.exit(1)

def ssh_test():
    cmd = "ssh -T git@github.com"
    res = subprocess.run(cmd, shell=True)
    if res.returncode in [0, 1]:
        logging.info(cmd)
    else:
        logging.error(f"{cmd}: Return: {res}")
        sys.exit(res.returncode)

def config(git_user: str, git_mail: str):
    gh_mail = bitwarden.rbw_get("github", git_mail)
    gh_user = bitwarden.rbw_get("github", git_user)
    cmds = [
        f"git config --global user.name '{gh_user}'",
        f"git config --global user.email '{gh_mail}'",
        "git config --global init.defaultBranch main"
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
            logging.info(cmd)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}: {err}")
            sys.exit(1)
