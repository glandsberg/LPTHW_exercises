# Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())
	
def rewind(f):
	f.seek(0)
	#it's almost like the cursor goes to the end when you run the rile
	# when you do a read on a file - the cursor is now at the bottom
	# you have to bring the seek back up to 0 to read from the beginning of the file
	
def print_a_line(line_count, f):
	print(line_count, f.readline())
	
current_file = open(input_file)

print("Firdt let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

