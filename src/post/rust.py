import subprocess


class Rust():

    """Docstring for Rust setup"""

    @staticmethod
    def toolchain():

        """
        Rust default toolchain install
        https://rustup.rs/
        """

        cmd = "rustup default stable"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print('[+] Toolchain install')
        except subprocess.CalledProcessError as err:
            print('[-] Toolchain install', err)
