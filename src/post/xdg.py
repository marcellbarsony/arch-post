import logging
import os
import shutil
import subprocess


"""Docstring for Cross Desktop Group (XDG)"""

def move_rust(home: str):
    cargo_conf = f"{home}/.cargo"
    cargo_home = f"{home}/.local/share/cargo"
    if os.path.exists(cargo_conf):
        shutil.move(cargo_conf, cargo_home)
        logging.info(f"{cargo_conf} >> {cargo_home}")

    rustup_conf = f"{home}/.rustup"
    rustup_home = f"{home}/.local/share/rustup"
    if os.path.exists(rustup_home):
        shutil.move(rustup_conf, rustup_home)
        logging.info(f"{rustup_conf} >> {rustup_home}")

def remove_dirs(home: str):
    dirs = [
        "Desktop",
        "Documents",
        "Music",
        "Public",
        "Templates",
        "Videos"
    ]
    for dir in dirs:
        path = os.path.join(home, dir)
        if os.path.exists(path):
            try:
                os.rmdir(path)
            except OSError as err:
                logging.error(f"{path}\n{err}")
            else:
                logging.info(path)

def remove_files(home: str):
    files = [
        ".bashrc",
        ".bash_history",
        ".bash_logout",
        ".bash_profile",
        ".gitconfig"
    ]
    for file in files:
        path = os.path.join(home, file)
        if os.path.exists(path):
            os.remove(path)
            logging.info(path)

def remove_self(home: str):
    path = f"{home}/arch-post"
    if os.path.exists(path):
        shutil.rmtree(path)
        logging.info(path)

def open():
    cmd = "xdg-settings set default-web-browser firefox.desktop"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        logging.error(f"{cmd}\n{repr(err)}")
        print(":: [-] :: XDG ::", err)
    else:
        logging.info(cmd)
        print(":: [+] :: XDG :: Open")
