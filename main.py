import tryhackme as thm
import utils
from sys import exit

def menu():
    global run
    tryhackme = thm.TryHackMe()
    utils.print_header("Menu", tryhackme.user, tryhackme.connection, tryhackme.lhost)
    if not tryhackme.check_sudo():
        utils.print_err("Run as sudo!")
        return

    print("1. Show info")
    print("99. Exit")
    usr = input("> ")
    match usr:
        case 1:
            ...
        case 99:
            tryhackme.exit_script()
            run = False
            exit()

run = True
if __name__ == "__main__":
    while run:
        menu()


