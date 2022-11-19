#House with 3 Rooms (note:  composition)

class House:
    def __init__(self,owner):
        self.owner = owner
        self.rooms = []
        self.price = 0

    def addRoom(self,name,roomArea):
        r = Room(name,roomArea)
        self.rooms.append(r)
        return r

    def getPrice(self):
        p=0
        for i in self.rooms:
            p += i.roomArea * 3000
        return p
    
    def getHouseInfo(self):
        print("=" * 30)
        for i in self.rooms:
            print(i.getRoomInfo())
        print("+" *30)
        print(f"{self.owner} 's house is {str(self.getPrice())} euros")
    
class Room:
    def __init__(self,name,roomArea):
        self.name = name
        self.roomArea = roomArea
    
    def getRoomInfo(self):
        return self.name + " is " + str(self.roomArea) + " square meters."

#data
h1 = House("Lili")
h1.addRoom("Livingroom",15)
h1.addRoom("Bedroom",10)
h1.addRoom("studyroom",7)

h2 = House("Lucy")
h2.addRoom("Livingroom",15)
h2.addRoom("Bedroom",12)

#show
h1.getHouseInfo()
h2.getHouseInfo()

