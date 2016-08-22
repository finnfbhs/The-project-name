#Test Python Code
#Created by Finn Foubister for testing different codes
import sqlite3

con = sqlite3.connect('database.db')
print("opened database successfully")

weaponID = 1
var = con.execute("SELECT * from Armour where ID = 1")
for row in var:
    #print("ID = ", row[0])
    #print("Name = ", row[1])
    #print("Defense = ", row[2], "\n")
    varlist = [row[0],row[1],row[2]]
    print(varlist)
print("operation successful")
con.close()