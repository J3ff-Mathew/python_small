shopping_cart=[]
while True:
	shopping_items=input("Enter thr product name to the cart or press 'q' to exit:  ")
	
	if shopping_items.lower() == "q":
		break
	shopping_cart.append(shopping_items) 

print(f"there are {len(shopping_cart)} items on your cart")
n=1
for items in shopping_cart :
	print(f"item {n}: {items}")
	n += 1

 
print("Thanks for shopping with us!!!!!")