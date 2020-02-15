# Functions can return something too!

"""
We have been using the = character to name variables and set them to numbers or strings
we are going to now use = and the word 'return'
this gets python to set variables to be a value from a function

"""

def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b
	
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b
	
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b
	
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b
	
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")