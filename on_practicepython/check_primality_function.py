def get_integer():
	return int(input("choose a number: "))

def is_not_prime(number):
	boo = True
	for x in range(2, number):
		print(x, "-", float(number)/x)
		if (float(number) / x).is_integer():
			boo = False
	return boo

number = get_integer()
if is_not_prime(number):
	print("your number is a prime number")
else:
	print('your number is not a prime number')
	
