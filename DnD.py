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

def DisplayClass():
    plist = {}
    x = 1
    for key in playerClass:
        plist[x] = key
        x = x+1
    #print(playerClass)
    print('{:9}    {:2}'.format('Class', 'Hit dice'))
    for key in playerClass:
        print("{:9}      {:2}  {}".format(
            playerClass[key]['player_class'], playerClass[key]['hit dice'], playerClass[key]['description']))
    print(plist)
    

def SelectClass():
    DisplayClass()
    playerClass = input("Enter number of selected class: ")
    if playerClass == "1":
        pclass = 'Barbarian'
    elif playerClass == "2":
        pclass = 'Bard'
    elif playerClass == "3":
        pclass = 'Cleric'
    elif playerClass == "4":
        pclass = 'Druid'
    elif playerClass == "5":
        pclass = 'Fighter'
    elif playerClass == "6":
        pclass = 'Monk'
    elif playerClass == "7":
        pclass = 'Paladin'
    elif playerClass == "8":
        pclass = 'Ranger'
    elif playerClass == "9":
        pclass = 'Rogue'
    elif playerClass == "10":
        pclass = 'Sorcerer'
    elif playerClass == "11":
        pclass = 'Warlock'
    elif playerClass == "12":
        pclass = 'Wizard'
    else:
        print("Invalid Number")    
        
    
    return(pclass)



class PlayerCharacter:
    name = ""
    stats = [0]
    playerClass =''
    #initalize player character with Name
    def __init__(self, name):
        self.name = name
        while mean(self.stats) < 13:
            self.stats = RollStats()
        self.playerClass=SelectClass()
        



Weapon = {}
Race = {}
playerClass = {}
Gear = {}
Barbarian = {}
Bard= {}
loadTables()
p1 = PlayerCharacter('Matt')
print(p1.stats)
print(p1.playerClass)

    
