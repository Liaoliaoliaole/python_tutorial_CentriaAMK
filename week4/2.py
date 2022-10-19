#Program calculates the sum of even numbers between 2 - 40.
#Use: for and while

sum1 = 0
for x in range(2,41):
	if(x % 2 == 0):
		sum1 =sum1 +x
print('The sum of even number between 2-40：%d' % sum1)


y=2
sum2=0
while (y<=40):
	sum2 += y
	y = y+2

print('The sum of even number between 2-40：%d' % sum2)
