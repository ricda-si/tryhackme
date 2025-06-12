import tryhackme as thm
import utils
import input_check
from sys import exit
import os

def menu():
    tryhackme = thm.TryHackMe()
    while True:
        os.system("clear")
        #utils.print_header("Menu")
        utils.print_user_info(tryhackme.user, tryhackme.connection, tryhackme.lhost)
        if not tryhackme.check_sudo():
            utils.print_err("Run as sudo!")
            return

        print("1.  Connect VPN")
        print("99. Exit")
        usr = input_check.menu_user_input()
        match usr:
            case 1:
                tryhackme.vpn_conn()
                if "DISCONNECTED" not in tryhackme.connection:
                    utils.print_success("VPN Connected!")
                    input("\nPress any key to continue.")
                else:
                    utils.print_err("Erro.")
                    input("\nPress any key to continue.")
            case 99:
                if "DISCONNECTED" not in tryhackme.connection:
                    tryhackme.stop_conn()
                break

if __name__ == "__main__":
    menu()


