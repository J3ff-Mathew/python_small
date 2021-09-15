from random import randint
x = randint(1,10)
guess = 0
while x != guess:
	
	guess = int( input( "Enter your guess from no (1-10):  " ) )

	if x > guess:
		print("You guessed low")
	elif x < guess:
		print("You guessed high")
	else:
		print("Your guess was correct")
		print("The no was ",x)
		play=input("Do you want to keep playing?(y/n): ")
		if play=='y':
			guess = 0
			x = randint(1,10)

print("Thanks for playing ")
