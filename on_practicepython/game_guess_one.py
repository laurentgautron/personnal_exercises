""" Generate a random NUMBER between 1 and 9 (including 1 and 9). Ask the user to guess the
NUMBER, then tell them whether they guessed too low, too high, or exactly right."""

import random

WANT_CONTINUE = ""
while True:
    if WANT_CONTINUE in  ("exit", "n"):
        print("ok, Bye !")
        break
    else:
        NUMBER = random.randint(1, 9)
        print(NUMBER)
        COUNTER = 1
        USER_NUMBER = input("guess the NUMBER (or type 'exit' if you want to quit): ")
        while USER_NUMBER not in (str(NUMBER), 'exit'):
            USER_NUMBER = int(USER_NUMBER)
            print(USER_NUMBER < NUMBER)
            if USER_NUMBER == "exit":
                break
            if USER_NUMBER < NUMBER:
                print("it's greater")
            else:
                print("it's smaller")
            USER_NUMBER = input("try again: ")
            COUNTER += 1
        if USER_NUMBER == "exit":
            print("you loose !! after {} try".format(COUNTER))
            break
        else:
            print("you win in {} try !!".format(COUNTER))
            WANT_CONTINUE = input("do you want  play again (y/n)? ")
            while WANT_CONTINUE not in ("y", "n"):
                WANT_CONTINUE = input(" you type {}, it's not a good answer ! ".format(WANT_CONTINUE))
