#Variables a, b and c have different values. Create a program that finds the biggest one. 
def find_max_one(a,b,c):
	if a>b:
		if b>=c:
			return a
		else:
			if a>=c:
				return a
			else:
				return c
	elif a<=b:
		if b<=c:
			return c
		else:
			return b

def find_max_two(a,b,c):
	max=a
	if max<b:
		max=b
		if max<c:
			max=c
	return max

def find_max_three(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	else:
		return c 


a=int(input("Enter a: "))	
b=int(input("Enter b: "))	
c=int(input("Enter c: "))

res1 = find_max_one(a,b,c)
print("Result of maximun number is {}".format(res1))
res2 = find_max_two(a,b,c)
print("Result of maximun number is {}".format(res2))
res3 = find_max_three(a,b,c)
print("Result of maximun number is {}".format(res3))

	
				
				
				
		
		
	 


