# # # # # # n=int(input("How many times do i have to tell you?\n"))

# # # # # # print("CLEAN UP YOUR ROOM!!!!!\n"*n)

# # # # # #########################	ALTERNATIVELY##################
# # # # # n=int(input("How many times do i have to tell you?\n"))

# # # # # for i in range(n):
# # # # # 	print("CLEAN UP YOUR ROOM!!!!!")


# # # # #######################emogi pyramid##############

# # # i=1
# # # while i<10:
# # # 	print("\U0001f600" * i)
# # # 	i += 1


# # # #############################OR######################3
# # # i=1
# # # while i<11:
# # # 	j=1
# # # 	while j<i:
# # # 		print(" *",end='||')
# # # 		j += 1
# # # 	print("")
# # # 	i=i+1

# # sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# # # Define your code below:
# # index=0
# # s= ""
# # while index < len(sounds):
# #     s += sounds[index].upper()
# #     index += 1

# # print(s)


# # ######################################################################################
# # Create a list called instructors
# instructors=[]
# # Add the following strings to the instructors list 
#     # "Colt"
#     # "Blue"
#     # "Lisa"
# instructors.extend(["Colt","Blue","Lisa"])

# # Remove the last value in the list
# instructors.pop()
# # Remove the first value in the list
# instructors.pop(0)
# # Add the string "Done" to the beginning of the list
# instructors.insert(0,"Done")
# # Run the tests to make sure you've done this correctly!
# print(instructors)
x=int(input())
y=int(input())
z=int(input())
n=int(input())

nos=[]
list_of_list=[]

# for i in range(x):
# 	for j in range(y):
# 		for k in range(z):
# 			nos=[i,j,k]
# 			list_of_list.append(nos)

# print(list_of_list)
# final_list=[nos for nos in list_of_list if nos[0] + nos[1] +nos[2] != n]
# print(f"The final list is \n{final_list}")


###############ALTERNATE FOR ABOVE 8 LINES
l=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
print(l)