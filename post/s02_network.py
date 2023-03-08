import subprocess


NETWORK_SSID = "ssid"
NETWORK_PASSWORD = "password"


class Network():

    """Network settings"""

    def __init__(self):
        super(Network, self).__init__()
        pass

    def wifi_activate(self):
        cmd = 'sudo nmcli radio wifi on'
        out = subprocess.run(cmd, shell=True)
        if out.returncode != 0:
            print('[-] Wifi activate')
            exit(out.returncode)

    def wifi_connect(self):
        cmd = f'nmcli device wifi connect {NETWORK_SSID} password {NETWORK_PASSWORD}'
        out = subprocess.run(cmd, shell=True)
        if out.returncode != 0:
            print('[-] Wifi connect')
            exit(out.returncode)


def main():
    n = Network()
    n.wifi_activate()
    n.wifi_connect()


if __name__ != '__main__':
    main()
