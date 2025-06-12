import os
import sys
import const

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.get_ovpn_file()

    def get_ovpn_file(self):
        for file in os.listdir(const.PATH):
            path = os.path.join(const.PATH, file)
            if os.path.isfile(path):
                print(file)

tryhackme = TryHackMe()
