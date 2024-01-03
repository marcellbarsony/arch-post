import subprocess
import sys


class JavaScript():

    """Docstring for JavaScript NPM setup"""

    @staticmethod
    def npm_install():
        """https://www.npmjs.com/package/live-server"""
        cmd = f"npm install -g live-server"
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("[+] JavaScript: NPM install live-server")
        except subprocess.CalledProcessError as err:
            print(f"[-] JavaScript: NPM install live-server, {err}")
            sys.exit(1)
