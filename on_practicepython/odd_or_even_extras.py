""" Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
 user. Hint: how does an even / odd number react differently when divided by 2?
 Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
 evenly into num, tell that to the user. If not, print a different appropriate message."""

number = int(input("what is our number? "))
divisor = int(input("what is the divisor? "))
mod = number % divisor
divisor = str(divisor)
if (number % 4) == 0:
    print('your number is divisible by 4')
elif (number % 2) == 0:
    print('your number is an even')
else:
    print('your number is an odd')
if mod == 0:
    print("your can divide it by" + divisor + " !")
else:
    print("your can't divide it by" + divisor + " !")
