import logging
import subprocess
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Zsh():

    """Docstring for Shell"""

    def set(self, shell: str):
        cmd = f'chsh -s /usr/bin/{shell}'
        try:
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f'Shell: Change to /usr/bin/{shell}')
        except Exception as err:
            logger.error(f'Shell: Change to /usr/bin/{shell} {err}')
            sys.exit(1)

    def config(self, user: str):
        cfg_list = ['zshenv', 'zprofile']
        for cfg in cfg_list:
            cmd = f'sudo cp -f /home/{user}/.config/zsh/global/{cfg} /etc/zsh/{cfg}'
            try:
                subprocess.run(cmd, shell=True, check=True)
                logger.info('Zsh: Config')
            except Exception as err:
                logger.error(f'Zsh: Config {err}')
                sys.exit(1)

    def tools(self, user: str):
        repositories = {
            'marlonrichert/zsh-autocomplete.git': 'zsh-autocomplete',
            'zsh-users/zsh-completions.git':      'zsh-completions',
            'zsh-users/zsh-autosuggestions':      'zsh-autosuggestions',
            'spaceship-prompt/spaceship-prompt':  'spaceship-prompt'
            }
        for repo, dir in repositories.items():
            dst = f'/home/{user}/.local/src/{dir}'
            cmd = f'git clone --depth 1 https://github.com/{repo}.git {dst}'
            try:
                subprocess.run(cmd, shell=True, check=True)
                logger.info('Zsh: Tool')
            except Exception as err:
                logger.error(f'Zsh: Config {err}')
                sys.exit(1)
