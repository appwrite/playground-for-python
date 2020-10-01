#import the required function form math module.
from math import sqrt

#function definition to check whether a number is prime or not.

def prime_check(number):
	if number<=1:
		return False
	for i in range(2,int(sqrt(number))+1):
		if (number%i)==0:
			return False
	return True


num = int(input("Enter the number:"))
if prime_check(num):
    print("It is a prime number")
else:
    print("It is not a prime number")
