#Group has 3 members (note:  aggregation)

class Member:
    def __init__(self, name, number):
        self.name = name
        self.number = number


    def getMemberInfo(self):
        print(f"Name: {str(self.name)}: Member number: {str(self.number)}")


class Group:
    def __init__(self, groupName):
        self.groupName = groupName
        self.memberList = []


    def addMember(self, name):
        self.memberList.append(name)


    def getGroupInfo(self):
        print("=" * 30)
        print(self.groupName)
        print("=" * 30)
        for i in self.memberList:
            i.getMemberInfo()

#data

m1 = Member("Jone", "22001")
m2 = Member("Ben", "22002")
m3 = Member("Gina", "22003")

g1 = Group("Bannana")

g1.addMember(m1)
g1.addMember(m2)
g1.addMember(m3)

#show 
print(g1.getGroupInfo())