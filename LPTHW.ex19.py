# Exercise 19
""""
Functions and Variables
the variables in your function are not connected to the variables in your script
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
# def is telling python that we want to make a function by using 'def' for define
# after def we are giving the function a name
	print(f"You have {cheese_count} cheeses!")
	# print statement 
	# cheese and crackers reading left to right for what it is defined as
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	# same as above
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

"""	
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# we defined this above as printing the above statements 

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# here we are creating new variables directly in the script

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# this statment is calling the defined statement at the beginning
# commanding the defined statement to use the parameters in parenthesis

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# calling the defined statement to use parameters that require doing math in parenthesis

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# calling the defined statement to use variables that we gave and math 
# at the same time
"""

print("this is my own function")
cheese_count = 40
boxes_of_crackers = 50
cheese_and_crackers(cheese_count + 10, boxes_of_crackers - 5)

# What is this showing us?
"""
this is showing us all the different ways we're able to give our function
	cheese_and_crackers
the values it needs to print them. you can give it variables, math, straight numbers, 
or even combine math and variables

in a way, arguments to a function are kind of like our = character when we make a variable. 
if you use a = to name something, you can usually pass it to a function as an argument
"""