import tryhackme as thm
import utils

def menu():
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


if __name__ == "__main__":
    while True:
        menu()

