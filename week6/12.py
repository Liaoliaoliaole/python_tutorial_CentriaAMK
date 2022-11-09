def factr(n):
	if n==1 or n==0:
		return 1
	elif n>0:
		return n*factr(n-1)
	else:
		return "Invalid parameter"
#Calculates an approximation of Neper's value (e).
def Neper(k):
	e=0
	for k in range(0,k+1):
			e+=1/factr(k)
	return e
print(Neper(10))
# Calculates  approximations of sin(x) and cos(x)
def sin(x):
	res=0.0
	pow=3
	while pow < 100:
		res -= x**pow/factr(pow)
		pow += 2
		res += x**pow/factr(pow)
		pow += 2
		if x**pow/factr(pow)<0.0001:
			break
	return x+res
print(sin(10))
print(sin(30))
print(sin(5))
def cos(x):
	res=0.0
	pow=2
	while pow<100:
		res -=x**pow/factr(pow)
		pow+=2
		res+=x**pow/factr(pow)
		pow+=2
		if x**pow/factr(pow)< 0.0001:
			break
	return 1+res
print(cos(10))
print(cos(30))
print(cos(2))
