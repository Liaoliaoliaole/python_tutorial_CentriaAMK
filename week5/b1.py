#There are 20 values in an array:calculate the standard deviation
#use simple formular

import random
import math

arr=[]
sum=0
for i in range(20):
	arr.append(random.randint(1,100))
	sum += arr[i]
print(arr)

m_x=sum/len(arr)
s=0
for x in arr:
	s+=(x-m_x)**2
sd=math.sqrt(s/(len(arr)-1))
print(sd) 











print("\r")


