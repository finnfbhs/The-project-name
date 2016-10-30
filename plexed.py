#Plexed
#Created by Finn Foubister 17/08/2016
#This is a game designed for NCEA level 2 standards assessment

import sqlite3          #Imports sqlite3 for connecting to the database
import random           #Imports random for the Gen functions
import time         #Imports time module for sleeps
import math         #Imports math module for combat function
con = sqlite3.connect('database.db')            #Adds a connect to database variable
cursor = con.cursor()           #Adds a cursor database variable

def loading():          #Loading function for loading user data, creating a new save or deleting saved data in the database
    hold = 0            #Variable for looping
    while hold == 0:            #Looping while statement
        global cursor           #Declares global variable
        global name             #Declares global variable                                                             
        global weapon           #Declares global variable
        global armour           #Declares global variable
        global lifeforce        #Declares global variable
        global saveID           #Declares global variable
        
        print(" ")          #Outputs spacer line
        print("Saves:")         #Outputs Saves:
        print(" ")          #Outputs a spacer line
        time.sleep(1)           #hold 1 second
        
        saveidlist = []         #initializes variable as list
        saverow = cursor.execute("SELECT SaveID from Save")         #Pulls saveID from Save table in database
        for row in saverow:
            savehold = row[0]           #Variable to be put into list
            saveidlist.append(savehold)         #Appends list with new variable
        
        curs = con.execute("SELECT SaveID,Name from Save")          #Pulls saveID and Name from Save table in database
        for row in curs:
            print("{0}. {1}".format(row[0],row[1]))        #Outputs list of name and save id
        time.sleep(1)           #hold 1 second
        print(" ")          #Outputs a spacer line
        answer = input("To create a new save enter '0', to load a save enter the save number, to delete a save enter '-1'.")           #Asks for input
        try:
            answerint = int(answer)
            
            if answerint == 0:         #If input was 0 then:
                hold = 1            #Set hold variable to 1 so loop ends
                newSave()           #Runs newSave function
            
            elif answerint == -1:          #Else if input was -1 then:
                print(" ")          #Outputs spacer line
                time.sleep(1)           #hold 1 second
                holdtwo = 1         #Set holdtwo variable to 1 so loop starts
                
                while holdtwo == 1:         #Loop
                    answer = input("Are you sure? (yes/no)")            #Asks for input
                    
                    if answer.lower() == "yes":         #If input was yes then:
                        print(" ")          #Outputs spacer line
                        deleteSave()            #Runs deleteSave function
                        holdtwo = 0         #Sets holdtwo variable to 0 to end loop
                        
                    elif answer.lower() == "no":            #Else if input was no then:
                        print(" ")          #Outputs spacer line
                        holdtwo = 0         #Sets variable to 0 to end loop
                        
                    else:           #Else input was else then:
                        print(" ")          #Outputs spacer line
                        print("Invalid command. Enter yes or no.")          #Outputs error message
                        time.sleep(1)           #hold 1 second
                    
            elif answerint in saveidlist:          #Else if input is in saveidlist list then:
                hold = 1            #Sets variable to 1 to end loop
                saveID = answer         #Sets saveID global variable to input
                print(" ")          #Outputs spacer line
                
                #Loading name from database
                cursor = con.execute("SELECT Name from Save where SaveID = {0}".format(answer))         #Pulls name from Save table in database where saveID is input
                for row in cursor:
                    name = row[0]           #Set name global variable to pulled data
                    print("Name = {0}".format(name))            #Outputs name variable statement
                    time.sleep(1)           #hold 1 second
                
                #Loading lifeforce from database 
                curs = con.execute("SELECT LifeForce from Save where SaveID = {0}".format(answer))          #Pulls LifeForce from Save table in database where saveID is input
                for row in curs:
                    lifeforce = row[0]          #Set lifeforce global variable to pulled data
                    print("Lifeforce = {0}".format(lifeforce))          #Outputs lifeforce variable statement
                    time.sleep(1)           #hold 1 second
                
                #Loading weapon from database      
                curs = con.execute("SELECT Weapon from Save where SaveID = {0}".format(answer))         #Pulls Weapon from Save table in database where saveID is input
                for row in curs:
                    weaponID = row[0]           #Sets weaponID to pulled data
                weaponcur = con.execute("SELECT * from Weapons where ID = {0}".format(weaponID))            #Pulls all data from Weapons table in database where weaponID is weaponID variable
                for row in weaponcur:
                    weapon = [row[0],row[1],row[2]]         #Sets weapon global list to pulled data
                    print("Weapon = {0}".format(weapon[1]))         #Outputs weapon variable statement
                    time.sleep(1)           #hold 1 second
                
                #Loading armour from database
                curs = con.execute("SELECT Armour from Save where SaveID = {0}".format(answer))         #Pulls Armour from Save table in database where saveID is input
                for row in curs:
                    armourID = row[0]           #Sets armourID to pulled data
                armourcur = con.execute("SELECT * from Armours where ID = {0}".format(armourID))            #Pulls all data from Armours table in database where ID is armourID variable
                for row in armourcur:
                    armour = [row[0],row[1],row[2]]         #Sets armour global list to pulled data
                    print("Armour = {0}".format(armour[1]))         #Outputs armour variable statement
                    time.sleep(3)           #hold 3 seconds
                    
            else:           #Else if input was else then:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("{0} is not a valid input, please follow the instructions.".format(answer))           #Print error message displaying incorrect input
                time.sleep(1)           #hold 1 second
                
        except ValueError:          #If input was not an integer
            time.sleep(1)           #hold 1 second
            print(" ")          #Outputs spacer line
            print("Please enter an integer")            #Outputs error message
            print(" ")          #Outputs spacer line
            time.sleep(1)           #hold 1 second

def saving():           #Saving function for saving the users data to the database
    global cursor           #Declares global variable
    
    weaponID = weapon[0]            #Sets weaponID to data at position 0 in weapon list
    armourID = armour[0]            #Sets armourID to data at position 0 in armour list
    
    cursor.execute("UPDATE Save SET Weapon = ?, Armour = ?, LifeForce = ? WHERE SaveID= ?",(weaponID, armourID, lifeforce, saveID))         #Updates Saves table data in database where SaveID is saveID variable
    con.commit()            #Commits the updated data to the database
    
    print("Game saved successfully")            #Outputs confirmation message

def deleteSave():           #deleteSave function for deleting saves
    global cursor           #Declares global variable
    
    time.sleep(1)           #hold 1 second
    print("Saves:")         #Output Saves:
    curs = con.execute("SELECT SaveID,Name from Save")          #Pulls SaveID and Name from Save table in database
    for row in curs:
        print(row[0],row[1])            #Prints each SaveID and Name next to each other for every row of data in the table
    
    time.sleep(1)           #hold 1 second
    print(" ")          #Outputs spacer line
    ID = int(input("What save would you like to delete? (Enter the save number)"))          #Sets ID to input, Asking which save to delete
    cursor.execute("DELETE FROM Save where SaveID = {0}".format(ID))            #Deletes row of data in Save table in database where SaveID is ID value
    con.commit()            #Commits the deletion to the database
    
    time.sleep(1)           #hold 1 second
    print(" ")          #Outputs spacer line
    print("Save {0} deleted successfully".format(ID))           #Outputs confirmation that the save has been deleted
    time.sleep(3)           #hold 3 seconds

def newSave():          #newSave function where new saves are created
    global name         #Declares global variable
    global weapon           #Declares global variable
    global armour           #Declares global variable
    global lifeforce            #Declares global variable
    global saveID           #Declares global variable
    global cursor           #Declares global variable
    
    time.sleep(1)           #hold 1 second
    print(" ")          #Output spacer line
    name = input("What is your name?")          #Sets name to input
    details = (name,1,1,10)         #Sets details list to input,1,1,10 to go into the database

    cursor.execute("INSERT INTO Save(Name,Weapon,Armour,LifeForce) VALUES (?,?,?,?)",details)           #Inserts details list data into Save table in database
    con.commit()            #Commits the insertion to the database
    
    savelist = []           #Initializes savelist variable as a list
    saveids = cursor.execute("SELECT SaveID from Save")         #Sets saveids to SaveID data from Save table in database
    for row in saveids:
        saveidhold = row[0]         #saveidhold is set to SaveID data to append list
        savelist.append(saveidhold)         #Appends savelist by adding saveidhold value onto the end of the list for each row
    saveID = max(savelist)          #Sets saveID global variable to the largest number in savelist list
    
    lifeforce = 30          #Sets lifeforce global variable to 30
    weapon = [1, "Scalpel", 5]          #Sets weapon global variable
    armour = [1, "Ripped Lab Coat", 4]          #Sets armour global variable
    
    time.sleep(1)           #hold 1 second
    print(" ")          #Output spacer line
    time.sleep(2)           #hold 2 seconds
    print("You wake up. Everything is very hazy.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("Regaining vision you see that you're in some kind of medical room.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("You see an empty syringe on the ground next to you labelled HALLUCINOGENS")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("Looking at your arm you see needle holes. You've been given hallucinogens!")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("These may affect the world around you. Rooms you have just came out of may have changed.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("Things are hard to see and nothing makes sense.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print("You need to find a way out!")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds   

def combat():           #combat function where the combat gameplay takes place
    live = 1        #Sets live to 1 for loop
    global lifeforce            #Declares global variable
    
    enemy = enemyStatGen()          #Sets enemy list to returned values of enemyStatGen function
    enemyLifeForce = enemy[1]           #enemyLifeForce is set to the data value at position 1 in enemy list
    enemyDamage = enemy[2]          #enemyDamage is set to the data value at position 2 in enemy list
    defenseTotal = armour[2] + lifeforce
    time.sleep(1)           #hold 1 second
    print(" ")          #Outputs spacer line
    print("A {0} leaps out at you. Time to fight!".format(enemy[0]))            #Outputs combat initiation statement
    print(" ")          #Outputs spacer line
    time.sleep(2)           #hold 2 seconds
    var = 1         #set var variable to 1 for loop
    
    while var == 1:         #While loop whilst var is equal to 1
        hold2 = 0
        while hold2 == 0:
            print("{0} Defense = {1}       {2} Defense = {3}".format(name, defenseTotal, enemy[0], enemyLifeForce))          #Outputs player lifeforce variable and enemyLifeForce variable
            print(" ")          #Outputs spacer line
            time.sleep(2)           #hold 2 seconds
            command = input("What are you going to do? (type help for a list of battle commands)")          #sets command to input
                
            if command.lower() == "stab":         #If command equals attack then:
                hold2 = 1           #Sets hold2 to 1 to end loop
                hitluck = random.randint(1,5)           #hitluck is set to a random number between 1 and 5
                    
                if hitluck != 1:            #If hitluck isn't equal to 1 then:
                    enemyLifeForce = enemyLifeForce - weapon[2]         #Takes away the value of the data in position 2 of weapon list from enemyLifeForce variable
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Outputs spacer line
                    print("Attack Hit! Enemy took {0} damage!".format(weapon[2]))           #Outputs successful hit statement
                    
                    if enemyLifeForce <= 0:         #If enemyLifeForce is less than 0 then:
                        win(enemy)          #Run the win function with parameters: enemy list
                        live = 0            #Set live to 0 to end loop
                        var = 0         #Set var to 0 to end while loop
                        
                    else:           #If enemyLifeForce is else then:
                        time.sleep(1)           #hold 1 second
                        live = 1            #Set live to 1 to continue loop
                        print(" ")          #Output spacer line
                    
                else:           #If hitluck is equal to 1 then:
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Output spacer line
                    print("Attack Missed!")         #Output Attack missed statement
            
            elif command.lower() == "swipe":
                hold2 = 1           #Sets hold2 to 1 to end loop
                hitluck = random.randint(1,5)           #hitluck is set to a random number between 1 and 5
                    
                if hitluck == 1 or hitluck == 2:            #If hitluck isn't equal to 1 then:
                    hitdamage = weapon[2]*2         #Sets hitdamage to two times the value of the data of weapon list at position 2
                    enemyLifeForce = enemyLifeForce - hitdamage         #Takes away the value of hitdamage from enemyLifeForce
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Outputs spacer line
                    print("Attack Hit! Enemy took {0} damage!".format(hitdamage))           #Outputs successful hit statement
                    
                    if enemyLifeForce <= 0:         #If enemyLifeForce is less than 0 then:
                        win(enemy)          #Run the win function with parameters: enemy list
                        live = 0            #Set live to 0 to end loop
                        var = 0         #Set var to 0 to end while loop
                        
                    else:           #If enemyLifeForce is else then:
                        time.sleep(1)           #hold 1 second
                        live = 1            #Set live to 1 to continue loop
                        print(" ")          #Output spacer line
                    
                else:           #If hitluck is equal to 1 then:
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Output spacer line
                    print("Attack Missed!")         #Output Attack missed statement
            
            elif command.lower() == "flee":         #Else if command is flee then:
                hold2 = 1           #Sets hold2 to 1 to end loop
                runluck = random.randint(1,5)           #Sets runluck to a random number between 1 and 5
                
                if runluck == 1 or runluck == 2 or runluck == 3:            #If runluck is equal to 1, 2 or 3 then:
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Output spacer line
                    print("Got away safely!")           #Output successful flee statement
                    var = 0         #Sets var to 0 to end loop
                    live = 0            #Sets live to 0 to end loop
                    
                else:           #If runluck is equal to 4 or 5 then:
                    time.sleep(1)           #hold 1 second
                    print(" ")          #Output spacer line
                    print("You were chased and could not escape!")          #Outputs unsuccessful flee statement
            
            elif command.lower() == "help":         #Else if command is help then:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("Commands:")          #Outputs Commands:
                print(" ")          #Outputs spacer line
                time.sleep(1)           #hold 1 second
                print("stab (Stab is a higher chance to hit, lower damage attack)")         #Outputs stab message
                print("swipe (Swipe is a lower chance to hit, higher damage attack)")           #Outputs swipe message
                print("flee (Attempts to flee battle)")           #Outputs flee
                print(" ")          #Outputs spacer line
                time.sleep(1)           #hold 1 second
            
            else:           #Else command is else then:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("Invalid command")            #Outputs error message
                print(" ")          #Outputs spacer line

        if live != 0:           #If enemy is alive then:
            enemyluck = random.randint(1,4)         #Sets enemyluck to a random integer between 1 and 4
            
            if enemyluck != 1:          #If enemyluck is not equal to 1 then:
                lifeforce = lifeforce - enemyDamage         #Subtract the value of enemyDamage from lifeforce global variable
                defenseTotal = armour[2] + lifeforce
                time.sleep(1)           #hold 1 second
                print("You have been hit! You took {0} damage.".format(enemyDamage))            #Outputs successful enemy hit statement
                
                if defenseTotal <= 0:          #If lifeforce global variable less than or equal to 0 then:
                    death()         #Runs death function
                    var = 0         #Sets variable to 0 to end loop
                
                else:           #Else so lifeforce global variable is more than 0 then:
                    print(" ")          #Output spacer line
                
            else:           #Else so enemyluck is equal to 1:
                print("Enemy attack missed!")           #Outputs enemy attack missed statement
            
        else:           #Else so live equals 0:
            time.sleep(1)           #hold 1 second
            print(" ")          #Outputs spacer line

def death():            #death function. Occurs if player loses combat
    global saveID           #Declares global variable saveID
    global cursor           #Declares global variable cursor
    
    time.sleep(2)           #hold 2 seconds
    print(" ")          #Output spacer line
    print("You have lost too much blood, your life force has been depleted!")           #Outputs storyline description
    time.sleep(1)           #hold 1 second
    print(" ")          #Output spacer line
    print("You are losing vision")          #Outputs storyline description
    time.sleep(1)           #hold 1 second
    print(" ")          #Output spacer line
    print("You fall to the floor and see a figure walk towards you.")           #Outputs storyline description
    time.sleep(1)           #hold 1 second
    print(" ")          #Output spacer line
    print("Your vision fades...")           #Outputs storyline description
    
    lifeforce = 25          #Sets liforce variable to 25
    weapon = [1, "Scalpel", 5]          #Sets weapon list values
    armour = [1, "Ripped Lab Coat", 4]          #Sets armour list values
    
    cursor.execute("UPDATE Save SET Weapon = 1, Armour = 1, LifeForce = 10 WHERE SaveID= ?",(saveID,))           #Updates the Save table in database where SaveID equals saveID value
    
    time.sleep(2)           #hold 2 seconds 
    print(" ")          #Output spacer line
    print("You wake up. Everything is very hazy.")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("Regaining vision you see that you're in some kind of medical room.")         #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("You see an empty syringe on the ground next to you labelled HALLUCINOGENS")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("Looking at your arm you see needle holes. You've been given hallucinogens!")         #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("These may affect the world around you. Rooms you have just came out of may have changed.")           #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("Things are hard to see and nothing makes sense.")            #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("You lost your weapons and armour!")          #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("You find a Scalpel and a Ripped Lab Coat so you grab them. Maybe they could be of use.")         #Outputs storyline description
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Output spacer line
    print("You need to find a way out!")            #Outputs storyline description
    time.sleep(3)           #hold 3 seconds  

def win(enemy):         #win function. Occurs when player wins combat
    enemyName = enemy[0]            #Sets enemyName to the value of enemy list at position 0
    global weapon           #Declares global variable
    global armour           #Declares global variable
    global cursor           #Declares global variable
    
    prize = dropGen()           #Set prize returned value from dropGen function
    drop = prize[0]         #Set drop to the value of prize list at position 0
    decider = prize[1]          #Set decider to the value of prize list at position 1
    
    time.sleep(2)           #hold 2 seconds
    print(" ")          #Outputs spacer line
    print("You killed the {0}!".format(enemyName))          #Output successful win statement
    print(" ")          #Outputs spacer line
    print("They dropped a {0}".format(drop[1]))         #Outputs what item the enemy dropped
    
    if decider == 1:            #If decider variable is equal to 1: (If decider is 1 the item dropped is an armour)
        var = 1         #Set var to 1 for loop
        
        while var == 1:         #Loop
            time.sleep(1)           #hold 1 second
            print(" ")          #Outputs spacer line
            answer = input("Would you like to replace your {0}: Defense = {1} with the {2}: Defense = {3}? (yes/no)".format(armour[1], armour[2], drop[1], drop[2]))            #Set answer to input, asks player if they would like to replace their currently equipped armour with the dropped piece
            
            if answer.lower() == "yes":         #If answer is equal to yes then:
                armour = [drop[0], drop[1], drop[2]]            #Set armour to new values
                cursor.execute("UPDATE Save SET Armour = ? WHERE SaveID= ?",(drop[0], saveID))          #Updates armour in Save table in database where SaveID = saveID value
                time.sleep(1)           #hold 1 second
                print(" ")          #Output spacer line
                print("You throw away your old armour and replaced with a new one! Armour updated")         #Outputs successful armour swap statement
                var = 0         #Set var to 0 to end loop
            
            elif answer.lower() == "no":            #Else if answer is equal to no then:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("You decide to keep your current armour.")            #Outputs keep armour statement
                var = 0         #Sets var to 0 to end loop
            
            else:           #Else so answer is not equal to yes or no:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("Invalid command. Enter yes or no.")          #Outputs error message
    
    else:           #Else so item dropped is a weapon
        var = 1         #Sets var to 1 for loop
        
        while var == 1:         #Loop statement
            time.sleep(1)           #hold 1 second
            print(" ")          #Outputs spacer line
            answer = input("Would you like to replace your {0}: Damage = {1} with the {2}: Damage = {3}? (yes/no)".format(weapon[1], weapon[2], drop[1], drop[2]))          #Set answer to input, asks player if they would like to replace their currently equipped weapon with the dropped piece
            
            if answer.lower() == "yes":         #If answer is equal to yes then:
                weapon = [drop[0], drop[1], drop[2]]            #Sets weapon to new values
                cursor.execute("UPDATE Save SET Weapon = ? WHERE SaveID= ?",(drop[0], saveID))          #Updates weapon in Save table in database where SaveID = saveID value
                time.sleep(1)           #hold 1 second
                print(" ")          #Output spacer line
                print("You throw away your old weapon and replaced with a new one! Weapon updated")         #Outputs successful weapon swap statement
                var = 0         #Sets var to 0 to end loop
            
            elif answer.lower() == "no":            #Else if answer is equal to no then:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("You decide to keep your current weapon.")            #Outputs keep weapon statement
                var = 0         #Sets var to 0 to end loop
            
            else:           #Else so answer is not equal to yes or no:
                time.sleep(1)           #hold 1 second
                print(" ")          #Outputs spacer line
                print("Invalid command. Enter yes or no.")          #Outputs error message

def enemyStatGen():         #enemyStatGen function is called in combat function. Its purpose is to generate a description, lifeforce and damage value for the enemy for combat
    global cursor           #Declares global variable
    
    randEnemy = random.randint(1,5)         #Set randEnemy to a random integer between 1 and 5
    
    vari = cursor.execute("SELECT * from EnemyGen WHERE desID = {0}".format(randEnemy))         #Set vari to pulled data from EnemyGen table in database where desID is equal to randEnemy value
    for row in vari:            #For every row in pulled data:
        enemyDes = row[1]           #Set enemyDes to value of pulled data at position 1
    
    enemyLifeForce = random.randint(10,40)          #Sets enemyLifeForce to a random integer between 10 and 40
    enemyDamage = random.randint(3,8)          #Sets enemyDamage to a random integer between 3 and 8
    
    enemy = (enemyDes, enemyLifeForce, enemyDamage)         #Sets enemy to a list containing enemyDes, enemyLifeForce and enemyDamage. This is essentially a parcel for returning values easily
    
    return enemy            #Returns the enemy list back to the combat function

def dropGen():          #dropGen function is called in the win function. Its purpose is to randomly pull a weapon or armour from the database and return it to the win function to be given to the player
    global cursor           #Declares global variable
    
    randNumber = random.randint(1,10)           #Set randNumber to a random integer between 1 and 10
    decider = random.randint(1,2)           #Set decider to a random integer either 1 or 2
    
    if decider == 1:            #If decider equals 1 then:
        var = cursor.execute("SELECT * from Armours where ID = {0}".format(randNumber))         #Set var to data in Armours table in database where ID equals randNumber
        for row in var:         #For every row of data in var:
            droplist = (row[0],row[1],row[2])           #Set droplist list to pulled data values
    
    else:           #If decider equals 2 then:
        var = cursor.execute("SELECT * from Weapons where ID = {0}".format(randNumber))         #Set var to data in Weapons table in database where ID equals randNumber
        for row in var:         #For every row of data in var:
            droplist = [row[0],row[1],row[2]]           #Set droplist list to pulled data values
    
    parcel = (droplist, decider)            #Set parcel list to droplist and decider values. This is to easily return both sets of data into the win function
    return parcel           #Send parcel list to win function

def roomGen():          #roomGen function. Its purpose is to generate a room description and return it to the main function
    randNumber = random.randint(1,15)           #Set randNumber to a random integer between 1 and 15

    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))          #Set var to data in RoomGen table in database where desID equals randNumber
    for row in var:         #For every row of data in var:
        roomDes = row[1]            #Set roomDes to data in position 1 of row
    
    return roomDes          #Return roomDes value to main function

def rest():         #rest function. Its purpose is to set players life force back to full
    global lifeforce            #Declares global variable
    
    lifeforce = 30          #Sets lifeforce to 30
    
    time.sleep(1)           #hold 1 second
    print(" ")          #Outputs spacer line
    print("You take a nap for a few minutes..")         #Outputs nap message
    time.sleep(4)           #hold 4 seconds
    print(" ")          #Outputs spacer line
    print("Lifeforce has been replenished.")            #Outputs successful rest message
    print(" ")          #Outputs spacer line
    time.sleep(1)           #hold 1 second
    print("Lifeforce = {0}".format(lifeforce))          #Outputs lifeforce value
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Outputs spacer line
    print("You wake up and you feel someone watching you so you exit the room")         #Outputs message

def checkStats():           #checkStats function. Its purpose is to display the players weapon and armour values and their life force level
    print("Name = {0}".format(name))            #Outputs player name
    print("Lifeforce = {0}".format(lifeforce))          #Outputs lifeforce value
    print("Weapon = {0}, Damage = {1}".format(weapon[1],weapon[2]))         #Outputs weapon name and damage value
    print("Armour = {0}, Defense = {1}".format(armour[1],armour[2]))            #Outputs armour name and defense value
    time.sleep(3)           #hold 3 seconds
    print(" ")          #Outputs spacer line
    print("You didn't realize but you kept walking as you were checking your statistics so you've exited your other room.")         #Outputs message

def help():         #help function. Its purpose is to display the possible commands for the player in the main function
    print("List of commands:")          #Outputs List of commands:
    print(" ")          #Outputs spacer line
    time.sleep(1)           #hold 1 second
    print("Explore")            #Outputs possible command
    time.sleep(1)           #hold 1 second
    print("Attack")         #Outputs possible command
    time.sleep(1)           #hold 1 second
    print("Rest")           #Outputs possible command
    time.sleep(1)           #hold 1 second
    print("Checkstats")         #Outputs possible command
    time.sleep(1)           #hold 1 second
    print("Save")           #Outputs possible command
    time.sleep(1)           #hold 1 second
    print(" ")          #Outputs spacer line
    time.sleep(3)           #hold 3 seconds
    print("In your search for inner help you have walked into another room.")           #Outputs message

def main():         #main function. Its purpose is to run through the main part of the gameplay. Many other functions are called from this function
    print("Plexed")         #Outputs Plexed
    print(" ")          #Outputs spacer line
    time.sleep(3)           #hold 3 seconds
    loading()           #Runs loading function
    variable = 1            #Sets variable to 1 for loop
    
    while variable == 1:            #While loop
        roomDes = roomGen()         #Set roomDes from returned value from roomGen function
        print(" ")          #Outputs spacer line
        print("You come into {0}".format(roomDes))          #Outputs current setting
        print(" ")          #Outputs spacer line
        time.sleep(3)           #hold 3 seconds
        ans = input("What would you like to do? (type help for a list of commands)")            #Set ans to input, asks player what command they would like to carry out
        if ans.lower() == "explore":            #If ans is equal to explore:
            print(" ")          #Outputs spacer line
            print("You exit the room.")         #Outputs successful explore message
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
            
        elif ans.lower() == "attack":           #Else if ans is equal to attack:
            print(" ")          #Outputs spacer line
            combat()            #Runs combat function
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
            
        elif ans.lower() == "rest":         #Else if ans is equal to rest:
            print(" ")          #Outputs spacer line
            rest()          #Runs rest function
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
            
        elif ans.lower() == "checkstats":
            print(" ")          #Outputs spacer line
            checkStats()            #Runs checkStats function
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
            
        elif ans.lower() == "save":
            print(" ")          #Outputs spacer line
            saving()            #Runs saving function
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
            
        elif ans.lower() == "help":
            print(" ")          #Outputs spacer line
            help()          #Runs help function
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds
        
        else:
            print(" ")          #Outputs spacer line
            print("Not a valid command; type help for a list of commands")          #Outputs error message
            print(" ")          #Outputs spacer line
            time.sleep(3)           #hold 3 seconds

main()          #Runs main function