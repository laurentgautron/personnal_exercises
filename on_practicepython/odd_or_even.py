""" Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
 user. Hint: how does an even / odd number react differently when divided by 2? """

number = int(input("what is our number? "))
odd_or_even = number % 2
if odd_or_even == 0:
    print("your number is an even")
else:
    print("your number is an odd !")
