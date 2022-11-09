#Returns the biggest of 3 integers.
def find_max_three(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	else:
		return c 
print(find_max_three(9,-5,0))
#Returns the BMI.
def BMI(height,weight):
	BMI = weight/pow((height/100),2)
	print(f"You BMI is {BMI}")
	if BMI <= 18.4:
		print("You are underweight.")
	elif BMI <= 24.9:
		print("You are healthy.")
	elif BMI <= 29.9:
		print("You are over weight.")
	else:
		print("You are severely over weight.")
BMI(170,70)
#Function returns the biggest of 5 integers.
def find_max_five(a,b,c,d,e):
	arr = [a,b,c,d,e]
	max=arr[0]
	for i in range(len(arr)):
		if max<arr[i]:
			max=arr[i]
	return max
print(find_max_five(1,8,4,90,-8))
