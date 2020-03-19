

# python app/script2.py

from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import execute_values 

# USE POSTGRESQL TO ANSWER QUESTION ABOUT TITANIC DATA
"""
How many passengers survived, and how many died?
How many passengers were in each class?
How many passengers survived/died within each class?
What was the average age of survivors vs nonsurvivors?
What was the average age of each passenger class?
What was the average fare by passenger class? By survival?
How many siblings/spouses aboard on average, by passenger class? By survival?
How many parents/children aboard on average, by passenger class? By survival?
Do any passengers have the same name?
(Bonus! Hard, may require pulling and processing with Python) 
How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name and with at least 1 sibling/spouse aboard are a married couple.
"""
# ESTABLISH CONNECTION TO DB
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

print("--------------")
print("PREGUNTAS")
print("How many passengers survived, and how many died?")

query = """
SELECT COUNT(survived)  
FROM titanic
WHERE survived = 1
"""
query2 = """
SELECT COUNT(survived)  
FROM titanic
WHERE survived <> 1
"""

cursor.execute(query)
result = cursor.fetchall()
print("SURVIVED:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("DID NOT SURVIVE:", result)


print("--------------")
print("How many passengers were in each class?")

query = """
SELECT COUNT(pclass)
FROM titanic
WHERE pclass = 1 
"""
query2 = """
SELECT COUNT(pclass)
FROM titanic
WHERE pclass = 2 
"""
query3 = """
SELECT COUNT(pclass)
FROM titanic
WHERE pclass = 3 
"""

cursor.execute(query)
result = cursor.fetchall()
print("CLASS 1:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("CLASS 2:", result)
cursor.execute(query3)
result = cursor.fetchall()
print("CLASS 3:", result)


print("--------------")
print("How many passengers survived/died within each class?")

query1a = """
SELECT count (survived)
FROM titanic
WHERE pclass = 1 AND survived = 0 
"""
query1b = """
SELECT count (survived)
FROM titanic
WHERE pclass = 1 AND survived = 1
"""
query2a = """
SELECT count (survived)
FROM titanic
WHERE pclass = 2 AND survived = 0 
"""
query2b = """
SELECT count (survived)
FROM titanic
WHERE pclass = 2 AND survived = 1
"""
query3a = """
SELECT count (survived)
FROM titanic
WHERE pclass = 3 AND survived = 0 
"""
query3b = """
SELECT count (survived)
FROM titanic
WHERE pclass = 3 AND survived = 1
"""

cursor.execute(query1a)
result = cursor.fetchall()
print("CLASS 1 PASSED:", result)
cursor.execute(query1b)
result = cursor.fetchall()
print("CLASS 1 SURVIVED:", result)
cursor.execute(query2a)
result = cursor.fetchall()
print("CLASS 2 PASSED:", result)
cursor.execute(query2b)
result = cursor.fetchall()
print("CLASS 2 SURVIVED:", result)
cursor.execute(query3a)
result = cursor.fetchall()
print("CLASS 3 PASSED:", result)
cursor.execute(query3b)
result = cursor.fetchall()
print("CLASS 3 SURVIVED:", result)


print("--------------")
print("What was the average age of survivors vs nonsurvivors?")

query = """
SELECT AVG(age) 
FROM titanic
WHERE survived = 0
"""
query2 = """
SELECT AVG(age) 
FROM titanic
WHERE survived = 1
"""

cursor.execute(query)
result = cursor.fetchall()
print("PASSED AVG AGE:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("SURVIVED AVG AGE:", result)


print("--------------")
print("What was the average age of each passenger class?")

query = """
SELECT AVG(age) 
FROM titanic
WHERE pclass = 1
"""
query2 = """
SELECT AVG(age) 
FROM titanic
WHERE pclass = 2
"""
query3 = """
SELECT AVG(age) 
FROM titanic
WHERE pclass = 3 
"""

cursor.execute(query)
result = cursor.fetchall()
print("CLASS 1 AVG AGE:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("CLASS 2 AVG AGE:", result)
cursor.execute(query3)
result = cursor.fetchall()
print("CLASS 3 AVG AGE:", result)

print("--------------")
print("What was the average fare by passenger class? By survival?")

query1a = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 1 
"""
query1b = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 1 and survived = 0
"""
query1c = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 1 and survived = 1
"""
query2a = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 2
"""
query2b = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 2 and survived = 0
"""
query2c = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 2 and survived = 1
"""
query3a = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 3
"""
query3b = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 3 and survived = 0
"""
query3c = """
SELECT AVG(fare) 
FROM titanic
WHERE pclass = 3 and survived = 1
"""

cursor.execute(query1a)
result = cursor.fetchall()
print("CLASS 1 AVG FARE:", result)
cursor.execute(query1b)
result = cursor.fetchall()
print("CLASS 1 PASSED AVG FARE :", result)
cursor.execute(query1c)
result = cursor.fetchall()
print("CLASS 1 SURVIVED AVG FARE:", result)
cursor.execute(query2a)
result = cursor.fetchall()
print("CLASS 2 AVG FARE:", result)
cursor.execute(query2b)
result = cursor.fetchall()
print("CLASS 2 PASSES AVG FARE:", result)
cursor.execute(query2c)
result = cursor.fetchall()
print("CLASS 2 SURVIVED AVG FARE:", result)
cursor.execute(query3a)
result = cursor.fetchall()
print("CLASS 3 AVG FARE:", result)
cursor.execute(query3b)
result = cursor.fetchall()
print("CLASS 3 PASSED AVG FARE:", result)
cursor.execute(query3c)
result = cursor.fetchall()
print("CLASS 2 SURVIVED AVG FARE:", result)


print("--------------")
print("How many siblings/spouses aboard on average, by passenger class? By survival?")

query = """
SELECT AVG(siblings_spouses) 
FROM titanic
"""
query2 = """
SELECT AVG(siblings_spouses) 
FROM titanic
WHERE pclass = 3
"""
query3 = """
SELECT AVG(siblings_spouses) 
FROM titanic
WHERE survived = 0
"""

cursor.execute(query)
result = cursor.fetchall()
print("AVG SIB/SPOUSE COUNT:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("CLASS 3 AVG SIB/SPOUSE COUNT:", result)
cursor.execute(query3)
result = cursor.fetchall()
print("AVG SIB/SPOUSE COUNT OF PASSED:", result)


print("--------------")
print("How many siblings/spouses aboard on average, by passenger class? By survival?")
query = """
SELECT count(name)
FROM titanic
"""
query2 = """
SELECT count(distinct name)
FROM titanic
"""

cursor.execute(query)
result = cursor.fetchall()
print("NAME COUNT:", result)
cursor.execute(query2)
result = cursor.fetchall()
print("DISTINCT NAME COUNT:", result)
