#Test Python Code
#Created by Finn Foubister for testing different codes
import sqlite3
import random
con = sqlite3.connect('database.db')
print("opened database successfully")

#weaponID = 1
#var = con.execute("SELECT * from Armour where ID = 1")
#for row in var:
    #print("ID = ", row[0])
    #print("Name = ", row[1])
    #print("Defense = ", row[2], "\n")
    #varlist = [row[0],row[1],row[2]]
    #print(varlist)

#def newSave():
    #cursor = con.cursor()
    #name = input("What is your name?")
    #details = (name,1,1)
    #cursor.execute("INSERT INTO Save(Name,Weapon,Armour) VALUES (?,?,?)",details)
    #con.commit()

#def save():
    #name = "Joe"
    #weapon = (3, "Wrench", 8)
    #armour = (3, "Shirt and Jeans", 7)
    #saveID = 2
    #weaponID = weapon[0]
    #armourID = armour[0]
    
    #cursor = con.cursor()
    #cursor.execute("UPDATE Save SET Name = ?, Weapon = ?, Armour = ? WHERE SaveID= ?",(name, weaponID, armourID, saveID))
    #con.commit()
    #print("operation successful")

def roomGen():
    randNumber = random.randint(1,30)
    print(randNumber)
    cursor = con.cursor()
    var = cursor.execute("SELECT * from RoomGen WHERE desID = {0}".format(randNumber))
    for row in var:
        roomDes = row[1]
    print(roomDes)

roomGen()