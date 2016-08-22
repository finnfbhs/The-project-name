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
    cursor = con.execute("SELECT Name from Save")
    for row in cursor:
        name = row[0]
    print(name)    

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