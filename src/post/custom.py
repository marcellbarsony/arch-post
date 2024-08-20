import logging
import os
import urllib.request
import zipfile


def wallpapers(home: str):
    dst = f"{home}/tmp/backgrounds"
    if not os.path.exists(dst):
        os.makedirs(dst)
        logging.info(f"makedirs: {dst}")

    print(":: [i] :: WALLPAPERS :: Download")
    url = "https://www.dropbox.com/scl/fo/5loqjisrohzslojb5ibmw/h?rlkey=onmox6lkop8uf9wzd314pbj66&dl=1"
    out = f"{dst}/wallpapers.zip"
    try:
        urllib.request.urlretrieve(url, out)
    except Exception as err:
        logging.error(err)
        print(":: [-] :: WALLPAPERS :: Download :: ", err)
    else:
        logging.info(f"download: {url} >> {out}")
        print(":: [+] :: WALLPAPERS :: Download")

    print(":: [i] :: WALLPAPERS :: Extract")
    with zipfile.ZipFile(out, "r") as zip_ref:
        zip_ref.extractall(dst)
        logging.info(f"extract: {zip_ref} >> {dst}")

    try:
        os.remove(out)
    except OSError as err:
        logging.error(err)
        print(":: [-] :: WALLPAPERS :: Remove zip :: ", err)
    else:
        logging.info(f"remove zip: {out}")
        print(":: [+] :: WALLPAPERS :: Remove zip")
        os.system("clear")

def spotify():
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
