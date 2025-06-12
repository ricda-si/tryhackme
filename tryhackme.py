import os
import sys
import const

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.get_ovpn_file()

    def get_ovpn_file(self):
        for file in os.listdir(const.PATH):
            if os.path.isfile(os.path.join(const.PATH, file)):
                print(file)


tryhackme = TryHackMe()
