#Test Python Code
#Created by Finn Foubister for testing different codes
import sqlite3

con = sqlite3.connect('database.db')
print("opened database successfully")

var = con.execute("SELECT * from Armour")
for row in var:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Defense = ", row[2], "\n")
    
print("operation successful")
con.close()