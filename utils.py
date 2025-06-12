from colorama import Fore, Style
import os

def print_header(title, width=50):
    header = f"║\t\t{title}\t\t║"
    upperline = "╔" + "=" * width + "╗"
    bottomline = "╚" + "═" * width + "╝"

    print(upperline)
    print(header)
    print(bottomline)

def print_user_info(user, conn, ip):
    user_line = f"👤: {user.capitalize()}   |"
    conn_line = f"🛜: {conn.capitalize()}   |"
    ip_line = f"🖥️:   {ip}                  |"

    line = "+" + "-" * len(conn_line) + "+"
    print(line)
    print(f"|{user_line}\t\t|")
    print(f"|{conn_line}\t\t|")
    print(f"|{ip_line}\t\t|")

def print_err(text):
    print(Fore.RED + text + '\n' + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + text + '\n' + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + text + '\n' + Style.RESET_ALL)



