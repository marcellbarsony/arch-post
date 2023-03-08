import subprocess
import sys


class Services():

    """Docstring for Services"""

    @staticmethod
    def enable():
        services = [
            'spotifyd',
            # 'ly',
            ]
        for service in services:
            cmd = f'sudo systemctl enable {service}.service'
            try:
                subprocess.run(cmd, shell=True)
                print('[+] SYSTEMCTL enable')
            except Exception as err:
                print('[-] SYSTEMCTL enable', err)
                sys.exit(1)
