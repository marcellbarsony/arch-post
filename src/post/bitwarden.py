import logging
import subprocess
import sys


"""
Bitwarden setup
https://github.com/doy/rbw
"""

def config(email: str, timeout: str):
    cmds = [
        f"rbw config set email {email}",
        f"rbw config set lock_timeout {timeout}",
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}\n{repr(err)}")
            print(":: [-] :: RBW :: ", err)
        else:
            logging.info(cmd)
            print(":: [+] :: RBW :: Config")

def register():
    cmd = "rbw register"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except KeyboardInterrupt:
        logging.warning(f"{cmd}\nKeyboardInterrupt")
        sys.exit(1)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        register_error()
    else:
        logging.info(cmd)

def register_error():
    while True:
        user_input = input(":: [?] :: Try again? :: Y/N ").lower()
        if user_input not in ("y", "n"):
            register_error()
        else:
            if user_input == "y":
                register()
            if user_input == "n":
                sys.exit(1)

def sync():
    cmd = "rbw sync"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] :: RBW :: Sync ::", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        print(":: [+] :: RBW :: Sync")

def rbw_get(name: str, item: str) -> str:
    cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
    out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8")
    if "ERROR" in str(out.stderr):
        logging.error(f"{cmd}: {out.stderr}")
        sys.exit(1)
    logging.info(cmd)
    return out.stdout.rstrip("\n")
