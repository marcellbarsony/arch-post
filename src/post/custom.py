import logging
import os
import urllib.request
import zipfile


def wallpapers_download(home: str) -> tuple[str, str]:
    url = "https://www.dropbox.com/scl/fo/zehsrcun1wbcb7tczyyum/AGqKkD1ILpPq3hPVDBKhCF4?rlkey=szjmedenux6fb799jn96hbgk8&st=5fbc9u7o&dl=1"
    dst = f"{home}/tmp/backgrounds"
    out = f"{dst}/wallpapers.zip"

    if not os.path.exists(dst):
        os.makedirs(dst)
        logging.info(f"makedirs: {dst}")

    print(":: [i] :: WALLPAPERS :: Downloading")

    try:
        urllib.request.urlretrieve(url, out)
    except Exception as err:
        logging.error(err)
        print(":: [-] :: WALLPAPERS :: Download ::", err)
    else:
        logging.info(f"download: {url} >> {out}")
        print(":: [+] :: WALLPAPERS :: Download")

    return out, dst

def wallpapers_extract(out: str, dst: str):
    print(":: [i] :: WALLPAPERS :: Extracting")
    try:
        with zipfile.ZipFile(out, "r") as zip_ref:
            zip_ref.extractall(dst)
            logging.info(f"extract: {zip_ref} >> {dst}")
    except Exception as err:
        logging.error(err)
        print(":: [-] :: WALLPAPERS :: Extraction ::", err)
    else:
        logging.info(f"Extracting wallpapers")
        print(":: [+] :: WALLPAPERS :: Extraction")

def wallpapers_remove(out: str):
    try:
        os.remove(out)
    except OSError as err:
        logging.error(err)
        print(":: [-] :: WALLPAPERS :: Remove zip ::", err)
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
