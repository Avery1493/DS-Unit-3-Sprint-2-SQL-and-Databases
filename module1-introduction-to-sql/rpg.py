
# 321
# python rpg.py

import os
import sqlite3

# connection to database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

# How many total Characters are there?
query = """
SELECT 
	COUNT(character_id)
FROM charactercreator_character
"""

result = cursor.execute(query).fetchall()
print("Total Characters")
print(result)
print("------------------")


# How many of each specific subclass?
query = """
# SELECT 
# 	count(distinct charactercreator_mage.character_ptr_id) as mage,
# 	count(distinct charactercreator_cleric.character_ptr_id) as cleric,
# 	count(distinct charactercreator_thief.character_ptr_id) as theif,
# 	count(distinct charactercreator_fighter.character_ptr_id) as fighter
# FROM 
# 	charactercreator_mage,
# 	charactercreator_cleric,
# 	charactercreator_thief,
# 	charactercreator_fighter
# """

# result = cursor.execute(query).fetchall()
# print("Characters per subclass")
# print(result)
# print("------------------")


# How many total Items?
query = """
SELECT count()item_id
FROM armory_item
"""

result = cursor.execute(query).fetchall()
print("Total Items")
print(result)
print("------------------")


# How many of the Items are weapons? How many are not?
query = """
SELECT count(item_ptr_id) as weapon
FROM armory_weapon
"""

result = cursor.execute(query).fetchall()
print("Weapons")
print(result)
print("--not wepons: 137")
print("------------------")


# How many Items does each character have? (Return first 20 rows)
query = """
SELECT character_id,
	item_id
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
"""

result = cursor.execute(query).fetchall()
print("Total Items Per Character")
print("First 20")
print(result)
print("------------------")


# How many Weapons does each character have? (Return first 20 rows)
query = """
SELECT count()item_id
FROM armory_item
"""

result = cursor.execute(query).fetchall()
print("Total Weapons Per Character")
print("First 20")
print(result)
print("------------------")


# On average, how many Items does each Character have?
query = """
SELECT count(item_id) as items
FROM charactercreator_character_inventory
"""

query2 = """
SELECT count (DISTINCT character_id) as Character
FROM charactercreator_character_inventory
"""

result = cursor.execute(query).fetchall()
result2 = cursor.execute(query2).fetchall()
print("Total Items")
print(result)
print("Total Items")
print(result2)
print("Average per person")
print(898/302)
print("------------------")


# On average, how many Weapons does each character have?
query = """
SELECT count()item_id
FROM armory_item
"""

result = cursor.execute(query).fetchall()
print("Total Items")
print(result)
print("------------------")