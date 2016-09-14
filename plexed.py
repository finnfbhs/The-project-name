#Plexed
#Created by Finn Foubister 17/08/2016
#This is a game designed for NCEA level 2 standards assessment

import sqlite3
import random
import time
con = sqlite3.connect('database.db')
cursor = con.cursor()

def loading():
    hold = 0
    while hold == 0:
        global cursor
        global name
        global weapon
        global armour
        global lifeforce
        global saveID
        
        print("Saves:")
        print(" ")
        time.sleep(1)
        
        saveidlist = []
        saverow = cursor.execute("SELECT SaveID from Save")
        for row in saverow:
            savehold = row[0]
            saveidlist.append(savehold)        
        
        curs = con.execute("SELECT SaveID,Name from Save")
        for row in curs:
            print(row[0],row[1])
        time.sleep(1)
        print(" ")
        answer = int(input("To create a new save enter '0', to load a save enter the save number, to delete a save enter '-1'."))
        
        if answer == 0:
            hold = 1
            newSave()
        
        elif answer == -1:
            print(" ")
            time.sleep(1)
            holdtwo = 1
            
            while holdtwo == 1:
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
                    time.sleep(1)
        
        elif answer in saveidlist:
            hold = 1
            saveID = answer
            
            cursor = con.execute("SELECT Name from Save where SaveID = {0}".format(answer))
            for row in cursor:
                name = row[0]
            print("Name = {0}".format(name))
            time.sleep(1)
            
            curs = con.execute("SELECT LifeForce from Save where SaveID = {0}".format(answer))
            for row in curs:
                lifeforce = row[0]
            print("Lifeforce = {0}".format(lifeforce))
            time.sleep(1)
            
            curs = con.execute("SELECT Weapon from Save where SaveID = {0}".format(answer))
            for row in curs:
                weaponID = row[0]
                weaponcur = con.execute("SELECT * from Weapons where ID = {0}".format(weaponID))
                for row in weaponcur:
                    weapon = [row[0],row[1],row[2]]
            print("Weapon = {0}".format(weapon[1]))
            time.sleep(1)
            
            curs = con.execute("SELECT Armour from Save where SaveID = {0}".format(answer))
            for row in curs:
                armourID = row[0]
                armourcur = con.execute("SELECT * from Armours where ID = {0}".format(armourID))
                for row in armourcur:
                    armour = [row[0],row[1],row[2]]
            print("Armour = {0}".format(armour[1]))
            time.sleep(3)
        
        else:
            time.sleep(1)
            print(" ")
            print("{0} is not a valid input, please follow the instructions.".format(answer))
            time.sleep(1)

def saving():
    global cursor
    
    weaponID = weapon[0]
    armourID = armour[0]
    
    cursor.execute("UPDATE Save SET Weapon = ?, Armour = ?, LifeForce = ? WHERE SaveID= ?",(weaponID, armourID, lifeforce, saveID))
    con.commit()
    
    print("Game saved successfully")

def deleteSave():
    global cursor
    
    time.sleep(1)
    print("Saves:")
    curs = con.execute("SELECT SaveID,Name from Save")
    for row in curs:
        print(row[0],row[1])
    
    time.sleep(1)
    print(" ")
    ID = int(input("What save would you like to delete? (Enter the save number)"))
    cursor.execute("DELETE FROM Save where SaveID = {0}".format(ID))
    con.commit()
    
    time.sleep(1)
    print(" ")
    print("Save {0} deleted successfully".format(ID))
    time.sleep(3)

def newSave():
    global name
    global weapon
    global armour
    global lifeforce
    global saveID
    global cursor
    
    time.sleep(1)
    print(" ")
    name = input("What is your name?")
    details = (name,1,1,10)

    cursor.execute("INSERT INTO Save(Name,Weapon,Armour,LifeForce) VALUES (?,?,?,?)",details)
    con.commit()
    
    savelist = []
    saveids = cursor.execute("SELECT SaveID from Save")
    for row in saveids:
        saveidhold = row[0]
        savelist.append(saveidhold)
    saveID = max(savelist)
    
    lifeforce = 25
    weapon = [1, "Scalpel", 5]
    armour = [1, "Ripped Lab Coat", 4]
    
    time.sleep(1)
    print(" ")
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
    time.sleep(1)
    print(" ")
    print("A {0} leaps out at you. Time to fight!".format(enemy[0]))
    print(" ")
    time.sleep(2)
    var = 1
    
    while var == 1:
        print("{0} Life Force = {1}       {2} Life Force = {3}".format(name, lifeforce, enemy[0], enemyLifeForce))
        print(" ")            
        time.sleep(2)
        command = input("What are you going to do? (type help for a list of battle commands)")
            
        if command.lower() == "attack":
            hitluck = random.randint(1,5)
                
            if hitluck != 1:
                enemyLifeForce = enemyLifeForce - weapon[2]
                time.sleep(1)
                print(" ")
                print("Attack Hit! Enemy took {0} damage!".format(weapon[2]))
                
                if enemyLifeForce <= 0:
                    win(enemy)
                    var = 0
                    
                else:
                    time.sleep(1)
                    print(" ")
            else:
                time.sleep(1)
                print(" ")
                print("Attack Missed!")
        
        elif command.lower() == "flee":
            runluck = random.randint(1,5)
            
            if runluck == 1 or runluck == 2 or runluck == 3:
                time.sleep(1)
                print(" ")
                print("Got away safely!")
                var = 0
                
            else:
                time.sleep(1)
                print(" ")
                print("You were chased and could not escape!")
        
        elif command.lower() == "help":
            time.sleep(1)
            print(" ")
            print("Commands:")
            print(" ")
            time.sleep(1)
            print("attack")
            print("flee")
            print(" ")
            time.sleep(1)
        
        else:
            time.sleep(1)
            print(" ")
            print("Invalid command")
    
        if live != 0:
            enemyluck = random.randint(1,4)
            
            if enemyluck != 1:
                lifeforce = lifeforce - enemyDamage
                time.sleep(1)
                print(" ")
                print("You have been hit! You took {0} damage.".format(enemyDamage))
                
                if lifeforce <= 0:
                    death()
                    var = 0
                else:
                    print(" ")
            else:
                print("Enemy attack missed!")
            
        else:
            time.sleep(1)
            print(" ")

def death():
    global cursor
    
    time.sleep(2)
    print(" ")
    print("You have lost too much blood, your life force has been depleted!")
    time.sleep(1)
    print(" ")
    print("You are losing vision")
    time.sleep(1)
    print(" ")
    print("You fall to the floor and see a figure walk towards you.")
    time.sleep(1)
    print(" ")
    print("Your vision fades...")
    
    lifeforce = 25
    weapon = [1, "Scalpel", 5]
    armour = [1, "Ripped Lab Coat", 4]
    
    cursor.execute("UPDATE Save SET Weapon = 1, Armour = 1, LifeForce = 10 WHERE SaveID= ?",(saveID))
    
    time.sleep(2)
    print(" ")
    print("You wake up. Everything is very hazy.")
    time.sleep(3)
    print(" ")
    print("Regaining vision you see that you're in some kind of medical room.")
    time.sleep(3)
    print(" ")
    print("You see an empty syringe on the ground next to you labelled HALLUCINOGENS")
    time.sleep(3)
    print(" ")
    print("Looking at your arm you see needle holes. You've been given hallucinogens!")
    time.sleep(3)
    print(" ")
    print("These may affect the world around you. Rooms you have just came out of may have changed.")
    time.sleep(3)
    print(" ")
    print("Things are hard to see and nothing makes sense.")
    time.sleep(3)
    print(" ")
    print("You lost your weapons and armour!")
    time.sleep(3)
    print(" ")
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")
    time.sleep(3)
    print(" ")
    print("You need to find a way out!")
    time.sleep(3)      

def win(enemy):
    enemyName = enemy[0]
    global weapon
    global armour
    global cursor
    
    prize = dropGen()
    drop = prize[0]
    decider = prize[1]
    
    time.sleep(2)
    print(" ")
    print("You killed the {0}!".format(enemyName))
    print(" ")
    print("They dropped a {0}".format(drop[1]))
    
    if decider == 1:
        var = 1
        
        while var == 1:
            time.sleep(1)
            print(" ")
            answer = input("Would you like to replace your {0}: Defense = {1} with the {2}: Defense = {3}? (yes/no)".format(armour[1], armour[2], drop[1], drop[2]))
            
            if answer.lower() == "yes":
                armour = [drop[0], drop[1], drop[2]]
                cursor.execute("UPDATE Save SET Armour = ? WHERE SaveID= ?",(drop[0], saveID))
                con.commit()
                time.sleep(1)
                print(" ")
                print("You throw away your old armour and replaced with a new one! Armour updated")
                var = 0
            
            elif answer.lower() == "no":
                time.sleep(1)
                print(" ")
                print("You decide to keep your current armour.")
                var = 0
            
            else:
                time.sleep(1)
                print(" ")
                print("Invalid command. Enter yes or no.")
    
    else:
        var = 1
        
        while var == 1:
            time.sleep(1)
            print(" ")
            answer = input("Would you like to replace your {0}: Damage = {1} with the {2}: Damage = {3}? (yes/no)".format(weapon[1], weapon[2], drop[1], drop[2]))
            
            if answer.lower() == "yes":
                weapon = [drop[0], drop[1], drop[2]]
                cursor.execute("UPDATE Save SET Weapon = ? WHERE SaveID= ?",(drop[0], saveID))
                con.commit()
                time.sleep(1)
                print(" ")
                print("You throw away your old weapon and replaced with a new one! Weapon updated")
                var = 0
            
            elif answer.lower() == "no":
                time.sleep(1)
                print(" ")
                print("You decide to keep your current weapon.")
                var = 0
            
            else:
                time.sleep(1)
                print(" ")
                print("Invalid command. Enter yes or no.")

def enemyStatGen():
    global cursor
    
    randEnemy = random.randint(1,5)
    
    vari = cursor.execute("SELECT * from EnemyGen WHERE desID = {0}".format(randEnemy))
    for row in vari:
        enemyDes = row[1]
    
    enemyLifeForce = random.randint(10,40)
    enemyDamage = random.randint(3,10)
    
    enemy = (enemyDes, enemyLifeForce, enemyDamage)
    
    return enemy

def dropGen():
    global cursor
    
    randNumber = random.randint(1,10)
    decider = random.randint(1,2)
    
    if decider == 1:
        var = cursor.execute("SELECT * from Armours where ID = {0}".format(randNumber))
        for row in var:
            droplist = (row[0],row[1],row[2])
    
    else:
        var = cursor.execute("SELECT * from Weapons where ID = {0}".format(randNumber))
        for row in var:
            droplist = [row[0],row[1],row[2]]
    
    parcel = (droplist, decider)
    return parcel

def roomGen():
    randNumber = random.randint(1,15)

    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))
    for row in var:
        roomDes = row[1]
    
    return roomDes

def rest():
    global lifeforce
    lifeforce = 25
    time.sleep(1)
    print(" ")
    print("You take a nap for a few minutes..")
    time.sleep(5)
    print(" ")
    print("Lifeforce has been replenished.")
    print(" ")
    print("Lifeforce = {0}".format(lifeforce))
    time.sleep(3)
    print(" ")
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
            print(" ")
            print("You exit the room.")
            print(" ")
            time.sleep(3)
            
        elif ans.lower() == "attack":
            print(" ")
            combat()
            print(" ")
            time.sleep(3)
            
        elif ans.lower() == "rest":
            print(" ")
            rest()
            print(" ")
            time.sleep(3)
            
        elif ans.lower() == "checkstats":
            print(" ")
            checkStats()
            print(" ")
            time.sleep(3)
            
        elif ans.lower() == "save":
            print(" ")
            saving()
            print(" ")
            time.sleep(3)
            
        elif ans.lower() == "help":
            print(" ")
            help()
            print(" ")
            time.sleep(3)
        
        else:
            print(" ")
            print("Not a valid command; type help for a list of commands")
            print(" ")
            time.sleep(3)

main()