from colorama import Fore, Style
import os

def print_header(text, user, conn, ip, width=40):
    os.system("clear")
    content_width = width - 2
    head = f"+" + "\t\t{text}\t\t" + "+"

    line = "+" + ("-" * len(head) + "+")

    user_line = f"👤    User: {user.capitalize()}"
    conn_line = f"🛜    Status: {conn.capitalize()}"
    ip_line = f"🖥️     IP: {ip}"

    print(line)
    print(head)
    print("|" + user_line + (" " * len(head)) + "|")
    print("|" + conn_line + (" " * len(head)) + "|")
    print("|" + ip_line + (" " * len(head)) + "|")


    '''
    print("+" + "-" * content_width + "+")
    print("|" + text.upper().center(content_width) + "|")
    print("|" + "-" * content_width + "|")

    print("|" + " " * content_width + "|")
    print("|" + user_line.ljust(content_width) + "|")
    print("|" + conn_line.ljust(content_width) + "|")
    print("|" + ip_line.ljust(content_width) + "|")

    print("|" + " " * content_width + "|")
    print("+" + "-" * content_width + "+")
    '''

def print_err(text):
    print(Fore.RED + text + '\n' + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + text + '\n' + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + text + '\n' + Style.RESET_ALL)



