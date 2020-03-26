print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do: ')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires explanation 
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
# we called them jelly beans to start and beans later because the function variable is tempoprary 
# when we return it, it can then be assigned a variable later
# ok but wait I don't understand why we can use "started" up there instead of start_point

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f "" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is where the function is being called and we are passing in start_point
# start_point is a variable and is mutable which means you can change it
# tuples are immutable 
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
# the asterisk means 
