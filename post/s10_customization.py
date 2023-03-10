import subprocess


class Customization():

    """Docstring for Customization"""

    @staticmethod
    def background(user):
        # mkdir '/home/{user}/Downloads'
        url = 'https://www.dropbox.com/sh/eo65dcs7buprzea/AABSnhAm1sswyiukCDW9Urp9a?dl=1'
        cmd = f'curl -L -o /home/{user}/Downloads/wallpapers.zip "{url}"'
        cmd = f'unzip /home/{user}/Downloads/wallpapers.zip -d /home/{user}/Pictures/Wallpapers/ -x /'

    def fonts(self):
        # Japanese
        # sudo sed -i '/#ja_JP.UTF-8 UTF-8/s/^#//g' /etc/locale.gen
        # sudo echo "LANG=ja_JP.UTF-8" >>/etc/locale.conf
        linenr= 69 # TODO
        with open('/etc/locale.gen', 'r') as file:
            lines = file.readlines()
        lines[linenr] = "ja_JP.UTF-8 UTF-8\n"
        with open('/etc/locale.gen', 'w') as file:
            file.writelines(lines)
            print('[+] /etc/locale.gen')

        locale = "LANG=ja_JP.UTF-8"
        conf = '/etc/locale.conf'
        with open(conf, 'w') as file:
            file.write(locale)
            print('[+] /etc/locale.conf')
        pass

    def ly_setup(self):
        # Configuration
        # /etc/ly/config.ini
        pass

    def pacman(self):
        commands = [
            # archlinux-keyring: make explicitly installed
            'sudo pacman -D --asexplicit archlinux-keyring',
            # Remove orphans and their configs
            'sudo pacman -Qtdq | pacman -Rns -'
            ]
        for cmd in commands:
            out = subprocess.run(cmd, shell=True)
            if out.returncode != 0:
                print(f'[-] Pacman customization [{cmd}]')
                exit(out.returncode)

    def pipewire(self):
        # echo "Pipewire"
        # https://roosnaflak.com/tech-and-research/transitioning-to-pipewire/
        pass

    def qtile_wayland(self):
        # Touchpad gestures
        # https://wiki.archlinux.org/title/Libinput

        # Desktop
        #/usr/qtile.desktop

        # Log
        #~/.local/share/qtile/qtile.log
        pass

    def spotify(self):
        # killall spotifyd

        # # Spotifyd.conf
        # sed -i "s/usr/${spotify_username}/g" ${HOME}/.config/spotifyd/spotifyd.conf
        # sed -i "s/pswd/${spotify_password}/g" ${HOME}/.config/spotifyd/spotifyd.conf
        # sed -i "s#cachedir#/home/${USER}/.cache/spotifyd/#g" ${HOME}/.config/spotifyd/spotifyd.conf

        # # Client.yml
        # sed -i "s/clientid/${spotify_client_id}/g" ${HOME}/.config/spotify-tui/client.yml
        # sed -i "s/clientsecret/${spotify_client_secret}/g" ${HOME}/.config/spotify-tui/client.yml
        # sed -i "s/deviceid/${spotify_device_id}/g" ${HOME}/.config/spotify-tui/client.yml
        pass

    def xdg_dirs(self):
        # # Generate XDG directories
        # LC_ALL=C.UTF-8 xdg-user-dirs-update --force
        # mkdir ${HOME}/.local/state
        # mkdir ${HOME}/.local/share/{bash,cargo,Trash,vim}

        # # Move files
        # mv ${HOME}/.cargo ${HOME}/.local/share/cargo
        # mv ${HOME}/.bash* ${HOME}/.local/share/bash
        # mv ${HOME}/.viminfo* ${HOME}/.local/share/vim

        # # Delete files
        # rm -rf ${HOME}/{Desktop,Music,Public,Templates,Videos}
        # rm -rf ${HOME}/arch
        pass
