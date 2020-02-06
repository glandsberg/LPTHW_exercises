# Exercise 15: Reading Files
"""
We are going to learn about reading from a file 
We are going to write two files - one is going to be a script
the other is going to be a plain text file that contains the following:

This is the stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

We are trying to "open" that file in our script and print it
we do not want to just "hard code" it into our script 
hard code = putting info that should come from a user directly in source code
^ this is bad because we want to load it into other files later
the solution is to use argv or inout to ask the user that file to open
(instead of "hard coding" the file's name)

"""

from sys import argv

script, filename = argv

# the above lines are using argv to get a filename

txt = open(filename)

# this is a new command: open
# taking a parameter and returning a value you can set to your own variable

print(f"Here's your file {filename}:")
print(txt.read())

# we are calling a function on txt "read" 
# we can command a file by using the dot like we did here on line 32 

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())