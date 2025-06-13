import sys
import os
import utils
import input_check as ichk

class Scanner:
    def __init__(self):
        self.rhost = None

    def check_conn(self, status):
        utils.print_info("Checking connection. . .")
        if "DISCONNECTED" in status:
            utils.print_err("Not connected to VPN.")
            input("\nPress any key to continue...")
            return False
        return True

    def get_target(self):
        target = input("Target IP: ")
        utils.print_info(f"RHOST: {target}")
        self.rhost = target
        info.append(f"RHOST: {self.rhost}")
        input("\nPress any key to continue...")

    def ping_target(self):
        if not self.rhost:
            utils.print_err("No target.")
            input("\nPress any key to continue...")
            return None
        return True if os.system(f"ping -n 1 {self.rhost} > /dev/null 2>&1") else False

    def menu(self, info1, info2, status):
        if not self.check_conn(status):
            return

        while True:
            os.system("clear")
            utils.print_header("Scanner")
            utils.scanner_user_info(info1, info2)
            utils.scanner_show_info(info)

            print("1.  Add target")
            print("2.  Ping target")
            print("99. Exit")
            usr = ichk.scanner_user_input()
            match usr:
                case 1:
                    self.get_target()
                case 2:
                    if self.ping_target():
                        utils.print_info("Host is up.")
                        input("\nPress any key to continue...")
                    utils.print_info("Host is down.")
                case 99:
                    break

info = []
