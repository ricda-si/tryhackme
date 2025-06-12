from colorama import Fore, Style
import os

def print_header(title, width=50):
    header = f"║{title}║"
    upperline = "╔" + "=" * len(header) + "╗"
    bottomline = "╚" + "═" * len(header) + "╝"

    print(upperline)
    print(header)
    print(bottomline)

def print_user_info(user, conn, ip, target=None):
    user_line = f"User:   {user.capitalize()}"
    conn_line = f"VPN:    {conn.capitalize()}"
    ip_line =   f"Host:   {ip}"
    target =    f"Target: {target}"

    line = "+" + "-" * 20 + "-+"
    print(line)
    print(f"{user_line}")
    print(f"{conn_line}")
    print(f"{ip_line}")
    print(f"{target}")
    print(line)
    print("\n")

def print_err(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)

def print_success(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

def print_info(text):
    print(Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL)
