import subprocess
import sys


class Bitwarden():

    """Bitwarden setup with rbw"""

    @staticmethod
    def rbw_register(mail, url, timeout):
        commands = [f'rbw config set email {mail}',
                    f'rbw config set base_url {url}',
                    f'rbw config set lock_timeout {timeout}',
                    'rbw register',
                    'rbw sync']
        for cmd in commands:
            try:
                subprocess.run(cmd, shell=True, check=True)
                print('[+] BITWARDEN register')
                return True
            except subprocess.CalledProcessError as err:
                print('[-]', repr(err))
                return False

    @staticmethod
    def rbw_get(name, item):
        cmd = f'rbw get {name} --full | grep "{item}" | cut -d " " -f 2'
        out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
        if "ERROR" in str(out.stderr):
            print(f'[-] BITWARDEN data <{name} {item}>')
            sys.exit(1)
        print(f'[+] BITWARDEN data <{name}>')
        return out.stdout
