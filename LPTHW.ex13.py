# Exercise 13: Parameters, Unpacking, Variables

"""
now we will cover another input method that you can use to pass variables to a script
script = another name for .py files 
we have typed python3.6 LPTHW.ex13.py to run the LPHTHW.ex13.py file
the LPTHW.ex13.py part of the command is called an "argument"
now we are going to write a script that also accepts arguments
"""

from sys import argv
#this is an import command and how we add features
# features are actually called modules 
script, first, second, third = argv
# argv = argument variable
# holds the argument that you pass to your python script
# this list is "unpacking" the argv - rather than holding all arguments, it gets assigned 

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# You can put anything you want for the assignments and it will print in the order left to right



