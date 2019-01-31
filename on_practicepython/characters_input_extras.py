""" Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
tells them the year that they will turn 100 years old. Add on to the previous program by asking the user for another
 number and printing out that many copies of the previous message. Print out that many copies of the previous message
 on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

name = input("what is your name? ")
age  = int(input("how old are you ? "))
age_old = str(2019 + 100 - age)
response = name + ", you will be 100 years in " + age_old
print(response)
number = int(input("choose a number: "))
print((response + '\n')*number)
