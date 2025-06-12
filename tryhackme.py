import os
from sys import exit
import subprocess
import netifaces
import time

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.check_sudo()
        self.vpn_conn()
        self.connected = False
        self.lhost = self.wait_for_ip()
        self.print_status()

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
        subprocess.run(["sudo", "openvpn", "--config", ovpn_file, "--daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.connected = True

    def stop_conn(self):
        os.system("sudo pkill openvpn")
        print("Connection Stopped!")

    def exit_script(self):
        self.stop_conn()
        exit()

    def get_ip(self):
        interface = "tun0"
        try:
            iface = netifaces.ifaddresses(interface)
            return iface[netifaces.AF_INET][0]['addr']
        except (KeyError, IndexError):
            return None

    def wait_for_ip(self, timeout=30, interval=1):
        for _ in range(int(timeout / interval)):
            ip = self.get_ip()
            if ip:
                return ip
            time.sleep(interval)
        print("Error: No IP")
        return None

    def print_status(self):
        print(f'''
              Connected: {self.connected}
              IP: {self.lhost}
              ''')

tryhackme = TryHackMe()
