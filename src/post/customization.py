import logging
import os
import urllib.request
import zipfile


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Customization():

    """Docstring for Customization"""

    @staticmethod
    def background(user: str):
        dir = f'/home/{user}/Pictures'

        os.mkdir(dir)

        url = 'https://www.dropbox.com/sh/eo65dcs7buprzea/AABSnhAm1sswyiukCDW9Urp9a?dl=1'
        out = f'{dir}/wallpapers.zip'
        urllib.request.urlretrieve(url, out)

        with zipfile.ZipFile(out, 'r') as zip_ref:
            zip_ref.extractall(dir)

        os.remove(out)

    @staticmethod
    def pc_speaker():
        """https://wiki.archlinux.org/title/PC_speaker#Globally"""
        file = "/etc/modprobe.d/nobeep.conf"
        content = "blacklist pcspkr\nblacklist snd_pcsp"
        try:
            with open(file, "w") as f:
                f.write(content)
            logger.info('Disable PC speaker')
        except IOError as err:
            logger.error(f'Disable PC speaker {err}')
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
