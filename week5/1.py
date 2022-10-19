#1.Array contains 30 random values. Calculate the sum and average.
#2.Find the maximun of the array.
#Search a value from an array.

import random
#generate array of random value between 0-100
values = []
for i in range(30):
	values.append(random.randint(0,100))

for i in range(30):
	print(values[i],end=",")
print("\r")
# calculate sum and average
sum=0
avrg=0
for i in range(30):
	sum += values[i]
print(f"sum: {sum}")
avrg = sum/30
print(f"average: {avrg}")
#find max in an array
max = values[0]
for i in range(1,30):
	if values[i] > max:
		max = values[i]
print("The maximum value is ",max)
#search 100 in this array
toBeFound=100
r = "Not found"
for i in range(1,30):
	if values[i] == toBeFound:
		r="found in position ",i;
		break;
print(r)
