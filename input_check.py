def menu_user_input():
    while True:
        try:
            user = int(input("> "))
            return user
        except ValueError:
            print("Invalid input.\n")
