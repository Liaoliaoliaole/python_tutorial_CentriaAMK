#2 arrays contain students grades in math and in English language.
#There are 10 students. Try to calculate the correlation. 

import math

m = [90,65,85,70,90,95,60,75,80,100]
e = [60,90,85,90,85,90,80,80,70,95]

sum_m=sum(m)
sum_e=sum(e)
n=10
m_m=float(sum_m/n)
e_m=float(sum_e/n)

sum_max=sum_min=m_p=e_p=0
for i in range(n):
	sum_max += (m[i]-m_m)*(e[i]-e_m)
print(sum_max)
for i in range(n):
	m_p += math.pow((m[i]-m_m),2)
print(m_p)
for i in range(n):
	e_p += math.pow((e[i]-e_m),2)
print(e_p)
sum_min=math.sqrt(m_p*e_p)
print(sum_min)
c=sum_max/sum_min
print(c)




