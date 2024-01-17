import subprocess
import sys


class Rust():

    """
    Rust default toolchain install
    https://rustup.rs/
    """

    @staticmethod
    def toolchain():

        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] Rust toolchain install")
        except subprocess.CalledProcessError as err:
            print("[-] Rust toolchain install", err)
            sys.exit(1)
