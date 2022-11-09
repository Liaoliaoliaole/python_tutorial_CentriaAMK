#Calculates amount of combinations (try to use also an own factorial function here).
def factr(n):
	if n==1 or n==0:
		return 1
	elif n>0:
		return n*factr(n-1)
	else:
		return "Invalid parameter"
def comb(n,k):
	return factr(n)/factr(k)/factr(n-k)
print(comb(3,2))
print(comb(3,3))
print(comb(2,1))
print(comb(1,0))
#Calculates the standard deviation.
import math
def standardDeviation(arr):
	sum=0
	for i in range(len(arr)):
		sum += arr[i]
	m_x=sum/len(arr)
	s=0
	for x in arr:
		s+=(x-m_x)**2
	sd=math.sqrt(s/(len(arr)-1))
	return sd 
arr=[1,3,5,7,9,11]
print(standardDeviation(arr))
