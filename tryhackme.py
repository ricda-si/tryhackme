import os
import subprocess
import sys
import const

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.check_sudo()
        self.connected = False
        self.vpn_conn()


    def check_sudo(self):
        while True:
            if os.geteuid() != 0:
                print("Run as sudo !")
            else:
                break

    def vpn_conn(self):
        if not self.connected:
            subprocess.run("ovpn_conn.sh", check=True)
            self.connected = True




tryhackme = TryHackMe()
