import tryhackme as thm
import utils
from sys import exit
import os

def menu():
    tryhackme = thm.TryHackMe()
    while True:
        os.system("clear")
        utils.print_header("Menu")
        utils.print_user_info(tryhackme.user, tryhackme.connection, tryhackme.lhost)
        if not tryhackme.check_sudo():
            utils.print_err("Run as sudo!")
            return

        print("1. Connect VPN")
        print("99. Exit")
        usr = int(input("> "))
        match usr:
            case 1:
                tryhackme.vpn_conn()
                if "CONNECTED" in tryhackme.connection:
                    utils.print_success("VPN Connected!")
            case 99:
                tryhackme.stop_conn()
                break

if __name__ == "__main__":
    menu()


