'''
Numbers and more in Python!

We'll learn about the following topics:

1.) Types of Numbers in Python
2.) Basic Arithmetic
3.) Differences between classic division and floor division
4.) Object Assignment in Python
'''

'''
Types of numbers:
Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.

Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.

Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.
'''

# Now let's start with some basic arithmetic.

# Addition
print(2+1) #output will be 3

# Subtraction
print(2-1) #output will be 1

# Multiplication
print(2*2) #output will be 4

#Division
print(3/2) #output will be 1.5

#Floor Division
print(7//4) #output will be 1

'''
Whoa! What just happened? Last time I checked, 7 divided by 4 equals 1.75 not 1!

The reason we get this result is because we are using "floor" division. The // operator (two forward slashes) truncates the decimal without rounding, and returns an integer result.
'''

#So what if we just want the remainder after division?
#Modulo
print(7%4) #output will be 3

#4 goes into 7 once, with a remainder of 3. The % operator returns the remainder after division.

'''
Arithmetic continued
'''

# Powers
print(2**3) #output will be 8

# Can also do roots this way
print(216**(1/3)) #output will be 5.999999999999999

# Order of Operations followed in Python
print(2 + 10 * 10 + 3) #output will be 105

# Can use parentheses to specify orders
print((2+10) * (10+3)) #output will be 156

'''
Variable Assignments
Now that we've seen how to use numbers in Python as a calculator let's see how we can assign names and create variables.

We use a single equals sign to assign labels to variables. Let's see a few examples of how we can do this.
'''

# Let's create an object called "a" and assign it the number 5
a = 5 #Now if I call a in my Python script, Python will treat it as the number 5.

#Adding the objects
print(a+a) #output will be 10

#What happens on reassignment? Will Python let us write it over?

# Reassignment
a = 10

# Check
print(a) #output will be 10

'''
Yes! Python allows you to write over assigned variable names. We can also use the variables themselves when doing the reassignment. Here is an example of what I mean:
'''

# Check
print(a) #output will be 10

#Use A to redefine A
a = a + a

#check
print(a) #output will 20

'''
The names you use when creating these labels need to follow a few rules:

1. Names can not start with a number.
2. There can be no spaces in the name, use _ instead.
3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
4. It's considered best practice (PEP8) that names are lowercase.
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
   or 'I' (uppercase letter eye) as single character variable names.
6. Avoid using words that have special meaning in Python like "list" and "str"
'''

# Using variable names can be a very useful way to keep track of different variables in Python. For example:

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# Show my taxes!
print(my_taxes) #output will be 10.0

'''
So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
'''