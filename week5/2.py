#Fill 2 arrays with some values and calculate the sum array.

import random

arr1 = []
arr2 = []
sumArr = []

for i in range(5):
	arr1.append(random.randint(0,10))
for i in range(len(arr1)):
	print(arr1[i],end=" ")
print("\r")
for i in range(5):
	arr2.append(random.randint(1,10))
for i in range(len(arr2)):
	print(arr2[i],end=" ")
print("\r")

for i in range(len(arr1)):
	sumArr.append(arr1[i] + arr2[i])
	print(sumArr[i],end=" ")
print("\r")
