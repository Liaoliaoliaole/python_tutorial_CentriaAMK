#Returns the average of 2 integers
def avrgOfTwo(a,b):
	avrg = (a+b)/2
	return avrg
print(avrgOfTwo(5,6))
print(avrgOfTwo(5.0,6.0))
#Returns the average of 4 floating point values.
def avrgOfFour(a,b,c,d):
	avrg = (a+b+c+d)/4
	return avrg
print(avrgOfFour(5,6,7,8))
print(avrgOfFour(5.0,6.0,7.0,8.0))
#Returns the sum of an  array.
def sumOfArr(arr):
	sum=0
	for i in range(len(arr)):
		sum+=arr[i]
	return sum
a=[1,2,1,2,1,2,1,2]
print(sumOfArr(a))
#Returns the factorial.
def factorial(n):
	if n==1 or n==0:
		return 1
	elif n>0:
		return n*factorial(n-1)
	else:
		return "Invalid parameter"
print(factorial(1))
print(factorial(5))
print(factorial(0))
print(factorial(-3))
#print(factorial('Hello'))

