#Program throws dice 100 times and tells amounts of different values (1, 
#2, 3, 4, 5, and 6).
import random

n1=n2=n3=n4=n5=n6=0

for x in range(100):
	y = random.randint(1,6)
	if y == 1:
		n1 += 1
	elif y ==2:
		n2 += 1
	elif y ==3:
		n3 += 1
	elif y ==4:
		n4 += 1
	elif y ==5:
		n5 +=1
	elif y ==6:
		n6 += 1
print("Amounts:")
print(f"number 1:{n1}")
print(f"number 2:{n2}")
print(f"number 3:{n3}")
print(f"number 4:{n4}")
print(f"number 5:{n5}")
print(f"number 6:{n6}")

