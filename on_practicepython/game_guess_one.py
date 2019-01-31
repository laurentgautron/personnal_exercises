""" Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right."""

import random

number = str(random.randint(1,9))
print(number)
counter = 1
user_number = input("guess the number (or type 'exit' if you want to quit): ")
while user_number not in (number, 'exit'):
    if user_number == "exit":
        break
    if user_number < number:
        print("it's greater")
    else:
        print("it's smaller")
    user_number = input("try again: ")
    counter += 1
print("you win in {} try !!".format(counter))