import os
import sys
import const

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.get_ovpn_file()

    def get_ovpn_file(self):
        path = os.path.expanduser(const.PATH)
        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            if os.path.isfile(full_path):
                print(file)

tryhackme = TryHackMe()
