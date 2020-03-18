# python app/insert_rpg.py

import os 
import sqlite3

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values 

# connection to RPG database
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"..","..",
"Desktop/Unit3/SQL/rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

# GETTING TABLE VALUES IN TUPLE
query = """
SELECT *
FROM charactercreator_character
"""

character_list = cursor.execute(query).fetchall()
print("TABLE: charactercreator_character")
col_names = ['character_id','name','level','exp','hp','strength',
'intelligence','dexterity','wisdom']
print("COLUMN NAMES:", col_names )
print(character_list)
print("------------------")


# CREATING NEW TABLE
load_dotenv()

DB_NAME = os.getenv("DB_NAME", default = "Ooops")
DB_USER = os.getenv("DB_USER", default = "Ooops")
DB_PASSWORD = os.getenv("DB_PASSWORD", default = "Ooops")
DB_HOST = os.getenv("DB_HOST", default = "Ooops")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# Create table 
query = """
CREATE TABLE IF NOT EXISTS charactercreator_character 
(id SERIAL PRIMARY KEY,
character_id INTEGER,
name VARCHAR(30),
level INTEGER,
exp INTEGER,
hp INTEGER,
strength INTEGER,
intelligence INTEGER,
dexterity INTEGER,
wisdom INTEGER);
"""

cursor.execute(query)
cursor.execute('SELECT * from charactercreator_character;')
result = cursor.fetchall()
print("RESULT:", len(result))


# # DATA INSERTION
# ALREADY EXECUTED ---------------------------
# argslist = character_list

# insertion_query = """
# INSERT INTO charactercreator_character
# (character_id, name, level, exp, hp, strength, 
# intelligence, dexterity, wisdom)
# VALUES %s
# """
# execute_values(cursor, insertion_query, argslist)
   
cursor.execute('SELECT * from charactercreator_character;')
result = cursor.fetchmany(size=5)
print("CHARACTER TABLE:", result)
cursor.execute('SELECT * from charactercreator_character;')
result2 = cursor.fetchall()
print("ROW COUNT:", len(result2))

connection.commit()
