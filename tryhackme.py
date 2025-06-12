import os
from sys import exit
import subprocess
import netifaces # type: ignore
import time
import utils

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.status = ["CONNECTED 🟢", "DISCONNECTED 🔴"]
        self.connection = self.status[1]
        self.user = "user"
        self.check_sudo()
        self.vpn_conn()
        self.lhost = self.wait_for_ip()

    def check_sudo(self):
        while True:
            if os.geteuid() != 0: # type: ignore
                return False
            self.user = "sudo"
            return True

    def vpn_conn(self):
        path = os.path.expanduser("/home/psybxxst/Documents")
        os.chdir(path)
        ovpn_file = "0xPsyBxxst.ovpn"
        subprocess.run(["sudo", "openvpn", "--config", ovpn_file, "--daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.connection = self.status[0]

    def stop_conn(self):
        os.system("sudo pkill openvpn")
        utils.print_info("Connection closed.")
        self.connection = self.status[1]

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

    def wait_for_iface(self, iface="tun0", timeout=30, interval=1):
        for _ in range(int(timeout / interval)):
            if iface in netifaces.interfaces():
                return True
            time.sleep(interval)
        return False

    def wait_for_ip(self, timeout=30, interval=1):
        if not self.wait_for_iface():
            return None

        for _ in range(int(timeout / interval)):
            ip = self.get_ip()
            if ip:
                return ip
            time.sleep(interval)
        utils.print_err("No IP.")
        return None
