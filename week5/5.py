#Generate a lottorow  (try to use an array here).
#Lottery number mathematics: https://en.wikipedia.org/wiki/Lottery_mathematics.
#In a typical 6/49 game, user chooses six distinct numbers from a range of 1-49. 
#Rrogram gives the  numbers on user's selection match the numbers drawn by the lottery

import random
#get user number
userNum=[]
while len(userNum)<6:
	num = int(input("Choose your number between 1 and 49: "))
	if num >=1 and num <=49:
		if num not in userNum:
			userNum.append(num)
		else:
			print("You have chosen this number already!")
	else:
		print("Invalid number choise!")
userNum.sort()
for i in range(len(userNum)):
	print(userNum[i],end=" ")
print("\r")
#generate lottorow
lotto =[]
lotto.append(random.randint(1,49))
x=0
while len(lotto)<6:
	x=random.randint(1,49)
	if x not in lotto:
		lotto.append(x)
lotto.sort()
for i in range(len(lotto)):
	print(lotto[i],end=" ")
print("\r")
#check user number and lotto number 
if userNum == lotto:
	print("Now you are millionare!")
else:
	print("Sorry you lost")


