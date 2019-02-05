""" Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the 
number, then tell them whether they guessed too low, too high, or exactly right."""

import random

want_continue = ""
while True:
    if want_continue in  ("exit", "n"):
        print("ok, Bye !")
        break
    else:
        number = random.randint(1, 9)
        print(number)
        counter = 1
        user_number = input("guess the number (or type 'exit' if you want to quit): ")
        while user_number not in (str(number), 'exit'):
            user_number = int(user_number)
            print(user_number < number)
            if user_number == "exit":
                break
            if user_number < number:
                print("it's greater")
            else:
                print("it's smaller")
            user_number = input("try again: ")
            counter += 1
        if user_number == "exit":
            print("you loose !! after {} try".format(counter))
            break
        else:
            print("you win in {} try !!".format(counter))
            want_continue = input("do you want  play again (y/n)? ")
            while want_continue not in ("y", "n"):
                want_continue = input(" you type {}, it's not a good answer ! ".format(want_continue))
