import logging
import os
import subprocess
import sys


"""
Rust default toolchain install
https://rustup.rs/
"""

def toolchain():
    cmd = "rustup default stable"
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL)
        print(":: [+] RUST :: ", cmd)
        logging.info(cmd)
    except subprocess.CalledProcessError as err:
        print(":: [-] INIT :: ", err)
        logging.error(f"{cmd}\n{repr(err)}")
        sys.exit(1)
    os.system("clear")
