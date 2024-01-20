import logging
import sys
import subprocess


class Pipewire():

    """
    Docstring for Pipewire
    https://wiki.archlinux.org/title/Pipewire
    """

    @staticmethod
    def service():
        services = [
            "pipewire",
            "wireplumber"
        ]
        for service in services:
            cmd = f"systemctl --user enable {service}"
            try:
                subprocess.run(cmd, shell=True, check=True)
                logging.info(f"Audio: Piewire service - {cmd}")
            except subprocess.CalledProcessError as err:
                logging.error(f"Audio: Pipewire service - {cmd}: {err}")
                sys.exit(1)
