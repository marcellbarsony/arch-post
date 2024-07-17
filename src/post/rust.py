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
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] RUST :: ", err)
        sys.exit(1)
    else:
        logging.info(cmd)
        os.system("clear")
