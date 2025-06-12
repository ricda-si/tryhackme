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
            else:
                break

    def vpn_conn(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "ovpn_conn.sh")
        os.chmod(script_path, 0o755)
        subprocess.run([script_path], check=True)
        self.connected = True

tryhackme = TryHackMe()
