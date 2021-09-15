sort	=	[]
for item in range(0,10):
	element=input(f"Enter the {item+1} element inside the list:	")
	element=int(element)
	sort.append(element)

print("Your unsorted list is :	")

print(sort)

for j in range(len(sort)):
	for i in range(0,len(sort)-1):
		if sort[i] > sort[i+1]:
			sort[i],sort[i+1]=sort[i+1],sort[i]

print("Thhe sorted list is :	")

print(sort)