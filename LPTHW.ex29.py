people = 20
cats = 30
dogs = 15

if people < cats:
	print("Too many cats! The world is doomed!")
	
if people > cats:
	print("Not many cats! The world is saved!")
	
if people < dogs:
	print("The world is drooled on!")
	
if people > dogs:
	print("The world is dry!")
	
dogs *= 5
# short hand way of writing dogs + 5 
# this really translates to dogs = dogs + 5

if people >= dogs:
	print("People are greater than or equal to dogs.")
	
if people <= dogs:
	print("People are less than or equal to dogs.")
	
if people == dogs:
	print("People are dogs.")
	
print(dogs)
	
"""
What is the "if" statement doing? 
The "if" statement is creating a branch in the code - like a choose your own adventure book
the if statement says, IF the boolean expression is true, then run the code under it

the code underneath the if needs to be tabbed in (4 spaces)
and a colon at the end of the if line
this is the same thing we did with functions

we can do other boolean statements here besides if

"""