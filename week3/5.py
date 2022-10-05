#User gives the lengths of the triangle's sides. Program tells what is the triangle like

def triangleType_by_angle(x, y, z):
    a = pow(x, 2)
    b = pow(y, 2)
    c = pow(z, 2)
    if (a == c+b or b == a+c or c == a+b):
        print("Right angled triangle")
    elif (a > c+b or b> a+c or c > a+b):
        print("Obtuse angled triangle")
    else:
        print("Acute angled triangle")

print("Enter the lengths of the triangle sides: ")
x = int(input("side x: "))
y = int(input("side y: "))
z = int(input("side z: "))

if x+y>=z and y+z>=x and z+x>=y:
	if x == y == z:
		print("Equilateral triangle")	
	elif x==y or y==z or z==x:
		print("isosceles triangle")
		triangleType_by_angle(x,y,z)
	else:
		print("Scalene triangle")
		triangleType_by_angle(x,y,z)
else:
	print("Tringle is not possible from given sides.")




