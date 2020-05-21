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
    loadLanguages()

def loadClass():
    #Load palyer class data from JSON
    # Opening JSON file
    try:
        f = open('PlayerClass.json',)
    except IOError as err:
        print("Error: ", err)
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
    except IOError as err:
        print("Error: ", err)
    # returns JSON object as a dictionary
    data = json.load(f)
    global Race
    for i in data['race_details']:
        Race[(i['Race'])] = i
    # Closing file
    f.close()
    return(Race)

def loadWeapon():
    #Loads weapon Dictionary from JSON
    #----------------------------------------------------------------------------
    # Opening JSON file
    try:
        f = open('weapon.json',)
    except IOError as err:
        print("Error: ", err)
    
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
    try:
        f = open('gear.json',)
    except IOError as err:
        print("Error: ", err)
    
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
    try:
        f = open('barbarian.json',)
    except IOError as err:
        print("Error: ", err)
    
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
    try:
        f = open('bard.json',)
    except IOError as err:
        print("Error: ",err)
    
    # returns JSON object as a dictionary
    data = json.load(f)
    global Bard 
    for i in data['bard_details']:
        Bard[(i['Level'])] = i
    # Closing file
    f.close()
    
def loadLanguages():
    #load languages data from JSON
    # Opening JSON file
    try:
        f = open('languages.json',)
    except IOError as err:
        print("Error: ", err)

    # returns JSON object as a dictionary
    data = json.load(f)
    
    global Languages
    for i in data['languages']:
        Languages[(i['language'])] = i
    # Closing file
    f.close()

def d(side):
    #roll die. side is the number of sides on the dice
    try:
        return random.randrange(1, side + 1)
    except:
        logging.warning("input not > 0")

def SelectLanguage(langs):
    l1=''
    print(Languages.keys())
    while l1 not in Languages.keys():
        l1 = input('Select a language from the list: ').capitalize()
    return (l1)

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
class PlayerCharacter:
    name = ""
    stats = [0]
    pClass =''
    hitdice = 0
    str = 0
    dex = 0 
    con = 0       
    cha = 0 
    wis = 0
    intel = 0
    hpBase = 0
    speed = 0
    DarkVision = 0
    height = 0
    weight = 0
    langauges = []
    #initalize player character with Name
    def __init__(self, name):
        self.name = name
        while mean(self.stats) < 13 or mean(self.stats) > 15:
            self.stats = RollStats()
        self.pClass = self.SelectClass()
        self.updateClass()
        self.pRace = self.SelectRace()
        self.UpdateStats()
        self.UpdateRaceFeatures()
    def SelectClass(self):
        self.DisplayClass()
        pClass = ''
        while pClass not in (playerClass.keys()):
            pClass = input("Enter selected class: ").capitalize()
        return(pClass)

    def DisplayClass(self):
        plist = {}
        x = 1
        for key in playerClass:
            plist[x] = key
            x = x+1
        print('{:9}    {:2}  {}'.format('Class', 'HD','Description'))
        for key in playerClass:
            print("{:9}    {:2}  {}".format(
                playerClass[key]['player_class'], playerClass[key]['hit dice'], playerClass[key]['description']))
        print(", ".join(playerClass))

    def updateClass(self):
        if self.pClass == "Barbarian":
            self.str = self.stats[0]
            self.dex = self.stats[2]
            self.con = self.stats[1]
            self.cha = self.stats[3]
            self.wis = self.stats[4]
            self.intel = self.stats[5]

        elif self.pClass == "Bard":
            self.str = self.stats[4]
            self.dex = self.stats[1]
            self.con = self.stats[3]
            self.cha = self.stats[0]
            self.wis = self.stats[2]
            self.intel = self.stats[5]
            self.hpBase = 8
        elif self.pClass == "Cleric":
            self.str = self.stats[2]
            self.dex = self.stats[3]
            self.con = self.stats[1]
            self.cha = self.stats[4]
            self.wis = self.stats[0]
            self.intel = self.stats[5]
            self.hpBase = 8
        elif self.pClass == "Druid":
            self.str = self.stats[2]
            self.dex = self.stats[4]
            self.con = self.stats[1]
            self.cha = self.stats[5]
            self.wis = self.stats[0]
            self.intel = self.stats[3]
            self.hpBase = 8
        elif self.pClass == "Fighter":
            self.str = self.stats[0]
            self.dex = self.stats[1]
            self.con = self.stats[2]
            self.cha = self.stats[3]
            self.wis = self.stats[4]
            self.intel = self.stats[5]
            self.hpBase = 10
        elif self.pClass == "Monk":
            self.str = self.stats[2]
            self.dex = self.stats[0]
            self.con = self.stats[3]
            self.cha = self.stats[4]
            self.wis = self.stats[1]
            self.intel = self.stats[5]
            self.hpBase = 8
        elif self.pClass == "Paladin":
            self.str = self.stats[0]
            self.dex = self.stats[3]
            self.con = self.stats[2]
            self.cha = self.stats[1]
            self.wis = self.stats[4]
            self.intel = self.stats[5]
            self.hpBase = 10
        elif self.pClass == "Ranger":
            self.str = self.stats[2]
            self.dex = self.stats[0]
            self.con = self.stats[3]
            self.cha = self.stats[4]
            self.wis = self.stats[1]
            self.intel = self.stats[5]
            self.hpBase = 10
        elif self.pClass == "Rogue":
            self.str = self.stats[3]
            self.dex = self.stats[0]
            self.con = self.stats[2]
            self.cha = self.stats[4]
            self.wis = self.stats[5]
            self.intel = self.stats[1]
            self.hpBase = 8
        elif self.pClass == "Sorcerer":
            self.str = self.stats[2]
            self.dex = self.stats[4]
            self.con = self.stats[1]
            self.cha = self.stats[0]
            self.wis = self.stats[5]
            self.intel = self.stats[3]
            self.hpBase = 6
        elif self.pClass == "Warlock":
            self.str = self.stats[2]
            self.dex = self.stats[4]
            self.con = self.stats[1]
            self.cha = self.stats[0]
            self.wis = self.stats[5]
            self.intel = self.stats[3]
            self.hpBase = 8
        elif self.pClass == "Wizard":
            self.str = self.stats[4]
            self.dex = self.stats[2]
            self.con = self.stats[1]
            self.cha = self.stats[5]
            self.wis = self.stats[3]
            self.intel = self.stats[0]
            self.hpBase = 6
        else:
            print("No such character")

        self.hitdice = (playerClass[self.pClass]['hit dice'])
        
    def displayRace(self):
        print('{:9}    {:2} '.format('Race',  'Description'))
        for key in Race:
            print("{:9}    {:2} ".format(
                Race[key]['Race'],  Race[key]['description']))
        print('-------------------------------------------------------------------------------------------------------------')
        print(", ".join(Race))

    def SelectRace(self):
        self.displayRace()
        pRace = ''
        while pRace not in (Race.keys()):
            pRace = input("Select Race from list: ").capitalize()
        return(pRace)

    def UpdateStats(self):
        self.str = self.str +(Race[self.pRace]['strBonus'])
        self.dex = self.dex +(Race[self.pRace]['dexBonus'])
        self.wis = self.wis +(Race[self.pRace]['wisBonus'])
        self.con = self.con +(Race[self.pRace]['conBonus'])
        self.intel = self.intel +(Race[self.pRace]['intBonus'])
        self.cha = self.cha + (Race[self.pRace]['chaBonus'])
    def UpdateLanguages(self):
        l1 = (Race[self.pRace]["languages"]).split(';')
        print(l1)

        for item in l1:
            if item == "+1":
                print("Selecting language")
                self.langauges.append(SelectLanguage(self.langauges))
            else:
                self.langauges.append(item)

    def UpdateRaceFeatures(self):
        #calc height
        h1 = (Race[self.pRace]['height']).split()
        self.height = (int(h1[0]) + int(h1[2]) * d(int(h1[4])))
        #calc weight
        w1 = (Race[self.pRace]['weight']).split()
        self.weight = (int(w1[0]) + int(w1[2]) * d(int(w1[4])))
        #calc age
        a1 = (Race[self.pRace]["age"]).split()
        self.age = (int(a1[0]) + int(a1[2]) * d(int(a1[4])))
        
        self.speed = (Race[self.pRace]["speed"])
        self.DarkVision = (Race[self.pRace]["DarkVision"])
        wp1 = (Race[self.pRace]["weaponproficiency"])
        sa1 = (Race[self.pRace]["specialAbilities"])
        self.UpdateLanguages()
        t1 = (Race[self.pRace]["toolProficiency"])
        sp1 = (Race[self.pRace]["special proficiency"])
  
#-----------------------------------------------------------------------------------------------
Languages={}
Weapon = {}
Race = {}
playerClass = {}
Gear = {}
Barbarian = {}
Bard= {}
loadTables()
p1 = PlayerCharacter('Matt')
print('{} is a {} {} with {}-sided hit dice.'.format(p1.name,p1.pRace,p1.pClass,p1.hitdice))
print('{} has {} strength, {} dexterity, {} wisdom, {} constitution, {} intelligence, {} charisma'.format(p1.name,p1.str, p1.dex, p1.wis, p1.con,p1.intel,p1.cha))
print('I can see {} feet in the dark and run {} feet per turn.'.format(p1.DarkVision,p1.speed))
print('{} is {} years old, {} inches tall and weigh {} pounds.'.format(p1.name,p1.age, p1.height, p1.weight))
print('{} speaks {} .'.format(p1.name, p1.langauges))
print(p1.stats)








    
