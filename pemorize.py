#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# pmemorize.py

__AUTHOR__ = 'Josh Burgess'
__VERSION__ = 'BETA'

BLUE, RED, WHITE, YELLOW, GREEN, END = "\33[94m", "\033[91m", "\33[97m", "\33[93m", "\033[32m", "\033[0m"

def heading():
    stdout.write(GREEN + """
    ██▓███   ███▄ ▄███▓▓█████  ███▄ ▄███▓ ▒█████   ██▀███   ██▓▒███████▒▓█████
    ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▒ ▒ ▒ ▄▀░▓█   ▀
    ▓██░ ██▓▒▓██    ▓██░▒███   ▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒▒██▒░ ▒ ▄▀▒░ ▒███
    ▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ▒██    ▒██ ▒██   ██░▒██▀▀█▄  ░██░  ▄▀▒   ░▒▓█  ▄
    ▒██▒ ░  ░▒██▒   ░██▒░▒████▒▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒░██░▒███████▒░▒████▒
    ▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ░▒▒ ▓░▒░▒░░ ▒░ ░
    ░▒ ░     ░  ░      ░ ░ ░  ░░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░░░▒ ▒ ░ ▒ ░ ░  ░
    ░░       ░      ░      ░   ░      ░   ░ ░ ░ ▒    ░░   ░  ▒ ░░ ░ ░ ░ ░   ░
    ░      ░  ░       ░       ░ ░     ░      ░    ░ ░       ░  ░
    ░
    Pmemorize is designed to help remember long passwords.
    It takes a password as a string and breaks it up into parts and allows one to memorize
    those parts individually. Once one part is considered memorized, the next part of the password is studied.
    The hope is, is that eventually you would retain the entire password to memory.

    Written by{} Josh Burgess{}
    """.format(RED, END))

def validate_password(pw):
        """Attempts to validate the password by peforming a series of tests, inside of a loop.
        Option 0: Default"""

        while True:
            attempt = getpass("\t\t[?]\t")
            if attempt == pw:
                return "\t\t[!]\t Correct"

            else:
                system("clear")
                heading()
                print("[!] Incorrect, Try Again.")
                continue


def main():

    heading()
    try:
        while True:
            password = getpass("\n\t\tEnter your password, amigo. ")
            if len(password) != 0:
                break
            else:
                print("\n\t\t[!] No Input Given, Try Again.")


        print("\n\t\tHow would you like your password?\n")
        print("\t\t[1] Whole")
        print("\t\t[2] Half")
        print("\t\t[3] Quarters\n")
        stdout.write(GREEN + "\t\t" + "*" * 110 + END + "\n")

        while True:
            password_options = input("\t\t[?]\t")
            if not password_options.isdigit():
                print("\n\t\t[!] Invalid Option, Try Again.")
            else:
                break

            if password_options == 1:
                if len(password) in range(1, 8+1):
                    print("[!] Clearing STDOUT in 10 seconds, Take Note.")
                    print(password)
                    system("sleep 10 && clear")
                    heading()
                    validate_password(password, option=1)
                else:
                    print("[!] {} characters would be difficult to remember, try breaking it up into segments.".format(len(password)))


            elif password_options == 2:
                if len(password) in list(range(8, 12+1)):
                    password_length = len(pw)
                    first_half = pw[0:int(password_length / 2)]
                    second_half = pw[first_half:]

                    print("[!] Clearing STDOUT in 10 seconds, take note.")
                    print(first_half)
                    system("sleep 10 && clear")
                    heading()
                    validate_password(first_half)

                    print("[!] Clearing STDOUT in 10 seconds, take note.")
                    print(second_half)
                    system("sleep 10 && clear")
                    heading()
                    validate_password(second_half)

                elif len(password) > 12 and len(password) < 24:
                    split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
                    for i in split_string(password, len(password) // 3):
                        validate_password(i)

            else:
                print("[!] Passwords of these lengths should be stored inside of a password manager, instead")


    except KeyboardInterrupt:
        system("clear")
        return "[!] Received Ctrl+C, closing..."



if __name__ == "__main__":
    from os import system
    from getpass import getpass
    from sys import stdout
    main()
