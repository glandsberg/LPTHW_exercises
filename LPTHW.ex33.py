""""

i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)
	
	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	

print("The numbers: ")

for num in numbers:
	print(num)
	
	"""
	
# for loops go through everything
# next lesson is basically saying you can access all of these elements without a loop
# loops are what causes a program to be slower because it cannot access directly it needs to browse through it

# for loops are for iterating through a data structure
# while loops are for doing something as long as its true - breaks as soon as it is false
# ^ you can do something until a condition changes

"""
What's the benefit of using a while loop over a for loop

* try and define the variables you need outside of the loop

numbers = []
^ this is doing that
if you're adding to the array, it needs to be outside of the 'while' block of code 

What is an array?
an array is a data structure that has variables of all the same type 
^ this is the main difference between lists and arrays -
lists can contain values w different data types 
arrays must be the same
"""

def while_func(limit):

	i = 0
	numbers = []

	while i < limit:
		print(f"At the top i is {i}")
		numbers.append(i)
	
		i = i + increment
		
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	

	print("The numbers: ")

	for num in numbers:
		print(num)
		
user_limit = int(input("What limit would you like?"))
user_increment = int(input("What would you like to increment by?"))
while_func(user_limit, user_increment)