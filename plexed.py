#Plexed
#Created by Finn Foubister 17/08/2016
#This is a game designed for NCEA level 2 standards assessment

import sqlite3
import random
import time
con = sqlite3.connect('database.db')

def loading():
    hold = 0
    while hold == 0:
        global name
        global weapon
        global armour
        global lifeforce
        global saveID
        
        print("Saves:")
        time.sleep(1)
        cursor = con.execute("SELECT SaveID,Name from Save")
        for row in cursor:
            print(row[0],row[1])
        answer = int(input("To create a new save enter '0', to load a save enter the save number, to delete a save enter '-1'."))
        
        if answer == 0:
            hold = 1
            newSave()
        
        elif answer == -1:
            answer = input("Are you sure? (yes/no)")
            if answer == "yes":
                deleteSave()
        
        else:
            hold = 1
            saveID = answer
            
            cursor = con.execute("SELECT Name from Save where SaveID = {0}".format(answer))
            for row in cursor:
                name = row[0]
            print("Name = {0}".format(name))
            time.sleep(1)
            
            cursor = con.execute("SELECT LifeForce from Save where SaveID = {0}".format(answer))
            for row in cursor:
                lifeforce = row[0]
            print("Lifeforce = {0}".format(lifeforce))
            time.sleep(1)
            
            cursor = con.execute("SELECT Weapon from Save where SaveID = {0}".format(answer))
            for row in cursor:
                weaponID = row[0]
                weaponcur = con.execute("SELECT * from Weapons where ID = {0}".format(weaponID))
                for row in weaponcur:
                    weapon = [row[0],row[1],row[2]]
            print("Weapon = {0}".format(weapon[1]))
            time.sleep(1)
            
            cursor = con.execute("SELECT Armour from Save where SaveID = {0}".format(answer))
            for row in cursor:
                armourID = row[0]
                armourcur = con.execute("SELECT * from Armours where ID = {0}".format(armourID))
                for row in armourcur:
                    armour = [row[0],row[1],row[2]]
            print("Armour = {0}".format(armour[1]))
            time.sleep(3)

def newSave():
    global name
    global weapon
    global armour
    global lifeforce
    global saveID
    
    name = input("What is your name?")
    details = (name,1,1,10)

    cursor = con.cursor()
    cursor.execute("INSERT INTO Save(Name,Weapon,Armour,LifeForce) VALUES (?,?,?,?)",details)
    con.commit()
    
    savelist = []
    cursor = con.cursor()
    saveids = cursor.execute("SELECT SaveID from Save")
    for row in saveids:
        saveidhold = row[0]
        savelist.append(saveidhold)
    saveID = max(savelist)
    
    lifeforce = 10
    weapon = [1, "Scalpel", 5]
    armour = [1, "Ripped Lab Coat", 4]
    
    time.sleep(2)
    print("You wake up. Everything is very hazy.")
    time.sleep(3)
    print("Regaining vision you see that you're in some kind of medical room.")
    time.sleep(3)
    print("You see an empty syringe on the ground next to you labelled HALLUCINOGENS")
    time.sleep(3)
    print("Looking at your arm you see needle holes. You've been given hallucinogens!")
    time.sleep(3)
    print("These may affect the world around you. Rooms you have just came out of may have changed.")
    time.sleep(3)
    print("Things are hard to see and nothing makes sense.")
    time.sleep(3)
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")
    time.sleep(3)
    print("You need to find a way out!")
    time.sleep(3)    

def saving():
    weaponID = weapon[0]
    armourID = armour[0]
    
    cursor = con.cursor()
    cursor.execute("UPDATE Save SET Weapon = ?, Armour = ?, LifeForce = ? WHERE SaveID= ?",(weaponID, armourID, lifeforce, saveID))
    con.commit()
    
    print("Game saved successfully")

def deleteSave():
    print("Saves:")
    cursor = con.execute("SELECT SaveID,Name from Save")
    for row in cursor:
        print(row[0],row[1])
    
    ID = int(input("What save would you like to delete? (Enter the save number)"))
    cursor = con.cursor()
    cursor.execute("DELETE FROM Save where SaveID = {0}".format(ID))
    con.commit()
    print("Save {0} deleted successfully".format(ID))

#def final():
    

#def combat():
    

def roomGen():
    randNumber = random.randint(1,30)

    cursor = con.cursor()
    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))
    for row in var:
        roomDes = row[1]
    
    return roomDes

#def enemyStatGen():
    

def dropGen():
    randNumber = random.randint(1,10)
    decider = random.randint(1,2)
    
    if decider == 1:
        cursor = con.cursor()
        var = cursor.execute("SELECT * from Armours where ID = {0}".format(randNumber))
        for row in var:
            droplist = (row[0],row[1],row[2])
    
    else:
        cursor = con.cursor()
        var = cursor.execute("SELECT * from Weapons where ID = {0}".format(randNumber))
        for row in var:
            droplist = [row[0],row[1],row[2]]
    
    return droplist

def rest():
    global lifeforce
    lifeforce = 10
    print("You take a nap for a few minutes..")
    time.sleep(5)
    print("Lifeforce has been replenished.")
    print("Lifeforce = {0}".format(lifeforce))
    time.sleep(3)
    print("You wake up and you feel someone watching you so you exit the room")
    time.sleep(4)

def checkStats():
    print("Name = {0}".format(name))
    print("Lifeforce = {0}".format(lifeforce))
    print("Weapon = {0}, Damage = {1}".format(weapon[1],weapon[2]))
    print("Armour = {0}, Defense = {1}".format(armour[1],armour[2]))
    time.sleep(3)
    print("You didn't realize but you kept walking as you were checking your statistics so you've exited your other room.")
    time.sleep(2)

def help():
    print("List of commands:")
    time.sleep(1)
    print(" ")
    print("Explore")
    time.sleep(1)
    print("Attack")
    time.sleep(1)
    print("Rest")
    time.sleep(1)
    print("Checkstats")
    time.sleep(1)
    print("Save")
    time.sleep(1)
    print(" ")
    time.sleep(3)
    print("In your search for inner help you have walked into another room.")
    time.sleep(2)

def main():
    print("Plexed")
    time.sleep(3)
    loading()
    var = 1
    while var == 1:
        roomDes = roomGen()
        print("You come into {0}".format(roomDes))
        time.sleep(3)
        ans = input("What would you like to do? (type help for a list of commands)")
        if ans.lower() == "explore":
            print("You exit the room.")
            time.sleep(3)
            
        elif ans.lower() == "attack":
            combat()
            time.sleep(3)
            
        elif ans.lower() == "rest":
            rest()
            time.sleep(3)
            
        elif ans.lower() == "checkstats":
            checkStats()
            time.sleep(3)
            
        elif ans.lower() == "save":
            saving()
            time.sleep(3)
            
        elif ans.lower() == "help":
            help()
            time.sleep(3)
        
        else:
            print("Not a valid command; type help for a list of commands")
            time.sleep(3)

main()