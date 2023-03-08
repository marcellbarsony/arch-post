import subprocess
import sys


class Bitwarden():

    """Bitwarden setup w/rbw"""

    @staticmethod
    def rbw_register(mail, url, timeout):
        cmds = [
            f'rbw config set email {mail}',
            f'rbw config set base_url {url}',
            f'rbw config set lock_timeout {timeout}',
            'rbw register',
            'rbw sync'
            ]
        for cmd in cmds:
            try:
                subprocess.run(cmd, shell=True, check=True)
                print('[+] BITWARDEN register')
            except subprocess.CalledProcessError as err:
                print('[-]', repr(err))
                sys.exit(1)

    @staticmethod
    def rbw_get(name, item):
        cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
        try:
            out = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print('[+] BITWARDEN data')
            return out.stdout
        except subprocess.CalledProcessError as err:
            print('[-]', repr(err))
            sys.exit(1)
