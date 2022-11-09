#Searches for a value from an array.
def find(arr,value):
	c=0
	index=[]
	for i in range(len(arr)):
		if arr[i]==value:
			c += 1
			index.append(i)
	if c>0:
		print(f"Value {value} is at position of {index}.")
	else:
		print("Not found.")
arr1=[1,3,1,3,5,6]
arr2=[0,8,6,5,43,1]
find(arr1,1)
find(arr2,4)
#Calculates the square root of value 2 (create your own function).
def mySqrt(n):
	if n<1 or n>4:
		print("I'll figure out later...")
	else:
		for x in range(1,2):
			if x*x==n:
				return x
			else:
				while True:
					if x*x-n>-0.001 and x*x-n < 0.001:
						break
					x+=0.001
				return x
print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(4))
print(mySqrt(5))
