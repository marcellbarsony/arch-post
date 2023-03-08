import subprocess
import sys

class Shell():

    """Docstring for Shell"""

    @staticmethod
    def change(shell):
        cmd = f'chsh -s /usr/bin/{shell}'
        try:
            subprocess.run(cmd, shell=True)
            print('[+] SHELL change')
        except Exception as err:
            print('[-] SHELL change', err)
            sys.exit(1)

    @staticmethod
    def config(user):
        cfg_list = ['zshenv', 'zprofile']
        for cfg in cfg_list:
            cmd = f'sudo cp -f /home/{user}/.config/zsh/global/{cfg} /etc/zsh/{cfg}'
            try:
                subprocess.run(cmd, shell=True)
                print('[+] ZSH config')
            except Exception as err:
                print('[-] ZSH config', err)
                sys.exit(1)

    @staticmethod
    def tools(user):
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
                subprocess.run(cmd, shell=True)
                print('[+] ZSH tools')
            except Exception as err:
                print('[-] ZSH tools', err)
                sys.exit(1)
