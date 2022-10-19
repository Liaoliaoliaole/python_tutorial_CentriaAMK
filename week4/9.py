#Program calculates the exponential value (base and exponent are 
#given in variable). Base can be a real number, exponent is a whole number. 
#Use a loop.

r=1
k=1

base = float(input("Entre your base number: "))
exp = int(input("Enter your exponent number: "))
if exp > 0:
	for x in range(1,exp+1):
		r *= base
	print(r)
elif exp == 0:
	print("1")
else:
	for y in range (1,(exp-1)*(-1)):
		k *= base
	r = 1/k
	print(r) 
