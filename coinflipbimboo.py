import random
face=["h","t"]
def coin_flip():
	"""flips the coin to find if you win or lose"""
	call=input("Press 'h' for heads and 't' for tails: ").lower()
	flip=random.choice(face)
	if call==flip:
		return "Win"
	else:
		return "Lose"

while quit!='q':
	print(f"You {coin_flip()}")
	quit=input("To quit press q or else press any other key: ")
# def square(num):
# 	"""Finds the squares of the no passed"""
# 	return num**2


# n=int(input("Enter  a no to square:"))
# print(square(n))

