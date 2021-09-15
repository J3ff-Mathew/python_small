age=input("How old are you?\n")



# if age  :
# 	age=int(age)
# 	if age < 18 :#to young sorry
# 		print("Sorry boy too YOUNG to enter....")
# 	else:
# 		if age >=18 and age <=21:#18-21 wrist band
# 			print("You get the entry But you need to wear a WRIST BAND\n")
# 		elif age >21:#21+ drink normal entry
# 			print("You get the normal entry and you can DRINK ")
# else:#invalid entry
# 	print("please enter an age")



#	////////////////////////////////////////////////////////////////////////////////////
#ALTERNATE METHOD
if age  :
	age=int(age)
	if age >=21 :#to young sorry
		print("You get the normal entry and you can DRINK ")
	elif age >=18 :#18-21 wrist band
			print("You get the entry But you need to wear a WRIST BAND\n")
	else :#21+ drink normal##### #entry
			print("Sorry boy too YOUNG to enter....")
else:#invalid entry
	print("please enter an age")