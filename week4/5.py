#Account manager with menu:
#User can make deposits
#Do withdrawal
#Check the balance

amount = float(input("Input your amount of savings: "))
round(amount,2)
while True:
	c = int(input("Choose 2 to make a deposit/Choose 1 to withdrawal/Choose 0 to quit the program: "))
	if (c==1):
		w=float(input("Input the amount you want to whithdrawal: "))
		round(w,2)
		if w<=amount:
			amount = amount-w
			print(f"Your amount is : {round(amount,2)}")
			continue
		else:
			print("Invalid withdrawal amount!")
			continue
	elif(c==2):
		d = float(input("Input your amount of deposite: "))
		round(d,2)
		amount = amount + d
		print(f"Your amount is : {amount}")
		continue
	elif(c==0):
		break


