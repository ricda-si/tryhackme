from colorama import Fore, Style
import os

def print_header(title, width=50):
    header = f"  {title}"
    upperline = "+" + "-" * len(header) + "+"
    bottomline = "+" + "-" * len(header) + "+"

    print(upperline)
    print(header)
    print(bottomline)

def print_user_info(conn, lhost):
    conn_line = f"  VPN:    {conn.capitalize()}"
    lhost_line =f"  LHOST:  {lhost}"

    line = "+" + "-" * 30 + "-+"
    print(line)
    print(f"{conn_line}")
    print(f"{lhost_line}")
    print(line)

def print_err(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)

def print_success(text):
    print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

def print_info(text):
    print(Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL)
