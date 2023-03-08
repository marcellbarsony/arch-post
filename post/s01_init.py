import subprocess


TIMEZONE = 'Europe/Amsterdam'
DEPENDENCIES = ['rbw']


class Initialize():

    """Initialize Arch base installer"""

    def __init__(self):
        super(Initialize, self).__init__()
        pass

    def timezone(self):
        cmd = f'sudo timedatectl set-timezone {TIMEZONE}'
        try:
            subprocess.run(cmd, shell=True)
        except Exception as err:
            print('[-] Timecatectl')
            print(err)
            exit(1)
        else:
            print('[+] Timedatectl')

    def dependencies(self):
        for dependency in DEPENDENCIES:
            cmd = f'sudo pacman -S {dependency} --noconfirm'
            try:
                subprocess.run(cmd, shell=True)
            except Exception as err:
                print('[-] Dependencies')
                print(err)
                exit(1)
            else:
                print('[+] Dependencies')


def main():
    i = Initialize()
    i.timezone()
    i.dependencies()


if __name__ != '__main__':
    main()
