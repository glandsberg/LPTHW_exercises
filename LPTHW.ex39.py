# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	'North Carolina': 'NC'
	'South Carolina': 'SC'
}
# dictionaries use the = { } syntax
# Oregon is the Key and OR is the value 
# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
#adding more pairs to the cities dictionary
cities['NY'] = 'New York'
#
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
# ^ this is printing out the --- to divide those lines
print("NY State has: ", cities['NY'])
# returning the key not the value
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
# states.get is the same thing as what we're doing here with states['Michigan']
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
# this is dictionary inception
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
# items is a built in method off of a dictionary
# methods are basically functions
	print(f"{state} is abbreviated {abbrev}")
# we're looping through dictionaries here 

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")
	
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
# get is another dictionary method
# get is a method that's calling Texas

if not state:
# if state has a value then line 70 is False
	print("Sorry, no Texas.")
#	print("Sorry, that state {state} isn't in the dictionary.")
# this doesn't work because state is undefined
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")