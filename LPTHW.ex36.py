from sys import exit
	 	

def cat_room():
	print("There are a lot of cats here.")
	print("The cats are starting to approach.")
	print("Do you flee for your life? Pet them? Feed them with the jerkey in your pocket?")
	cats_hiding = False
		# this needs to be True to run because it cannot run while False
	
	while True:
		choice = input("> ")
		
		if choice == "pet":
			dead("The cats scratch your face off.")
		elif "flee" in choice:
			print("The cats are hiding now.")
			dead("You escaped.")
			cats_hiding = True 
		elif "feed" in choice:
			dead("The cats are eatin. You're safe.")
			

def dog_room():
	print("There are a lot of dogs here.")
	print("The dogs are starting to approach.")
	print("Do you flee for your life? Pet them? Feed them with the jerkey in your pocket?")
	
	choice = input("> ")
	choice = choice.lower()
	print(choice)
	# this makes it so that you could enter your text in any case and it will automatically lowercase it.
	
	if "pet" in choice or "feed" in choice:
	# we needed to add the "in choice" after "pet" because each side of the or is treated as a separate conditional
	# if choice == "pet" or choice == "feed" 
		dead("Cool! Dogs are happy. You're safe.")
	elif "flee" in choice:
		dead("The dogs ate you.")
	else:
		dog_room()
		

def dead(why):
	print(why, "Good job!")
	exit(0)
	
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	choice = input("> ")
	
	if choice == "left":
		cat_room()
	elif choice == "right":
		dog_room()
	else:
		dead("You are eaten by rats.")
		
		
start()