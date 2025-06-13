import tryhackme as thm
import scanner as sc
import utils
import input_check
from sys import exit
import os

def menu():
    tryhackme = thm.TryHackMe()
    scanner = sc.Scanner()
    while True:
        os.system("clear")
        utils.print_header("Menu")
        utils.print_user_info(tryhackme.connection, tryhackme.lhost)
        if not tryhackme.check_sudo():
            utils.print_err("Run as sudo!")
            return

        print("1.  Connect VPN")
        print("2.  Scan Target")
        print("99. Exit")
        usr = input_check.menu_user_input()
        match usr:
            case 1:
                if "DISCONNECTED" in tryhackme.connection:
                    tryhackme.vpn_conn()
                    utils.print_info(f"IP: {tryhackme.lhost}")
                    utils.print_success("VPN Connected!")
                    input("Press any key to continue...")
                else:
                    utils.print_info("Conected.")
                    input("Press any key to continue...")
            case 2:
                scanner.menu(tryhackme.connection, tryhackme.lhost)
            case 99:
                if "DISCONNECTED" not in tryhackme.connection:
                    tryhackme.stop_conn()
                break

if __name__ == "__main__":
    menu()
