""" Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old."""

name = input("what is your name? ")
age  = int(input("how old are you ? "))
age_old = str(2019 + 100 - age)
print(name + ", you will be 100 years in " + age_old)
