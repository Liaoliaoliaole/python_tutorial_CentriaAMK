#1. A complex number is a number that can be expressed in the form a + bi,
# where a and b are real numbers and i is the imaginary unit.
#Create class Complex with attributes, constructors and getters/setters.

class Complex:
	def __init__(self,real,imag):
		self.real = real
		self.imag = imag

	def getComplexNumber(self):
		if(self.imag > 0):
			ComplexNum = str(self.real) + "+" + str(self.imag) + "i"
		elif(self.imag == 0):
			ComplexNum = str(self.real)
		else:
			ComplexNum = str(self.real) + "-" + str(self.imag*(-1)) + "i"
		return ComplexNum

	def setComplexNumber(self,real,imag):
		self.real = real
		self.imag = imag


num1 = Complex(1,2)
num2 = Complex(2,0)
num3 = Complex(-3,-4.5)
print (num1.getComplexNumber())
print (num2.getComplexNumber())
print (num3.getComplexNumber())
num3.setComplexNumber(3,6)
print (num3.getComplexNumber())

