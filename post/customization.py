import logging
import os
import subprocess
import urllib.request
import zipfile


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Customization():

    """Docstring for Customization"""

    @staticmethod
    def background(user: str):
        # makedir
        dir = f'/home/{user}/Downloads/Wallpapers'
        if not os.path.exists(dir):
            os.makedirs(dir)

        # download
        url = 'https://www.dropbox.com/sh/eo65dcs7buprzea/AABSnhAm1sswyiukCDW9Urp9a?dl=1'
        out = f'{dir}/wallpapers.zip'
        urllib.request.urlretrieve(url, out)

        # unzip
        with zipfile.ZipFile(out, 'r') as zip_ref:
            zip_ref.extractall(dir)

    @staticmethod
    def login_manager():
        print('[TODO] Login manager <ly>')
        # ly configuration
        # /etc/ly/config.ini
        pass

    @staticmethod
    def pacman():
        commands = [
            # archlinux-keyring: make explicitly installed
            'sudo pacman -D --asexplicit archlinux-keyring',
            # Remove orphans and their configs
            'sudo pacman -Qtdq | pacman -Rns -'
            ]
        for cmd in commands:
            out = subprocess.run(cmd, shell=True, check=True)
            if out.returncode != 0:
                print(f'[-] Pacman customization [{cmd}]')
                exit(out.returncode)

    @staticmethod
    def pipewire():
        print('[TODO] Pipewire')
        # echo "Pipewire"
        # https://roosnaflak.com/tech-and-research/transitioning-to-pipewire/
        pass

    @staticmethod
    def wayland():
        print('[TODO] Wayland')
        # Touchpad gestures
        # https://wiki.archlinux.org/title/Libinput

        # Desktop
        #/usr/qtile.desktop

        # Log
        #~/.local/share/qtile/qtile.log
        pass

    @staticmethod
    def spotify():
        print('[TODO] Spotify')
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

    @staticmethod
    def xdgDirs():
        print('[TODO] XDG directories')
        # https://wiki.archlinux.org/title/XDG_user_directories

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
