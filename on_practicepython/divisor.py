""" Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
divisor of 26 because 26 / 13 has no remainder.) """

number = int(input("choose a number: "))
divisor_list = [elements for elements in range(2, number+1) if number % elements == 0]
print("the divisor for", number, "are", divisor_list)
