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

def tidy_screen(option=0):

    if option == 1:
        system("sleep 5 && clear")
        heading()
    elif option == 2:
        system("clear")
        heading()
    elif option == 3:
        heading()
    elif option == 4:
        system("clear")
def validate_password(pw):
    """Reveives the password and starts a simple loop to check if the inputted value(pw)
        matches the original password"""
    try:
        while True:
            attempt = getpass("[!] Enter Your Password\t ")
            if attempt == pw:
                return
            else:
                print("[!] Incorrect, Try Again.")

    except KeyboardInterrupt:
        print(KeyboardInterrupt("\n[!] Received Ctrl+C, closing..."))
        exit()
def complete_password(pword, pword_length):

    try:
        if pword_length in range(1, 8+1):
            stdout.write(RED + "\n\t\t" + "*" * 110 + END)
            stdout.write(RED + "\n\t\t{}\n".format(pword) + END)
            stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

            print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

            tidy_screen(option=1)
            validate_password(pword)
            tidy_screen(option=2)

            print("\n\t\t[!] Correct")
            exit()

        else:
            print("\t\t[!] {} characters would be difficult to remember, try breaking it up into segments.\n".format(pword_length))
            exit()

    except KeyboardInterrupt:
        print("\n\t\t[!] Received Ctrl+C, closing...")
        exit()
def half_password(pword, pword_length):

    try:
        if pword_length in range(4, 8+1):
            first_half = pword[0:int(pword_length / 2)]
            second_half =  pword[len(first_half):]

            stdout.write(RED + "\n\t\t" + "*" * 110 + END)
            stdout.write(RED + "\n\t\t{}\n".format(first_half) + END)
            stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

            print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

            tidy_screen(option=1)
            validate_password(first_half)
            tidy_screen(option=2)

            print("[!] Correct")

            stdout.write(RED + "\n\t\t" + "*" * 110 + END)
            stdout.write(RED + "\n\t\t{}\n".format(second_half) + END)
            stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

            print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

            tidy_screen(option=1)
            validate_password(second_half)
            tidy_screen(option=2)

            print("\n\t\t[!] Correct")
            exit()

        elif pword_length in range(1, 4+1):
            complete_password(pword, pword_length)

        if pword_length in range(8, 13+1):
            first_half = pword[0:int(pword_length / 2)]
            second_half =  pword[len(first_half):]

            stdout.write(RED + "\n\t\t" + "*" * 110 + END)
            stdout.write(RED + "\n\t\t{}\n".format(first_half) + END)
            stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

            print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

            tidy_screen(option=1)
            validate_password(first_half)
            tidy_screen(option=2)

            print("[!] Correct")

            stdout.write(RED + "\n\t\t" + "*" * 110 + END)
            stdout.write(RED + "\n\t\t{}\n".format(second_half) + END)
            stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

            print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

            tidy_screen(option=1)
            validate_password(second_half)
            tidy_screen(option=2)

            print("\n\t\t[!] Correct")
            exit()

        elif pword_length in range(13, 18+1):
            split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
            pword_segments = []
            for i in split_string(pword, pword_length // 3):
                pword_segments.append(i)

            if len(pword_segments[-1]) < 4:
                pword_segments[-2] += pword_segments[-1]
                pword_segments.pop(-1)

            for segment in pword_segments:

                stdout.write(RED + "\n\t\t" + "*" * 110 + END)
                stdout.write(RED + "\n\t\t{}\n".format(segment) + END)
                stdout.write(RED + "\t\t" + "*" * 110 + "\n" + END)

                print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

                tidy_screen(option=1)
                validate_password(segment)

                print("\n\t\t[!] Correct")
                exit()


        elif pword_length in range(18, 24+1):
            split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
            for segment in split_string(pword, pword_length // 4):

                stdout.write(RED + "\n*" * 110 + END)
                stdout.write(RED + "\n\t\t{}\n".format(segment) + END)
                stdout.write(RED + "*\n" * 110 + END)

                print("\n\t\t[!] Clearing STDOUT in 5 seconds, take note.")

                tidy_screen(option=1)
                validate_password(segment)

                print("\n\t\t[!] Correct")
                exit()
        else:
            print("\n\t\t[!] Passwords of these lengths should be stored inside of a password manager, instead")
            print("\n\t\t[!] Closing...")
            exit()

    except KeyboardInterrupt:
        print("\n\t\t[!] Received Ctrl+C, closing...")
        exit()

def main():
    try:
        tidy_screen(option=3) # Show pemorize banner
        password = ""
        while True:
            password += getpass("\n\t\tEnter your password, amigo. ")
            if not len(password) == 0:
                break
            else:
                print("\n\t\t[!] No Input Given, Try Again.")

        tidy_screen(option=2) # Just in case if the else clause has polluted STDOUT, We'll clear the screen and show the pemorize banner.

        print("\n\t\tHow would you like your password?\n")
        print("\t\t[1] Complete")
        print("\t\t[2] In Parts")

        stdout.write(GREEN + "\t\t" + "*" * 110 + END + "\n")

        while True:
            password_length = len(password)
            password_options = 0
            while True:
                try:
                    option_input = int(input("\t\t[?]\t"))
                    if option_input in range(1,2+1):
                        password_options += option_input
                        break
                    else:
                        print("\n\t\t[!] Invalid Option '{}', Try Again.".format(option_input))

                except ValueError:
                    print("\n\t\t[!] Invalid Character '{}', Try Again.".format(option_input))

            if password_options == 1:
                complete_password(password, password_length)

            elif password_options == 2:
                half_password(password, password_length)

            else:
                print("\n\t\t[!] Invalid Option, Try Again.")

    except KeyboardInterrupt:
        print("\n\t\t[!] Received Ctrl+C, closing...")
        exit()

if __name__ == "__main__":
    from os import system, close
    from getpass import getpass
    from sys import stdout, exit
    main()
