#Dungeons and dragons

import csv
import random 
from statistics import mean
import json
from collections import defaultdict
from tabulate import tabulate
import tkinter as tk 
import logging


def loadTables():
    loadClass()
    loadRace()
    loadWeapon()
    loadGear()
    loadBarbarian()
    loadBard()

def loadClass():
    #Load palyer class data from JSON
    # Opening JSON file
    f = open('PlayerClass.json',)
    # returns JSON object as a dictionary
    data = json.load(f)
    global playerClass 
    for i in data['player_class_details']:
        playerClass[(i['player_class'])] = i
       # Closing file
    f.close()
    return(playerClass)
    
def loadRace():
    #load race data from JSON 
    # Opening JSON file
    try:
        f = open('Race.json',)
    except IOError:
        print("Error: can't find file or read data")
    
    # returns JSON object as a dictionary
    data = json.load(f)
    global Race 
    for i in data['race_details']:
        Race[(i['Race'])] = i
    # Closing file
    f.close()
    
def loadWeapon():    
    #Loads weapon Dictionary from JSON
    #----------------------------------------------------------------------------
    # Opening JSON file
    f = open('weapon.json',)
    # returns JSON object as a dictionary
    data = json.load(f)
    global Weapon 
    for i in data['weapon_details']:
        Weapon[(i['weapon'])] = i
    # Closing file
    f.close()

def loadGear():
    #load gear data from JSON
    # Opening JSON file
    f = open('gear.json',)
    # returns JSON object as a dictionary
    data = json.load(f)
    global Gear 
    for i in data['gear_details']:
        Gear[(i['Item'])] = i
    # Closing file
    f.close()

def loadBarbarian():
    #load barbarian data from JSON
    # Opening JSON file
    f = open('barbarian.json',)
    # returns JSON object as a dictionary 
    data = json.load(f)
    global Barbarian 
    for i in data['barbarian_details']:
        Barbarian[(i['Level'])] = i
    # Closing file
    f.close()

def loadBard():
    #load Bard data from JSON
    # Opening JSON file
    f = open('bard.json',)
    # returns JSON object as a dictionary
    data = json.load(f)
    global Bard 
    for i in data['bard_details']:
        Bard[(i['Level'])] = i
    # Closing file
    f.close()

def d(side):
    #roll die. side is the number of sides on the dice
    try:
        return random.randrange(1, side + 1)
    except:
        logging.warning("input not > 0")
        

def RollStats():
    #Rolls stats. 4 6 sided dice for each stat, subtracting the lowest dice roll. returns 6 stats.
    stat = []
    stats = []
    for x in range(6):
        for y in range(4):
            stat.append(d(6))
        stats.append(sum(stat)-min(stat))
        stat.clear()
    stats.sort(reverse=True)
    return stats

#Displays class data so player can choose player class
def DisplayCharacterRace():
    racelist=[]
    for key in Race:
        racelist.append(Race[key])

    race_attributes = []
    for key in (Race['Human']):
        race_attributes.append(key)

    print(race_attributes)
    print(tabulate(racelist))

#Select player race
def SelectCharacterRace():
    lstRaces = []
    for i in Race:
        lstRaces.append(i)
    print(lstRaces)
    test = True
    while test == True:
        race = input("Enter Race from the list: ")
        print(race.capitalize())
        if race.capitalize() in lstRaces:
            return race.capitalize()
        else:
            print("There is no {} character race. try again.".format(race))
            test == False

#Selects player race
def DisplayCharacterClasses():
    

    pclist = []
    for key in playerClass:
        pclist.append(playerClass[key])

    pc_attributes = []
    for key in (playerClass['Bard']):
        pc_attributes.append(key)
    print(pclist)
    print(pc_attributes)
    print(tabulate(pclist))

#Stores character data in PlayerCharacter class
class PlayerCharacter:
#PlayerCharacter class variables    
    stats=[]
    race = []
    occupation = ""
    chrClass=""
    hitDie = 0
    level = 0
    str = 0
    mstr = 0
    dex = 0
    mdex = 0
    con = 0
    mcon = 0
    wis = 0
    mwis = 0
    intel = 0
    mintel = 0
    cha = 0
    mcha = 0
    hpBase = 0
    hpBonus = 0
    AC = 0
    DarkVision = 0
    speed = 0
    inventory = []
    weapons = []
    armor = []
    height = 0
    weight = 0
    gpcurrency = 0
    totalHP = 0
    #initalize player character with Name
    def __init__(self, name):
        self.name = name

  #Creates the character, calling class, race, other updatesto class variables, and prints character attributes
    def myfunc(self):
        DisplayCharacterClasses()
        self.updateClass()
        self.updateCharacterStats()
        
        print("My stats are strength {}, dexterity {}, constitution {}, wisdom {}, intelligence {}, and charisma {}.".format(
            self.str, self.dex, self.con, self.wis, self.intel, self.cha))
        swap = input("Want to swap to stats? (Y/N): ")
        while swap.capitalize() == "Y":
            self.requestSwapStats()
            print("My stats are strength {}, dexterity {}, constitution {}, wisdom {}, intelligence {}, and charisma {}.".format(
                self.str, self.dex, self.con, self.wis, self.intel, self.cha))
            swap = input("Swap more? (Y/N): ")

        self.updateRace()
        self. updateModifiers()
        self.updatehpBonus()
        self.totalHP = self.hpBase +self.hpBonus
        
        print("My stats are strength {}, dexterity {}, constitution {}, wisdom {}, intelligence {}, and charisma {}.".format(
            self.str, self.dex, self.con, self.wis, self.intel, self.cha))
        
        print("{} is a {} {} with Dark Vision to {} feet and speed of {} feet per round and am {} inches tall and I weigh {} pounds with a {} sided hit die and {} hit points".format(
           self.name, self.race, self.occupation, self.DarkVision, self.speed, self.height, self.weight, self.hitDie, self.totalHP))
        print("I have {} g.p. to start with.".format(self.gpcurrency))
        
    #Player Selects character class from list of classes (occupations because class is a reserved word)
    @classmethod
    def updateClass(cls):
        #Sets occupation
        lstClasses = []
        for i in playerClass:
            lstClasses.append(i)
        print(lstClasses)
        test = True
        while test == True:
            chrClass = input("Enter Class from the list: ")
            if chrClass.capitalize() in lstClasses:
                cls.occupation = chrClass.capitalize()
                test=False
            else:
                print("There is no {} character class. try again.".format(chrClass))
                test == True
                
        print("You picked {}.".format(cls.occupation))
        #sets stats to 0
        stats=[0]
        #generates stats until you get an average stat 13 or above     
        while mean(stats) < 13:
            stats = RollStats()
        cls.stats = stats

    #Select race and apply racial modifications    
    @classmethod
    def updateRace(cls):
        DisplayCharacterRace()
        cls.race=SelectCharacterRace()
        cls.updateStr(cls.str + (Race[cls.race]['strBonus']))
        cls.updateDex(cls.dex + (Race[cls.race]['dexBonus']))
        cls.updateCon(cls.con + (Race[cls.race]['conBonus']))
        cls.updateInt(cls.intel + (Race[cls.race]['intBonus']))
        cls.updateWis(cls.wis + (Race[cls.race]['wisBonus']))
        cls.updateCha(cls.cha + (Race[cls.race]['chaBonus']))
        cls.updateDarkVision((Race[cls.race]['DarkVision']))
        cls.updateSpeed((Race[cls.race]['speed']))
        cls.updateHeight((Race[cls.race]['height']))
        cls.updateWeight((Race[cls.race]['weight']))
   
    #Set stats
    @classmethod 
    def updateCharacterStats(cls):
        
        cls.level = 1
        if cls.occupation == "Barbarian":
            cls.str = cls.stats[0]
            cls.dex = cls.stats[2]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[3]
            cls.wis = cls.stats[4]
            cls.intel = cls.stats[5]
 
        elif cls.occupation == "Bard":
            cls.str = cls.stats[4]
            cls.dex = cls.stats[1]
            cls.con = cls.stats[3]
            cls.cha = cls.stats[0]
            cls.wis = cls.stats[2]
            cls.intel = cls.stats[5]
            cls.hpBase = 8
        elif cls.occupation == "Cleric":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[3]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[4]
            cls.wis = cls.stats[0]
            cls.intel = cls.stats[5]
            cls.hpBase = 8
        elif cls.occupation == "Druid":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[4]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[5]
            cls.wis = cls.stats[0]
            cls.intel = cls.stats[3]
            cls.hpBase = 8
        elif cls.occupation == "Fighter":
            cls.str = cls.stats[0]
            cls.dex = cls.stats[1]
            cls.con = cls.stats[2]
            cls.cha = cls.stats[3]
            cls.wis = cls.stats[4]
            cls.intel = cls.stats[5]
            cls.hpBase = 10
        elif cls.occupation == "Monk":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[0]
            cls.con = cls.stats[3]
            cls.cha = cls.stats[4]
            cls.wis = cls.stats[1]
            cls.intel = cls.stats[5]
            cls.hpBase = 8
        elif cls.occupation == "Paladin":
            cls.str = cls.stats[0]
            cls.dex = cls.stats[3]
            cls.con = cls.stats[2]
            cls.cha = cls.stats[1]
            cls.wis = cls.stats[4]
            cls.intel = cls.stats[5]
            cls.hpBase = 10
        elif cls.occupation == "Ranger":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[0]
            cls.con = cls.stats[3]
            cls.cha = cls.stats[4]
            cls.wis = cls.stats[1]
            cls.intel = cls.stats[5]
            cls.hpBase = 10
        elif cls.occupation == "Rogue":
            cls.str = cls.stats[3]
            cls.dex = cls.stats[0]
            cls.con = cls.stats[2]
            cls.cha = cls.stats[4]
            cls.wis = cls.stats[5]
            cls.intel = cls.stats[1] 
            cls.hpBase = 8
        elif cls.occupation == "Sorcerer":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[4]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[0]
            cls.wis = cls.stats[5]
            cls.intel = cls.stats[3]
            cls.hpBase = 6
        elif cls.occupation == "Warlock":
            cls.str = cls.stats[2]
            cls.dex = cls.stats[4]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[0]
            cls.wis = cls.stats[5]
            cls.intel = cls.stats[3]
            cls.hpBase = 8
        elif cls.occupation == "Wizard":
            cls.str = cls.stats[4]
            cls.dex = cls.stats[2]
            cls.con = cls.stats[1]
            cls.cha = cls.stats[5]
            cls.wis = cls.stats[3]
            cls.intel = cls.stats[0]
            cls.hpBase = 6
        else:
            print("No such character")

        cls.hpBase = (playerClass[cls.occupation]['hit dice'])
        cls.hitDie = (playerClass[cls.occupation]['hit dice'])
        cls.calcFunds()

#Set stats
    @classmethod
    def requestSwapStats(cls):
        print("Stats are --1. Strength {} --2. Deterity {} --3. Constituion {} --4. Intelligence {} --5.Wisdon {} --6. Charisma {} ".format(cls.str,cls.dex,cls.con,cls.intel,cls.wis,cls.cha))
        stat1 = input("Select number of first stat to swap: ")
        if stat1 == "1":
            temp = cls.str
            name = "str"
        elif stat1 == "2":
            temp = cls.dex 
            name = "dex"
        elif stat1 == "3":
            temp = cls.con 
            name ="con"
        elif stat1 =="4":
            temp = cls.intel 
            name ="intel"
        elif stat1 == "5":
            temp = cls.wis 
            name ="wis"
        elif stat1 == "6":
            temp = cls.cha 
            name ="cha"
        else:
            print("No such stat as {}.".format(stat1))

        stat2 = input("Select number of second stat to swap: ")
        if stat2 == "1":
            temp1 = cls.str
            cls.str = temp
            setattr(cls,name,temp1)
        elif stat2 == "2":
            temp1 = cls.dex
            cls.dex = temp
            setattr(cls,name,temp1)
            
        elif stat2 == "3":
            temp1 = cls.con
            cls.con = temp
            setattr(cls,name,temp1)
        elif stat2 == "4":
            temp1 = cls.intel
            cls.intel = temp
            setattr(cls,name,temp1)
        elif stat2 == "5":
            temp1 = cls.wis
            cls.wis = temp
            setattr(cls, name, temp1)
        elif stat2 == "6":
            temp1 = cls.cha
            cls.cha = temp
            setattr(cls, name, temp1)
        else:
            print("No such stat as {}.".format(stat1))

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateStr(cls,value ):
        cls.str = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateDex(cls,value ):
        cls.dex = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateCon(cls,value ):
        cls.con = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateWis(cls,value ):
        cls.wis = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateInt(cls,value ):
        cls.intel = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updateCha(cls,value ):
        cls.cha = value

    #updates stat by adding value to stat (initially 0)
    @classmethod
    def updatehpBase(cls, value):
        cls.hpBase += value

    #updates DarkVision whether by race or other modifier by adding to initial value
    @classmethod
    def updateDarkVision(cls, value):
        cls.DarkVision = value

    #updates speed whether by race or other modifier by adding to initial value
    @classmethod
    def updateSpeed(cls, value):
        cls.speed += value

    #updates height whether by race or other modifier by adding to initial value
    @classmethod
    def updateHeight(cls, value):
        h1 = value.split( )
        base = int(h1[0])
        multiplier = int(h1[2])
        adj =  d(int(h1[4]))
        cls.height =base + (adj * multiplier)
    
    #updates weight whether by race or other modifier by adding to initial value
    @classmethod
    def updateWeight(cls, value):
        h1 = value.split()
        #print("weight data")
        #print(int(h1[0]), int(h1[2]), int(h1[4]))
        base = int(h1[0])
        multiplier = int(h1[2])
        adj = d(int(h1[4]))
        #print(int(h1[0]), int(h1[2]), int(h1[4]), adj)
        cls.weight = base + (adj * multiplier)

    #updates weight whether by race or other modifier by adding to initial value
    @classmethod
    def updatehpBonus(cls,valuse):
        hpBonus = (cls.con - 10) /2
        cls.hpBonus = int(hpBonus * cls.level)

    @classmethod
    def calcFunds(cls):
        money = playerClass[cls.occupation]['starting_wealth'].split(" ")
        gp = 0
        for x in range(int(money[0])):
            gp = gp + d(int(money[2]))
        gp = gp * int(money[4])
        cls.gpcurrency = gp

    @classmethod
    def updateModifiers(cls):
        cls.mstr = int((cls.str - 10) / 2)
        cls.mdex = int((cls.dex - 10) / 2)
        cls.mcon = int((cls.con - 10) / 2)
        cls.mwis = int((cls.wis - 10) / 2)
        cls.mintel = int((cls.intel - 10) / 2)
        cls.mcha = int((cls.cha - 10) / 2)

    @classmethod
    def updatehpBonus(cls):
        cls.hpBonus = cls.level * cls.mcon

playerClass = {}

Race = {}
Weapon = {}
Gear = {}
Armor = {}
Bard = {}
Barbarian = {}
racelist = []
loadTables()
print(Race)

name = input("enter a name for your characater: ")
p1 = PlayerCharacter(name)
p1.name = name
p1.myfunc()
'''
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def createPlayer():
    p1 = PlayerCharacter(name.get())
    p1.name = name.get()
    #p1.myfunc()

def viewPlayerClass():

tkvar = "Fighter"
master = tk.Tk()
tk.Label(master, text="Enter your character's name").grid(row=0)
tk.Label(master, text="Select a class").grid(row=1)

name = tk.Entry(master)
playerClss = tk.Entry(master)

playerClss = tk.OptionMenu(master,tkvar,*playerClass)
name.grid(row=0, column=1)
playerClss.grid(row=1, column=1)

tk.Button(master,text='Quit',command=master.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(master, text='Enter', command=createPlayer).grid(row=0, column=2, sticky=tk.W, pady=4)
tk.Button(master, text='Enter', command=createPlayer).grid(row=1, column=2, sticky=tk.W, pady=4)
tk.mainloop()
'''
