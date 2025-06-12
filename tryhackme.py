import os
from sys import exit
import subprocess

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.check_sudo()
        self.vpn_conn()
        self.run_scan()

    def check_sudo(self):
        while True:
            if os.geteuid() != 0:
                print("Run as sudo !")
                break
            else:
                break

    def vpn_conn(self):
        path = os.path.expanduser("/home/psybxxst/Documents")
        os.chdir(path)
        ovpn_file = "0xPsyBxxst.ovpn"
        subprocess.run(["sudo", "openvpn", "--config", ovpn_file, "--daemon"], check=True)

    def stop_conn(self):
        os.system("sudo pkill openvpn")
        os.system("ps aux | grep openvpn")
        print("Connection Stopped!")

    def run_scan(self):
        print("Scanning. . .")
        sair = input("Exit? y/n> ").lower()
        if sair == 'y':
            self.stop_conn()
            exit()

tryhackme = TryHackMe()
