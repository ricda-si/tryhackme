import os
import sys
import const

class TryHackMe:
    def __init__(self):
        os.system("clear")
        self.get_ovpn_file()

    def get_ovpn_file(self):
        for file in os.listdir(const.PATH):
            print(file)


tryhackme = TryHackMe()
