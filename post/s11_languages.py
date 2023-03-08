import subprocess
import sys


class Python():

    """Docstring for Python"""

    @staticmethod
    def venv():
        pass

    @staticmethod
    def modules(modules):
        for module in modules:
            cmd = f'pip install {module}'
            try:
                subprocess.run(cmd, shell=True)
                print('[+] PYTHON modules')
            except Exception as err:
                print('[-] PYTHON modules', err)
                sys.exit(1)


class Ruby():

    """Docstring for Ruby"""

    @staticmethod
    def install():
        cmd = 'sudo pacman -Q ruby'
        try:
            subprocess.run(cmd, shell=True)
            print('[+] RUBY install')
        except Exception as err:
            print('[-] RUBY install', err)
            sys.exit(1)

    @staticmethod
    def gems():
        # cd ${HOME}/.local/git/blog
        # gem update
        # gem install jekyll bundler
        # bundle update
        # cd ${HOME}
        pass
