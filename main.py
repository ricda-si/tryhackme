import tryhackme as thm
import utils

def menu():
    tryhackme = thm.TryHackMe()
    utils.print_header("Menu")
    print("1. Show info")
    usr = input("> ")
    if usr == "1":
        print(tryhackme.connected)

if __name__ == "__main__":
    while True:
        menu()

