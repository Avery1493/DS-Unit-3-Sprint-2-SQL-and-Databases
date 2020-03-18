# python app/insert_titanic.py

import os 
import pandas as  pd

from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values 

# load titanic dataset (csv file)
CSV_FILEPATH = "https://raw.githubusercontent.com/Avery1493/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv"
df = pd.read_csv(CSV_FILEPATH)

print(df.shape)
print(df.head())
print(df.columns)
print(df.dtypes)
"""
Survived Pclass Name Sex Age Siblings_Spouses,
Parents_Children Fare]
"""


# GETTING DF VALUES IN TUPLE
titanic = df.to_records().tolist()
#print(titanic)


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
CREATE TABLE IF NOT EXISTS titanic
(id SERIAL PRIMARY KEY,
Survived INTEGER,
Pclass INTEGER,
Name VARCHAR,
Sex VARCHAR(7),
Age FLOAT,
Siblings_Spouses INTEGER,
Parents_Children INTEGER,
Fare FLOAT);
"""

cursor.execute(query)
cursor.execute('SELECT * from titanic;')
result = cursor.fetchall()
print("RESULT:", len(result))


# DATA INSERTION
# # ALREADY EXECUTED ---------------------------
# argslist = titanic

# insertion_query = """
# INSERT INTO titanic
# (id, Survived, Pclass, Name, Sex, Age, Siblings_Spouses,
# Parents_Children, Fare)
# VALUES %s
# """
# execute_values(cursor, insertion_query, argslist)
   
cursor.execute('SELECT * from titanic;')
result = cursor.fetchmany(size=5)
print("CHARACTER TABLE:", result)
cursor.execute('SELECT * from titanic;')
result2 = cursor.fetchall()
print("ROW COUNT:", len(result2))

connection.commit()

