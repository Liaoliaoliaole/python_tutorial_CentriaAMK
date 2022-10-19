from collections import deque
a = [1,2,3,4,5,6,7,8]
print(a)
a.insert(2, 9)
print("Array after inserting 9 is", a)
a.append(10)
print (a)
a.remove(1)
print(a)
a.pop(a[0])
print(a)
print(a.index(4))
print(a.count(9))
a.sort()
print(a)
a.reverse()
print(a)
a.append(10)
a.pop()
print(a)
del a[0]
print(a)
del a[2:4]
print(a)

b=deque(a)
b.append(6)
b.append(7)
print(b.popleft())
print(b.popleft())
#del b
#print(b)
triple=[]
for x in range(5):
	triple.append(x**3)
print(triple)
triple = list(map(lambda x: x**3,range(5)))
print(triple)
triple = [x**3 for x in range(5)]
print(triple)

print([(x, y) for x in [6,7,8] for y in [5,6,7] if x != y])

c =[-9,-6,-3,0,3,6,9]
print([x**2 for x in c])
print([x for x in c if x>0])
print([abs(x) for x in c if x<0])

d=[(x,x*10) for x in range(2,9)]
print(d)

e=[[1,3],[2,4],[5,7],[6,8]]
print([num for elem in e for num in elem])

m=[
  	[1,3,5,7,9],
	[2,4,6,8,10],
	[0,0,0,0,0],
  ]
t1=[[row[i] for row in m] for i in range(len(m[0]))]
print(m)
print(t1)
t2=[]
for i in range(len(m[0])):
	t2.append([row[i] for row in m])
print(t2)
t3=[]
for i in range(5):
	t3_row=[]
	for row in m:
		t3_row.append(row[i])
	t3.append(t3_row)
print(t3)

t=1357,2468,'test'
print(t[2])
print(t)
tu=t,t,('works')
print(tu)

s1={1,1,2,2,3,4,5,6,7,8,9}
print(s1)
print(2 in s1)
print(10 in s1)
s2=set('a1b2c3d4')
s3=set('abcd')
print(s2)
print(s3)
print(s2-s3)
print(s2|s3)
print(s2&s3)
print(s2^s3)

