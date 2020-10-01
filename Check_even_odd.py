# function to check whether a number is even or odd.
def check_even_odd(number):
	if number%2 == 0:
		print(number,"is even")
	else:
		print(number,"is odd")

num = int(input("Enter the number:"))
check_even_odd(num)