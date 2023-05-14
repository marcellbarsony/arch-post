import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Audio():

    """Docstring for Customization"""

    @staticmethod
    def pipewire():
        print('[TODO] Pipewire')
        # # Install
        # services = ['pipewire.socket', 'pipewire-pulse.socket', 'wireplumber.service'] #spotifyd
        # for service in services:
        #     cmd = f'sudo systemctl enable {service}'
        #     try:
        #         subprocess.run(cmd, shell=True, check=True)
        #         logger.info(f'Service: Enable <{service}>')
        #     except Exception as err:
        #         logger.error(f'Service: Enable <{service}> {err}')
        #         sys.exit(1)
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
