list_of_names=[]

list_of_items	=	[]

list_of_items_list = []

response = 'a'

while response.lower() != 'q':

	name_of_list	=	input("Enter the name of the list\n")

	list_of_names.append(name_of_list)

	while True:
		item=input("Enter an item into the list or press 'q' to quit: ")

		if item.lower()=='q':
			break

		list_of_items.append(item)


	print(f" Items present in list {name_of_list} are :- ")

	for items in list_of_items:
		print(items)

	list_of_items_list.append(list_of_items)
	list_of_items=[]

	response=input(" press q to quit or press anyother key to create another list \n")

print("Here is the list and the items inthe lists:-")
n=0
for li in list_of_names:
	print(li)
	while  len(list_of_items_list) > n :
		print(list_of_items_list[n])
		break
	n +=1


print("Thanks for using our service:")
