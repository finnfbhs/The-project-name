#Plexed
#Created by Finn Foubister 17/08/2016
#This is a game designed for NCEA level 2 standards assessment

import sqlite3
import random
import time
con = sqlite3.connect('database.db')

def loading():
    print("0 Create new save")
    print("Saves:")
    cursor = con.execute("SELECT SaveID,Name from Save")
    for row in cursor:
        print(row[0],row[1])
    answer = int(input("What save would you like to load?(type the number)"))
    
    if answer == 0:
        newSave()
        
    else:
        cursor = con.execute("SELECT Name from Save where SaveID = {0}".format(answer))
        for row in cursor:
            name = row[0]
        print("Name = {0}".format(name))
        
        cursor = con.execute("SELECT Weapon from Save where SaveID = {0}".format(answer))
        for row in cursor:
            weaponID = row[0]
            weaponcur = con.execute("SELECT * from Weapons where ID = {0}".format(weaponID))
            for row in weaponcur:
                weapon = [row[0],row[1],row[2]]
        print("Weapon = {0}".format(weapon[1]))
        
        cursor = con.execute("SELECT Armour from Save where SaveID = {0}".format(answer))
        for row in cursor:
            armourID = row[0]
            armourcur = con.execute("SELECT * from Armours where ID = {0}".format(armourID))
            for row in armourcur:
                armour = [row[0],row[1],row[2]]
        print("Armour = {0}".format(armour[1]))

def newSave():
    name = input("What is your name?")
    details = (name,1,1)

    cursor = con.cursor()
    cursor.execute("INSERT INTO Save(Name,Weapon,Armour) VALUES (?,?,?)",details)
    con.commit()
    
    weapon = [1, "Scalpel", 5]
    armour = [1, "Ripped Lab Coat", 4]
    
    print("You wake up. Everything is very hazy.")
    time.sleep(3)
    print("Regaining vision you see that you're in some kind of medical room.")
    time.sleep(3)
    print("You see an empty syringe on the ground next to you labelled HALLUCINOGENS")
    time.sleep(3)
    print("Looking at your arm you see needle holes. You've been given hallucinogens!")
    time.sleep(3)
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")
    time.sleep(3)
    print("You need to find a way out!")
    time.sleep(3)    

def saving():
    weaponID = weapon[0]
    armourID = armour[0]
    
    cursor = con.cursor()
    cursor.execute("UPDATE Save SET Weapon = ?, Armour = ? WHERE SaveID= ?",(weaponID, armourID, saveID))
    con.commit()   

def final():
    print("")

#def combat():
    

def roomGen():
    randNumber = random.randint(1,30)

    cursor = con.cursor()
    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))
    for row in var:
        roomDes = row[1]
    return roomDes

#def enemyStatGen():
    

#def dropGen():
    

#def rest():
    

#def checkStats():


def main():
    loading()
    

main()