# model/wifi_manager.py

import subprocess


class WifiManager:

    def scanAvailableWifiNetwork(self):
        result = subprocess.run(
            ["nmcli", "-t", "-f", "SSID", "dev", "wifi"],
            capture_output=True,
            text=True
        )

        networks = list(set(result.stdout.split("\n")))
        return [n for n in networks if n]

    def selectParticluarWifi(self, networks, index):
        if 1 <= index <= len(networks):
            return networks[index - 1]
        return None

    def connectByUserNameAndPassword(self, userName, passWord):
        result = subprocess.run(
            ["nmcli", "dev", "wifi", "connect", userName, "password", passWord],
            capture_output=True,
            text=True
        )

        return result.returncode == 0, result.stderr