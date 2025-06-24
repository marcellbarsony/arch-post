import logging
import subprocess
import sys


"""
Rust default toolchain install
https://rustup.rs/
https://wiki.archlinux.org/title/Rust
"""

def toolchain():
    cmd = ["rustup", "default", "stable"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as err:
        logging.error("%s\n%s", cmd, repr(err))
        sys.exit(1)
    else:
        logging.info(cmd)
