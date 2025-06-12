from colorama import Fore, Style

def print_header(text, width=40, char='=', info=""):
    print("╔" + "═" * (width-2) + "╗")
    print("║" + text.center(width-2).upper() + "║")
    print("║" + info.center(width-2).upper() + "║")
    print("╚" + "═" * (width-2) + "╝")

def print_err(text):
    print(Fore.RED + text + Style.RESET_ALL)

def print_success(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def print_info(text):
    print(Fore.BLUE + text + Style.RESET_ALL)



