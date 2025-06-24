import logging
import os
import urllib.request
import zipfile


def downloads(home: str) -> tuple[str, str]:
    url = "https://www.dropbox.com/scl/fo/zehsrcun1wbcb7tczyyum/AGqKkD1ILpPq3hPVDBKhCF4?rlkey=szjmedenux6fb799jn96hbgk8&st=5fbc9u7o&dl=1"
    dst = f"{home}/tmp/backgrounds"
    out = f"{dst}/wallpapers.zip"

    if not os.path.exists(dst):
        os.makedirs(dst)
        logging.info("makedirs: %s", dst)

    try:
        logging.info("downloading")
        urllib.request.urlretrieve(url, out)
    except Exception as err:
        logging.error(err)
    else:
        logging.info(out)

    return out, dst

def extract(out: str, dst: str):
    try:
        with zipfile.ZipFile(out, "r") as zip_ref:
            logging.info("extracting")
            zip_ref.extractall(dst)
    except Exception as err:
        logging.error(err)
        return
    else:
        logging.info(dst)

def cleanup(out: str):
    try:
        os.remove(out)
    except OSError as err:
        logging.error(err)
        return
    else:
        logging.info(out)

