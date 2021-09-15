# print("Rock == r")
# print("paper == p")
# print("scisors == s")

# choice_1=input("Enter the choice of player 1\n")

# #print("########## NO CHEATING ##########\n\n" * 20)

# choice_2=input("Enter the choice of player 2\n")


# if choice_2==choice_1:
# 	print("It's a Draw!!!!")

# elif  (choice_1!=('r' or 'p' or 's') ) or (choice_2!=('r' or 'p' or 's')):
# 	print("INVALID TEXT ENTRY!!!\n")

# elif choice_1=='r':
# 	if choice_2=='p':
# 		print("player 2 WINS!!!\n")
# 	elif choice_2=='s':
# 		print("player 1 WINS\n")

# elif choice_1=='p':
# 	if choice_2=='s':
# 		print("player 2 WINS!!!\n")
# 	elif choice_2=='r':
# 		print("player 1 WINS\n")

# elif choice_1=='s': 
# 	if choice_2=='r':
# 		print("player 2 WINS\n")
# 	elif choice_2=='p':
# 		print("player 1 WINS!!!\n")



# else :
# 	print("Some thing went wrong\n")


#################################THIS WAS FOR 2 PLAYERS###############################


#######################THE NEX ONE IS AGAINST A COMPUTER####################################
import random

# alternative method <from random import randint>
print("Rock == r")
print("paper == p")
print("scisors == s")

player_wins = 0
computer_wins = 0
no_of_games=int(input("how many points should one score to win? "))

while player_wins < no_of_games  and  computer_wins < no_of_games:
	print(f"The current score is player:{player_wins} $ computer {computer_wins}")

	choice_1=input("Enter the YOUR choice \n")

	#print("########## NO CHEATING ##########\n\n" * 20)

	rand_num = random.randint(0,100)
	rand_num = rand_num % 3

	if rand_num==0:
		choice_2 = "r"
	elif rand_num==1:
		choice_2 = "p"
	else:
		choice_2 = "s"

	print(f"The computer picked {choice_2}\n")



	if choice_2==choice_1:
		print("It's a Draw!!!!")

	elif choice_1=='r':
		if choice_2=='p':
			print("computer WINS!!!\n")
			computer_wins += 1
		elif choice_2=='s':
			print("player WINS\n")
			player_wins += 1

	elif choice_1=='p':
		if choice_2=='s':
			print("computer WINS!!!\n")
			computer_wins += 1
		elif choice_2=='r':
			print("player WINS\n")
			player_wins += 1

	elif choice_1=='s': 
		if choice_2=='r':
			print("computer WINS\n")
			computer_wins += 1
		elif choice_2=='p':
			print("player WINS!!!\n")
			player_wins += 1

	elif choice_1 == 'quit' or 'q':
		break


	elif  (choice_1!=('r' or 'p' or 's') ) or (choice_2!=('r' or 'p' or 's')):
		print("INVALID TEXT ENTRY!!!\n")



	else :
		print("Some thing went wrong\n")

print(f"The final score is player:{player_wins}  computer {computer_wins}")
