from colorama import Fore, Style

def print_header(text, user, conn, ip, width=40):
    content_width = width - 2

    user_line = f"👤    User: {user.capitalize()}"
    conn_line = f"🌐    Connection: {conn.capitalize()}"
    ip_line = f"🖥️      IP: {ip}"

    print("╔" + "═" * content_width + "╗")
    print("║" + text.upper().center(content_width) + "║")
    print("║" + " " * content_width + "║")

    print("║" + user_line.ljust(content_width) + "║")
    print("║" + conn_line.ljust(content_width) + "║")
    print("║" + ip_line.ljust(content_width) + "║")

    print("║" + " " * content_width + "║")
    print("╚" + "═" * content_width + "╝")

def print_err(text):
    print(Fore.RED + text + '\n' + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + text + '\n' + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + text + '\n' + Style.RESET_ALL)



