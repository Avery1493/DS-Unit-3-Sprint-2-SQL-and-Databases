
# python buddymove_holidayiq.py

import os
import pandas as pd
import sqlite3

CSV_FILEPATH = 'https://raw.githubusercontent.com/Avery1493/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

df = pd.read_csv(CSV_FILEPATH)
"""
User Id	Sports	Religious	Nature	Theatre	Shopping	Picnic
"""
print(df.shape)
print(df.head())


connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("buddymove_holidayiq.sqlite3", connection, if_exists='replace')

cursor = connection.cursor()

# How many rows are there?
query = """
SELECT count(`User Id`)
FROM 'buddymove_holidayiq.sqlite3'
"""

result = cursor.execute(query).fetchall()
print("Total Rows")
print(result)
print("------------------")


# How many users who reviewed at least 100 Nature in the category also 
# reviewed at least 100 in the Shopping category?
query = """
SELECT count(`User Id`)
FROM 'buddymove_holidayiq.sqlite3'
WHERE Nature >= 100 AND Shopping >= 100
"""

result = cursor.execute(query).fetchall()
print("Total Users")
print(result)
print("------------------")


# What are the average number of reviews for each category?
query = """
SELECT AVG(Sports),
    AVG(Religious),
    AVG(Nature),
    AVG(Theatre),
    AVG(Shopping),
    AVG(Picnic)
FROM 'buddymove_holidayiq.sqlite3'
"""

result = cursor.execute(query).fetchall()
print("Average Rows")
print(result)
print("------------------")
