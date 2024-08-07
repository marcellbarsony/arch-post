import logging
import os
import urllib.request
import zipfile


def background(home: str):
    dir = f"{home}/tmp/backgrounds"
    if not os.path.exists(dir):
        os.makedirs(dir)
        logging.info(f"makedirs: {dir}")

    print(":: [i] :: WALLPAPERS :: Download")
    url = "https://www.dropbox.com/scl/fo/5loqjisrohzslojb5ibmw/h?rlkey=onmox6lkop8uf9wzd314pbj66&dl=1"
    out = f"{dir}/wallpapers.zip"
    try:
        urllib.request.urlretrieve(url, out)
    except Exception as err:
        print(":: [-] :: WALLPAPERS :: Downlaod :: ", err)
        logging.error(err)
    else:
        logging.info(f"download: {url} >> {out}")

    print(":: [i] :: WALLPAPERS :: Extract")
    with zipfile.ZipFile(out, "r") as zip_ref:
        zip_ref.extractall(dir)
        logging.info(f"extract: {zip_ref} >> {dir}")

    os.remove(out)
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
