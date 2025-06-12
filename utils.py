from colorama import Fore, Style

def print_header(text, user, conn, ip, width=40):
    upline = "╔" + "═" * (width-2) + "╗"
    downline = "╚" + "═" * (width-2) + "╝\n"
    content_width = width - 2
    user = f"[👤]  User: {user.capitalize()}"
    conn = f"[🌐]  Connection: {conn.capitalize()}"
    ip = f"[🖥️]  IP: {ip}\n"

    print(upline)
    print("║" + text.center(width-2).upper() + "║")
    print("║" + user.ljust(len(upline)) + "║")
    print("║" + conn.ljust(len(upline)) + "║")
    print("║" + ip.ljust(len(upline)) + "║")
    print(downline)

def print_err(text):
    print(Fore.RED + text + '\n' + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + text + '\n' + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + text + '\n' + Style.RESET_ALL)



