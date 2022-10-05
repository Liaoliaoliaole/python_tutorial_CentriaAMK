#User gives a month number and our program tells the number of days in that month.
x=int(input("Enter your month number: "))
if x>0 and x<=12:
	if x==4 or x==6 or x==9 or x==11:
		print("30 days in this month")
	elif x==2:
		print("28 or 29 days in this month")
	else:
		print("31 days in this month")
else:
	print("Invalid input")
		
