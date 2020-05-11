ten_things = "Apples Oranges Crows Telephone Light Sugar"
# a string

print("Wait there are not 10 things in that list. Let's fix that.")
# printing something

stuff = ten_things.split(' ')
# getting rid of the space - split it at the space, split it into separate items instead of a whole string
# makes it look like more_stuff
# showing you how to quickly convert string into data for a list

more_stuff = ["Day", "Night", "Song", "Frisbee",
				"Corn", "Banana", "Girl", "Boy"]
				
while len(stuff) != 10:
# while loop
# while the length is not equal to 10 it is going to do the following:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")
	# or you could do %d items now % len(stuff)
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa fancy
print(stuff.pop())
print(' '.join(stuff)) # whattt cool
print('#'.join(stuff[3:5])) # super cool


"""
an 'array' and a 'list' are the same thing
the delimiter defaults to a space unless specific

.pop is used for queue in 'formal data structures'
-1 (negative one) grabs the last element of the list
then you could also 
^ that's really unique for python 
remember splicing from earlier so 3:5 is grabbing 3-5 but does not include the 5 
"""