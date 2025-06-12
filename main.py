import tryhackme as thm
import utils
from sys import exit

def menu():
    tryhackme = thm.TryHackMe()
    while True:
        utils.print_header("Menu")
        utils.print_user_info(tryhackme.user, tryhackme.connection, tryhackme.lhost)
        if not tryhackme.check_sudo():
            utils.print_err("Run as sudo!")
            return

        print("1. Connect VPN")
        print("99. Exit")
        usr = input("> ")
        match usr:
            case 1:
                tryhackme.vpn_conn()
            case 99:
                break
        tryhackme.stop_conn()
        break


if __name__ == "__main__":
    menu()


