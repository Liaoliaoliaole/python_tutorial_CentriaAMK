#Program calculates the factorial of n (given in a variable)

f=1
n = int(input("give your number to calculate factorial of n: "))
if n<0:
	print("Error! Factorial of a negative number doesn't exist.")
elif n==0:
	f=1
	print(f"zero factorial is:{f}")
else:
	for i in range(1,n+1):
		f *= i
	print(f"Factorial of {n} = {f}")
