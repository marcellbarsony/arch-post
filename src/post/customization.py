import logging
import os
import sys
import urllib.request
import zipfile


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Customization():

    """Docstring for Customization"""

    @staticmethod
    def background(user: str):
        dir = f'/home/{user}/Pictures'

        # makedir
        os.mkdir(dir)

        # download
        url = 'https://www.dropbox.com/sh/eo65dcs7buprzea/AABSnhAm1sswyiukCDW9Urp9a?dl=1'
        out = f'{dir}/wallpapers.zip'
        urllib.request.urlretrieve(url, out)

        # unzip
        with zipfile.ZipFile(out, 'r') as zip_ref:
            zip_ref.extractall(dir)

        # delete
        os.remove(out)

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
