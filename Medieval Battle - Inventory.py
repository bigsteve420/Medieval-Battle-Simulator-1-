import time

class Inventory():
    def __init__(self):
        self.inventory = []

    def GetInventory(self):
        return self.inventory
    def GetInventoryItem(self,index):
        return self.inventory[index]
   
    def SetInventory(self,value):
        self.inventory = value
   
    def AddToInventory(self,item):
        self.inventory.append(item)

class Item():
    def __init__(self):
        self.itemID = "#1"
        self.name = "item_1"
        self.displayName = "Item 1"
        self.rarity = "common"
        self.type = "item"

    def GetID(self):
        return self.itemID
    def GetName(self):
        return self.name
    def GetDisplayName(self):
        return self.displayName
    def GetRarity(self):
        return self.rarity
    def GetType(self):
        return self.type

    def SetID(self,value):
        self.itemID = value
    def SetName(self,value):
        self.name = value
    def SetDisplayName(self,value):
        self.displayName = value
    def SetRarity(self,value):
        self.rarity = value
    def SetType(self,value):
        self.type = value

class Weapon(Item):
    def __init__(self):
        super().__init__()
        self.type = "weapon"
        self.weaponType = "special"
        self.canTargetAir = False
        self.canTargetGround = True
        self.accuracy = 50
        self.power = 20
        self.nickname = "Weapon"
   
    def GetWeaponType(self):
        return self.weaponType
    def GetCanTargetAir(self):
        return self.canTargetAir
    def GetCanTargetGround(self):
        return self.canTargetGround
    def GetAccuracy(self):
        return self.accuracy
    def GetPower(self):
        return self.power
    def GetNickname(self):
        return self.power

    def SetWeaponType(self, value):
        self.weaponType = value
    def SetCanTargetAir(self,value):
        self.canTargetAir = value
    def SetCanTargetGround(self,value):
        self.canTargetGround = value
    def SetAccuracy(self,value):
        self.accuracy = value
    def SetPower(self,value):
        self.power = value
    def SetNickname(self,value):
        self.power = value

class Magic(Item):
    def __init__(self):
        super().__init__()
        self.type = "magic"
        self.effects = [0,0,0,0,0,0,0,"ground",0]
        self.duration = "0/0/0/0/0/10"
        self.tempEffects = [0,0,0,0,0,0,0,"ground",0]

    def GetEffects(self):
        return self.effects
    def GetDuration(self):
        return self.duration
    def GetTempEffects(self):
        return self.tempEffects

    def SetEffects(self,value):
        self.effects = value
    def SetDuration(self,value):
        self.duration = value
    def SetTempEffects(self,value):
        self.tempEffects = value


def ExtractList(subject,length):
    extracted = []
    for i in range(1,length + 1):
        print(subject)
        j = 0
        while subject[j] != "/" and j<len(subject)-1:
            j += 1
        if (subject[0:j].isdigit()):
            extracted.append(int(subject[0:j]))
        else:
            extracted.append(subject[0:j])
        subject = subject[j+1:len(subject)]
    return extracted

itemIndex = []
itemIndexFile = open("itemIndex.txt","r")
reading = True
itemInfo = itemIndexFile.readline()
while reading == True:
    print(itemInfo)
    commaLocations = []
    for i in range(len(itemInfo)):
        if itemInfo[i] == ",":
            commaLocations.append(i)
    print(commaLocations)
    itemType = itemInfo[commaLocations[3]+1:commaLocations[4]]
    if (itemType == "weapon"):#sets weapon only attributes
        item = Weapon()
        item.SetWeaponType(itemInfo[commaLocations[4]+1:commaLocations[5]])
        item.SetCanTargetAir(itemInfo[commaLocations[5]+1:commaLocations[6]])
        item.SetCanTargetGround(itemInfo[commaLocations[6]+1:commaLocations[7]])
        item.SetAccuracy(int(itemInfo[commaLocations[7]+1:commaLocations[8]]))
        item.SetPower(int(itemInfo[commaLocations[8]+1:commaLocations[9]]))
        item.SetNickname(itemInfo[commaLocations[9]+1:commaLocations[10]])
        
    elif (itemType == "magic"): # sets magic only attributes
        item = Magic()
        item.SetDuration(itemInfo[commaLocations[5]+1:commaLocations[6]])
        for x in range(1,3):
            if x == 1:
                subject = itemInfo[commaLocations[4]+1:commaLocations[5]]
                length = 9
            elif x == 2:
                subject = itemInfo[commaLocations[5]+1:commaLocations[6]]
                length = 6
            else:
                subject = itemInfo[commaLocations[6]+1:commaLocations[7]]
                length = 9
            extracted = ExtractList(subject,length)

            if x == 1:
                item.SetEffects(extracted)
            elif x == 2:
                item.SetDuration(extracted)
            else:
                item.SetTempEffects(extracted)
             
    else: #sets universal attributes
        item = Item()
    print(itemType)
    item.SetID(itemInfo[0:commaLocations[0]])
    item.SetName(itemInfo[commaLocations[0]+1:commaLocations[1]])
    item.SetDisplayName(itemInfo[commaLocations[1]+1:commaLocations[2]])
    item.SetRarity(itemInfo[commaLocations[2]+1:commaLocations[3]])

    itemIndex.append(item)




    itemInfo = itemIndexFile.readline()

    if itemInfo == "":
        reading = False
##
##print(itemIndex[0].GetID(),itemIndex[0].GetName(),itemIndex[0].GetType())
##print(itemIndex[0].GetEffects())
##print(itemIndex[0].GetDuration())
##print(itemIndex[0].GetTempEffects())
##
##print(itemIndex[1].GetID(),itemIndex[0].GetName(),itemIndex[0].GetType())
##print(itemIndex[1].GetWeaponType())
##print(itemIndex[1].GetAccuracy())
##print(itemIndex[1].GetPower())

for i in range(len(itemIndex)):
    print(itemIndex[i].GetID(),itemIndex[i].GetName(),itemIndex[i].GetRarity(),itemIndex[i].GetType())
    if (itemIndex[i].GetType() == "weapon"):
        print(itemIndex[i].GetWeaponType(),itemIndex[i].GetAccuracy(),itemIndex[i].GetPower(),itemIndex[i].GetCanTargetAir(),itemIndex[i].GetCanTargetGround())
    elif (itemIndex[i].GetType() == "magic"):
        print(itemIndex[i].GetEffects(),itemIndex[i].GetDuration(),itemIndex[i].GetTempEffects())














