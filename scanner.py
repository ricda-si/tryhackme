import sys
import os
import utils
import input_check as ichk

class Scanner:
    def __init__(self):
        self.rhost = None

    def get_target(self):
        target = input("Target IP: ")
        utils.print_info(f"RHOST: {target}")
        self.rhost = target

    def ping_target(self):
        if not self.rhost:
            utils.print_err("No target.")
            return None
        return True if os.system(f"ping -n 1 {self.rhost} > /dev/null 2>&1") else False

    def menu(self, info1, info2):
        while True:
            os.system("clear")
            utils.print_header("Scanner")
            utils.print_user_info(info1, info2)

            print("1.  Add target")
            print("2.  Ping target")
            print("99. Exit")

            usr = ichk.scanner_user_input()
            match usr:
                case 1:
                    self.get_target()
                case 2:
                    self.ping_target()



