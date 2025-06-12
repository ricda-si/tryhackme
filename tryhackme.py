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
        os.system("cd ~/Documents/")
        os.system("sudo openvpn 0xPsyBxxst.ovpn")
        '''
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "ovpn_conn.sh")
        os.chmod(script_path, 0o755)
        os.system("./ovpn_conn.sh")
        #subprocess.run(["bash", script_path], check=True)
        self.connected = True
        '''

tryhackme = TryHackMe()
