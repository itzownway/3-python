# main.py

from model.wifi_manager import WifiManager
import getpass


def main():
    wifi = WifiManager()

    networks = wifi.scanAvailableWifiNetwork()

    if not networks:
        print("No WiFi networks found")
        return

    print("\nAvailable Networks:")
    for i, net in enumerate(networks):
        print(f"{i+1}. {net}")

    choice = int(input("\nSelect WiFi: "))
    selected = wifi.selectParticluarWifi(networks, choice)

    if not selected:
        print("Invalid selection")
        return

    password = getpass.getpass("Enter Password: ")
    print("Entered Password:", password)

    success, error = wifi.connectByUserNameAndPassword(selected, password)

    if success:
        print("✅ Connected successfully!")
    else:
        print("❌ Failed:", error)


if __name__ == "__main__":
    main()