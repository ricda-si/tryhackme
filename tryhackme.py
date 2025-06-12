import os
from sys import exit
import subprocess
import netifaces

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.check_sudo()
        self.vpn_conn()
        self.lhost = self.get_ip()

    def check_sudo(self):
        while True:
            if os.geteuid() != 0:
                print("Run as sudo !")
                break
            else:
                break

    def vpn_conn(self):
        print("Connecting. . .")
        path = os.path.expanduser("/home/psybxxst/Documents")
        os.chdir(path)
        ovpn_file = "0xPsyBxxst.ovpn"
        subprocess.run(["sudo", "openvpn", "--config", ovpn_file, "--daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Connected!")

    def stop_conn(self):
        os.system("sudo pkill openvpn")
        print("Connection Stopped!")

    def get_ip(self):
        interface = "tun0"
        try:
            iface = netifaces.ifaddresses(interface)
            ip = iface[netifaces.AF_INET][0]['addr']
            print(f"IP: {ip}")
            return ip
        except (KeyError, IndexError):
            return None

tryhackme = TryHackMe()
