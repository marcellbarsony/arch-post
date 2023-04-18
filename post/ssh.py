import logging
import subprocess
import sys
from .bitwarden import Bitwarden


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OpenSSH():

    """OpenSSH setup"""

    def __init__(self, user):
        self.user = user

    def keygen(self, ssh_key: str, gh_mail: str):
        gh_mail = Bitwarden().rbwGet('github', gh_mail)
        dir = f'/home/{self.user}/.ssh/id_ed25519'
        cmd = f'ssh-keygen -q -t ed25519 -N {ssh_key} -C {gh_mail} -f {dir}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info('Keygen')
        except Exception as err:
            logger.error('Keygen', err)
            sys.exit(1)

    #@staticmethod
    #def addKey():
    #    res = subprocess.run(['ssh-add', '-q', '~/.ssh/id_ed25510'])
