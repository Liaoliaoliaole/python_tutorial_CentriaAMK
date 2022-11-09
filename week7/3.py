#3. Bird has features name and amount of eggs.
#Amount of eggs has to be between 1 and 10.

class Bird:
	def __init__(self,name):
		self.name = name
		self.egg = None

	def layEgg(self,Aegg):
		self.egg = Aegg

class Egg:
		def __init__(self, amount):
			if (amount >=1 and amount <= 10):
				self.amount = amount
			else:
				print("Oooops")

myBird1 = Bird("seagull")
myEggs1 = Egg(8)
myBird1.layEgg(myEggs1)
print(myBird1.egg.amount)

myEggs2 = Egg(12) #print ooooops
myBird1.layEgg(myEggs2)
print(myBird1.egg.amount) #AttributeError: 'Egg' object has no attribute 'amount'

