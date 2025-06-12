from colorama import Fore, Style
import os

def print_header(title, width=50):
    header = f"║    {title}    ║"
    upperline = "╔" + "=" * len(header + "\t\t") + "╗"
    bottomline = "╚" + "═" * len(header) + "╝"

    print(upperline)
    print(header)
    print(bottomline)

def print_user_info(user, conn, ip):
    user_line = f"👤: {user.capitalize()}"
    conn_line = f"🛜: {conn.capitalize()}"
    ip_line = f"🖥️: {ip}"

    line = "+" + "-" * len(conn_line) + "+"
    print(line)
    print(f"{user_line}")
    print(f"{conn_line}")
    print(f"{ip_line}")
    print(line)
    print("\n")

def print_err(text):
    print("\n" + Style.BRIGHT + Fore.RED + text + '\n' + Style.RESET_ALL)

def print_success(text):
    print("\n" + Style.BRIGHT + Fore.GREEN + text + '\n' + Style.RESET_ALL)

def print_info(text):
    print("\n" + Style.BRIGHT + Fore.BLUE + text + '\n' + Style.RESET_ALL)
