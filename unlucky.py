
for x in range(1,21):
	if x==4 or x==13:
		STATE = " UNLUCKY"
	elif x%2==0:
		STATE = " EVEN"
	else:
		STATE = " ODD"
	print(f"{x} is {STATE}")