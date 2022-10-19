#Program calculates sum: 5, 10, 15, .. 100.
#Use: for and while

sum1 = 0
for x in range(5,105,5):
	sum1 = sum1 +x
print (sum1)

y=5
sum2=0
while(y<=100):
	sum2 = sum2 +y
	y= y+5
print(sum2)
