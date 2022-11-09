#Migratory has special features: 
#there is attribute named country that is the destination
#country and month when the migration mainly occurs.
#Country name has to begin with a cap and its length has to be between 5 to 20. 
#Month has to be between 1 and 12.

class Country:
	def __init__(self,countryName,cap):
		self.country = countryName
		if len(cap) in range(5,12,1):
			self.capital = cap
	
	def getCountry(self):
		return self.country

	def getCapital(self):
		return self.capital

class Migratory:

	def __init__(self,dstCountry,destCapital,mon):
		self.destinationCountry = dstCountry
		self.destinationCapital = destCapital
		if mon in range(1,12,1):
			self.month = mon
		else:
			raise ValueError('month number out of range: {}'.format(self.month))

	def getMigratoryInfo(self):
		print("Migratory to " + self.destinationCountry + "whose capital city is " + self.destinationCapital + " ,usually happens in " + str(self.month))


mycountry = Country("Finland","Helsinki")
c = mycountry.getCountry()
cp = mycountry.getCapital()
m = Migratory(c,cp,11)
m.getMigratoryInfo()

