import os
import subprocess

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
                break
            else:
                break

    def vpn_conn(self):
        path = os.path.expanduser("/home/psybxxst/Documents")
        os.chdir(path)
        ovpn_file = "0xPsyBxxst.ovpn"
        subprocess.run(["sudo", "openvpn", "--config", ovpn_file, "--daemon"], check=True)

tryhackme = TryHackMe()
