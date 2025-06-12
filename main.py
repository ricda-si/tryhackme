import tryhackme as thm
import utils

def info(user, conn, ip):
    print(f"👤 User: {user.capitalize()}")
    print(f"🌐 Connection: {conn.capitalize()}")
    print(f"🖥️ IP: {ip}")

def menu():
    tryhackme = thm.TryHackMe()
    utils.print_header("Menu")
    if not tryhackme.check_sudo():
        utils.print_err("Run as sudo!")
        return

    print("1. Show info")
    usr = input("> ")
    if usr == "1":
        print("\n", tryhackme.connected)
        input()

if __name__ == "__main__":
    while True:
        menu()

