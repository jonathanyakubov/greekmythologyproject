
from sys import exit

#greek mythology game

def poseidon():
	print "Welcome! Poseidon is sending you on a mission."
	print "You are going with Hercules to complete the 12 voyages."
	print "Before you do, you need to get the sword under a closed door behind the Three-headed dog."
	print "Do you taunt the dog or try to put in to sleep with your siren abilities."
	dog_moved = False

	while True:
		next = raw_input(">")

		if next =="taunt" and not dog_moved:
			print "Sorry, but you've pissed off the dog, and it eats your hand off, try again"
			dog_moved= True
		elif "siren" in next and dog_moved:
			print "Great the dog is asleep, but still didn't move."
		elif next=="taunt" and dog_moved:
			print "You opened the door and got the sword, but there's more in store"
			sword()
		else:
			dead("I don't know what you're typing.")

def sword():
	print "You are in a lair with Medusa. That's rough."
	print "Do you flee or try to cut her hair."
	next = raw_input(">")
	if "flee" in next:
		start()
	elif "cut" in next:
		dead("She's stronger than you, sorry.")
	else:
		zeus()

def zeus():
	print "You are in Zeus' company."
	print "He is angry that you have intefered during his affair."
	print "Do you stop him or steal some of his $$ and go away."
	next = raw_input(">")
	if "stop" in next:
		dead("Come on man, what are you thinking, it's zeus.")
	elif "take" in next:
		print "How much do you take?"
		how_much = raw_input(">")

		if "0" in how_much or "2" in how_much:
			money=int(how_much)
		else:
			dead("Sorry, don't understand.")

		if money<100:
			print "You can take more I guess."
			exit(0)
		else:
			dead("You're not gonna make it alive with all that dough.")
	else:
		dead("Sorry you just suck.")


def start():
	print "You are on Mt. Olympus, and you have two doors to choose from."
	print "Which do you take, left or right."
	next = raw_input(">")
	if "left" in next:
		poseidon()
	elif "right" in next:
		zeus()
	else:
		dead("What the hell are you smoking?")



def dead(why):
	print why, "Nice job, you got yourself killed."
	exit(0)

start()
