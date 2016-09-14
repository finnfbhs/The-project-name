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
        
        saveidlist = []
        cursor = con.cursor()
        saverow = cursor.execute("SELECT SaveID from Save")
        for row in saverow:
            savehold = row[0]
            saveidlist.append(savehold)        
        
        cursor = con.execute("SELECT SaveID,Name from Save")
        for row in cursor:
            print(row[0],row[1])
        time.sleep(1)
        answer = int(input("To create a new save enter '0', to load a save enter the save number, to delete a save enter '-1'."))
        
        if answer == 0:
            hold = 1
            newSave()
        
        elif answer == -1:
            print(" ")
            time.sleep(1)
            holdtwo = 1
            while holdtwo = 1:
                answer = input("Are you sure? (yes/no)")
                if answer.lower() == "yes":
                    deleteSave()
                    holdtwo = 0
                elif answer.lower() == "no":
                    print(" ")
                    holdtwo = 0
                else:
                    print(" ")
                    print("Invalid command. Enter yes or no.")
        
        elif answer in saveidlist:
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
        
        else:
            print(" ")
            print("{0} is not a valid input, please follow the instructions.".format(answer))

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
    
    print(" ")
    ID = int(input("What save would you like to delete? (Enter the save number)"))
    cursor = con.cursor()
    cursor.execute("DELETE FROM Save where SaveID = {0}".format(ID))
    con.commit()
    print(" ")
    print("Save {0} deleted successfully".format(ID))

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

def combat():
    global lifeforce
    
    enemy = enemyStatGen()
    enemyLifeForce = enemy[1]
    enemyDamage = enemy[2]
    print(" ")
    print("A {0} leaps out at you. Time to fight!".format(enemy[0]))
    print(" ")
    live = 1
    while live == 1:
        print("{0} Life Force = {1}       {2} Life Force = {3}".format(name, lifeforce, enemy[0], enemyLifeForce))
        var = 1
        while var == 1:
            command = input("What are you going to do? (type help for a list of battle commands)")
            if command.lower() == "attack":
                hitluck = random.randint(1,5)
                if hitluck != 1:
                    enemyLifeForce = enemyLifeForce - weapon[2]
                    print("Attack Hit! Enemy took {0} damage!".format(weapon[2]))
                    var = 0
                    if enemyLifeForce <= 0:
                        win(enemy)
                        live = 0
                    else:
                        print(" ")
                else:
                    print("Attack Missed!")
                    var = 0
            elif command.lower() == "flee":
                runluck = random.randint(1,5)
                if runluck == 1 or runluck == 2 or runluck == 3:
                    print("Got away safely!")
                    var = 0
                else:
                    print("You were chased and could not escape!")
                    var = 0
            else:
                print("Invalid command")
        if live != 0:
            enemyluck = random.randint(1,4)
            if enemyluck != 1:
                lifeforce = lifeforce - enemyDamage
                print("You have been hit! You took {0} damage.".format(enemyDamage))
                if lifeforce <= 0:
                    death()
                    live = 0
                else:
                    print(" ")
            else:
                print("Enemy attack missed!")

def death():
    print("You have lost too much blood, your life force has been depleted!")
    time.sleep(1)
    print("You are losing vision")
    time.sleep(1)
    print("You fall to the floor and see a figure walk towards you.")
    time.sleep(1)
    print("Your vision fades...")
    
    lifeforce = 10
    weapon = [1, "Scalpel", 5]
    armour = [1, "Ripped Lab Coat", 4]
    
    cursor = con.cursor()
    cursor.execute("UPDATE Save SET Weapon = 1, Armour = 1, LifeForce = 10 WHERE SaveID= ?",(saveID))
    
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
    print("You lost your weapons and armour!")
    time.sleep(3)
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")
    time.sleep(3)
    print("You need to find a way out!")
    time.sleep(3)      

def win(enemy):
    enemyName = enemy[0]
    global weapon
    global armour
    
    prize = dropGen()
    drop = prize[0]
    decider = prize[1]
    
    print("You killed the {0}!".format(enemyName))
    print("They dropped a {0}".format(drop[1]))
    if decider == 1:
        var = 1
        while var == 1:
            answer = input("Would you like to replace your {0}: Defense = {1} with the {2}: Defense = {3}? (yes/no)".format(armour[1], armour[2], drop[1], drop[2]))
            if answer.lower() == "yes":
                armour = [drop[0], drop[1], drop[2]]
                cursor = con.cursor()
                cursor.execute("UPDATE Save SET Armour = ? WHERE SaveID= ?",(drop[0], saveID))
                con.commit()
                print("You throw away your old armour and replaced with a new one! Armour updated")
                var = 0
            elif answer.lower() == "no":
                print("You decide to keep your current armour.")
                var = 0
            else:
                print("Invalid command. Enter yes or no.")
    else:
        var = 1
        while var == 1:
            answer = input("Would you like to replace your {0}: Damage = {1} with the {2}: Damage = {3}? (yes/no)".format(weapon[1], weapon[2], drop[1], drop[2]))
            if answer.lower() == "yes":
                weapon = [drop[0], drop[1], drop[2]]
                cursor = con.cursor()
                cursor.execute("UPDATE Save SET Weapon = ? WHERE SaveID= ?",(drop[0], saveID))
                con.commit()
                print("You throw away your old weapon and replaced with a new one! Weapon updated")
                var = 0
            elif answer.lower() == "no":
                print("You decide to keep your current weapon.")
                var = 0
            else:
                print("Invalid command. Enter yes or no.")

def enemyStatGen():
    randEnemy = random.randint(1,5)
    
    cursor = con.cursor()
    vari = cursor.execute("SELECT * from EnemyGen WHERE desID = {0}".format(randEnemy))
    for row in vari:
        enemyDes = row[1]
    
    enemyLifeForce = random.randint(1,10)
    enemyDamage = random.randint(1,3)
    
    enemy = (enemyDes, enemyLifeForce, enemyDamage)
    
    return enemy

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
    
    parcel = (droplist, decider)
    return parcel

def roomGen():
    randNumber = random.randint(1,15)

    cursor = con.cursor()
    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))
    for row in var:
        roomDes = row[1]
    
    return roomDes

def rest():
    global lifeforce
    lifeforce = 10
    print("You take a nap for a few minutes..")
    time.sleep(5)
    print("Lifeforce has been replenished.")
    print("Lifeforce = {0}".format(lifeforce))
    time.sleep(3)
    print("You wake up and you feel someone watching you so you exit the room")

def checkStats():
    print("Name = {0}".format(name))
    print("Lifeforce = {0}".format(lifeforce))
    print("Weapon = {0}, Damage = {1}".format(weapon[1],weapon[2]))
    print("Armour = {0}, Defense = {1}".format(armour[1],armour[2]))
    time.sleep(3)
    print(" ")
    print("You didn't realize but you kept walking as you were checking your statistics so you've exited your other room.")

def help():
    print("List of commands:")
    print(" ")
    time.sleep(1)
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

#def final():

def main():
    print("Plexed")
    print(" ")
    time.sleep(3)
    loading()
    variable = 1
    while variable == 1:
        roomDes = roomGen()
        print(" ")
        print("You come into {0}".format(roomDes))
        print(" ")
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