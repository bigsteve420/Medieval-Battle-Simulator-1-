import time
import random

class World():
    def __init__(self):
        self.day = 1
        self.weather = "nice"
        self.temperature = "mild"
   
    def GetDay(self):
        return self.day
    def GetWeather(self):
        return self.weather
    def GetTemperature(self):
        return self.temperature

    def SetDay(self,value):
        self.day = value
    def SetWeather(self,value):
        self.weather = value
    def SetTemperature(self,value):
        self.temperature = value
   
    def ChangeDay(self,value):
        self.day += value
   

class BaseStats():
    def __init__(self):
        self.characterClass = "peasant"

        self.strength = 0
        self.speed = 0
        self.magic = 0
       
        self.hitpointsmax = 100
        self.hitpoints = self.hitpointsmax
        self.energymax = 100
        self.energy = self.energymax

        self.airStatus = "ground"

   
    def GetCharacterClass(self):
        return self.characterClass    
    def GetStrength(self):
        return self.strength
    def GetSpeed(self):
        return self.speed
    def GetMagic(self):
        return self.magic
    def GetHitpoints(self):
        return self.hitpoints
    def GetMaxHitpoints(self):
        return self.hitpointsmax
    def GetEnergy(self):
        return self.hitpoints
    def GetMaxEnergy(self):
        return self.hitpointsmax

    def SetCharacterClass(self,value):
        self.characterClass = value
    def SetStrength(self,value):
        self.strength = value
    def SetSpeed(self,value):
        self.speed = value
    def SetMagic(self,value):
        self.magic = value
    def SetHitpoints(self,value):
        self.hitpoints = value
    def SetMaxHitpoints(self,value):
        self.hitpointsmax = value
    def SetEnergy(self,value):
        self.hitpoints = value
    def SetMaxEnergy(self,value):
        self.hitpointsmax = value

    def ChangeCharacterClass(self,value):
        self.characterClass += value
    def ChangeStrength(self,value):
        self.strength += value
    def ChangeSpeed(self,value):
        self.speed += value
    def ChangeMagic(self,value):
        self.magic += value
    def ChangeHitpoints(self,value):
        self.hitpoints += value
    def ChangeMaxHitpoints(self,value):
        self.hitpointsmax += value
    def ChangeEnergy(self,value):
        self.hitpoints += value
    def ChangeMaxEnergy(self,value):
        self.hitpointsmax += value


    #Move to seperate classes.  e.g class WarriorStat extends Stats()
    def AssignClassWarrior(self):
        self.SetCharacterClass("warrior")
        self.SetStrength(15)
        self.SetSpeed(10)
        self.SetMagic(5)
    def AssignClassMage(self):
        self.SetCharacterClass("mage")
        self.SetStrength(5)
        self.SetSpeed(10)
        self.SetMagic(15)
    def AssignClassThief(self):
        self.SetCharacterClass("thief")
        self.SetStrength(10)
        self.SetSpeed(15)
        self.SetMagic(5)
    def AssignClassGod(self):
        self.SetCharacterClass("god")
        self.SetStrength(100)
        self.SetSpeed(100)
        self.SetMagic(100)

class SecondaryStats():
    def __init__(self):
        self.damageReduction = 0

class Inventory():
    def __init__(self):
        self.inventory = []

    def GetInventory(self):
        return self.inventory
   
    def SetInventory(self,value):
        self.inventory = value
   
    def AddToInventory(self,item):
        self.inventory.append(item)

class Player():
    def __init__(self):
        self.stats = BaseStats()
        self.inventory = Inventory()

class Item():
    def __init__(self):
        self.rarity = "common"
        self.type = "item"
        self.name = "item1"
        self.itemID = "#1"
   
    def GetRarity(self):
        return self.rarity
    def GetType(self):
        return self.type
    def GetName(self):
        return self.name
    def SetRarity(self,value):
        self.rarity = value
    def SetType(self,value):
        self.type = value
    def SetName(self,value):
        self.name = value

class Weapon(Item):
    def __init__(self):
        super().__init__(self)
        self.type  = "weapon"
        self.weaponType = "special"
        self.canTargetAir = False
        self.canTargetGround = True
        self.accuracy = 50
        self.power = 20
   
    def GetCanTargetAir(self):
        return self.canTargetAir
    def GetCanTargetGround(self):
        return self.canTargetGround
    def GetAccuracy(self):
        return self.accuracy
    def GetPower(self):
        return self.power

   
    def SetCanTargetAir(self,value):
        self.canTargetAir = value
    def SetCanTargetGround(self,value):
        self.canTargetGround = value
    def SetAccuracy(self,value):
        self.accuracy = value
    def SetPower(self,value):
        self.power = value
       
world = World()
player_1 = Player()


def RequestClass():
    print("choose a class")
    time.sleep(1)
    print("warrior")
    print("mage")
    print("thief")
    classes = str(input(""))
    if classes == "warrior":
        player_1.stats.AssignClassWarrior()
    elif classes == "mage":
        player_1.stats.AssignClassMage()
    elif classes == "thief":
        player_1.stats.AssignClassThief()
    elif classes == "god":
        player_1.stats.AssignClassGod()
    else:
        print("class set to 'peasant'")

def Train():
    trainingTime = 0
    continueTraining = True
    while (trainingTime <= 4 and continueTraining == True):


        print("what would you like to train")
        print("strength")
        print("speed")
        print("magic")
        print("anything else to exit training")
        training = str(input(""))
        if training == "strength":
            player_1.stats.ChangeStrength(1)
            print("your strengh is now,",player_1.stats.GetStrength())
        elif training == "speed":
            player_1.stats.ChangeSpeed(1)
            print("your speed is now,",player_1.stats.GetSpeed())
        elif training == "magic":
           player_1. stats.ChangeMagic(1)
           print("your magic is now,",player_1.stats.GetMagic())
        else:
            continueTraining = False
            print("training exited")
        trainingTime += 1




print("welcome to medieval battle simulator")
time.sleep(1)
name = str(input("choose a name for your character"))
RequestClass()

print("the beginning of your adventure")
playing = True

time.sleep(1)
#need a while loop to repeat this
while playing == True:
    print("day",world.GetDay())
    print(player_1.stats.GetStrength(),player_1.stats.GetSpeed(),player_1.stats.GetMagic())
    print("would you like to")
    print("sleep")
    print("train")
    print("explore")
    option = str(input(""))
    if option == "sleep":
        print("your hitpoints have been restored")
        player_1.stats.SetHitpoints(player_1.stats.GetMaxHitpoints())
    elif option == "train":
        Train()
    elif option == "explore":
        print("where do you want to explore")
        print("woods (recommended total stats, 20)")
        print("caves (recommended total stats, 100)")
        print("evil castle (recommended total stats, 225)")
        exploreOption = str(input(""))
        if exploreOption == "woods":
            woodsScenario = random.randint(1,5)
            if woodsScenario == "1" or "2" or "3":
                #goblin will have 20 strength 20 speed 10 magic
                print("there is a goblin (50 total stats)")
            elif woodsScenario == "4":
                print("you found a health shard")
            elif woodsScenario == "5":
                print("you found a chest")
                woodsLoot = random.randint(1,10)
                if woodsLoot == "1" or "2" or "3":
                    rarity = "common"
                    woodsLootType = random.randint(1,5)
                    if woodsLootType == "1" or "2" or "3":
                        weapon = "sword"
    world.ChangeDay(1)
    player_1.stats.SetEnergy(player_1.stats.GetMaxEnergy())
