import logging
import subprocess
import sys


"""
Bitwarden setup
https://github.com/doy/rbw
"""

def config(email: str, timeout: str):
    cmds = [
        ["rbw", "config", "set", "email", email],
        ["rbw", "config", "set", "lock_timeout", timeout]
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as err:
            logging.error(f"{cmd}\n{repr(err)}")
            print(":: [-] :: RBW ::", err)
        else:
            logging.info(cmd)
            print(":: [+] :: RBW :: Config")

def register():
    cmd = ["rbw", "register"]
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        logging.warning(f"{cmd}\nKeyboardInterrupt")
        sys.exit(1)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        while True:
            print(":: [?] :: Try again? :: Y/N: ", end="")
            user_input = input().strip().lower()
            if user_input == "y":
                return register()
            elif user_input == "n":
                sys.exit(1)
            else:
                continue
    else:
        logging.info(cmd)

def sync():
    cmd = ["rbw", "sync"]
    try:
        subprocess.run(cmd, check=True)
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
