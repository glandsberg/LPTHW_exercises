# Exercise 17 - More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

"""
on line 4 we imported another command "exists" 
this will return "True" if the file exists, and False if not
we are only seeing how we can import it 
importing is a good way to get lots of free code
"""

# I don't really understand what "Echo" is doing in the book
# echo is a bash command
# echo "This is a test file." > test.txt makes a file 
# the >> would append if it already exists