import utils

def menu_user_input():
    while True:
        try:
            user = int(input("> "))
            if user not in [1, 99]:
                utils.print_err("Invalid input.")
                continue
            return user
        except ValueError:
            utils.print_err("Invalid input.")
