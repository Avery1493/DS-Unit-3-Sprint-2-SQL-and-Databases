
# python app/titanic_nosql.py

from dotenv import load_dotenv
import os
import pymongo 

import pandas as pd
import json

# LOAD MONGO DATABASE ENV VARS FROM ".env" FILE
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="Oooops")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="Oooops")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="Oooops")

# ESTABLISH MONGODB CONNECTION WITH f string
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

# DATABASE
db = client.rpg_database 
print("----------------")
print("DB:", type(db), db)

# CREATE COLLECTION
collection = db.titanic
print("----------------")
print("COLLECTION:", type(collection), collection)

print("DOCS:", collection.count_documents({}))

# load titanic dataset (csv file)
CSV_FILEPATH = "https://raw.githubusercontent.com/Avery1493/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv"
df = pd.read_csv(CSV_FILEPATH)

print(df.shape)
print(df.head())
column_names = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 
'Siblings_Spouses', 'Parents_Children', 'Fare']
df.columns = column_names
print(df.columns)
print(df.dtypes)

# Convert Titanic JSON
data = json.loads(df.T.to_json()).values()
print(data)
print(type(data))
print("--Hello Solar System--")

# INSERT MANY DOCUMENT INTO COLLECTION
# collection.insert_many(data)

print("DOCS:", collection.count_documents({})) # select *

# #print("EXP OVER 0:", collection.count_documents({"exp":{"$gt":0}}))