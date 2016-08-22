#Plexed
#Created by Finn Foubister 17/08/2016
#This is a game designed for NCEA level 2 standards assessment

import sqlite3
import random
con = sqlite3.connect('database.db')

def loading():
    cursor = con.execute("SELECT Name from Save")
    for row in cursor:
        name = row[0]
    print(name)
    
    cursor = con.execute("SELECT Weapon from Save")
    for row in cursor:
        weaponID = row[0]
        weaponcur = con.execute("SELECT * from Weapons where ID = {0}".format(weaponID))
        for row in weaponcur:
            weapon = [row[0],row[1],row[2]]
    print(weapon)
    
    cursor = con.execute("SELECT Armour from Save")
    for row in cursor:
        armourID = row[0]
        armourcur = con.execute("SELECT * from Armours where ID = {0}".format(armourID))
        for row in armourcur:
            armour = [row[0],row[1],row[2]]
    print(armour)

#def saving():
    

#def introduction():
    

#def final():
    

#def combat():
    

#def roomGen():
    

#def enemyStatGen():
    

#def dropGen():
    

#def rest():
    

def main():
    loading()

main()