# Exercise 18
"""
Names, Variables, Code, Functions
introduction to Functions
functions do 3 things:
1. They name pieces of code the way Variables name strings and numbers
2. They take arguments the way your scripts take argv
3. Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands."

you create a function by using the word 'def' in python. 
"""


# this one is like your scripts with argv
def pretzel(*args):
	arg1, arg2, arg3 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
		
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
		print(f"arg1: {arg1}, arg2: {arg2}")
		
# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
	
# this one takes no arguments
def print_none():
	print("I got nothin'.")
	
pretzel("Zed","Shaw", "cucumber")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

"""
What is "print_two" ??
	1. first we have to tell python that we want to make a function using def for 'define'
	2. we then give the function a name. in this piece of code we just called it 
	'print two' 
	### I dont think thats a good name at all. super confusing. ###
	3. then we tell it that we want (*args) - with the asterisk and in parentheses
	it is like your argv parameter but for functions
	
	
	QUESTIONS !!!!
	
Why do we not use the asterisk for any of the other def commands after the first one???
^ actually see the note in the hashtag after that says the *args is pointless
wait..... there's the 2nd note in "common student questions" that implies it might actually be important



Demonstrating how it is taking whatever variables you are designating as the argument at the bottom????
I think ^ 
	
	4. end the line with a colon :
		start indenting
	5. after the colon all the lines that are indented four spaces will become attached to this name, 'print two'
	
	### do we have to remember all of this???? ####		"""	
			