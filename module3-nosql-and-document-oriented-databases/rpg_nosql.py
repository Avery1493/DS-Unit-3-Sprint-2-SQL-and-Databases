
# python app/rpg_nosql.py

from dotenv import load_dotenv
import os
import pymongo 

import sqlite3
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

# CREATE DATABASE
db = client.rpg_database 
print("----------------")
print("DB:", type(db), db)

# CREATE COLLECTION
collection = db.charactercreator_character
print("----------------")
print("COLLECTION:", type(collection), collection)

print("DOCS:", collection.count_documents({}))

# Retrieve RPG JSON file
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"character_table.json")
with open(DB_FILEPATH) as char:
    data = json.load(char)

#print(data)

# # INSERT MANY DOCUMENT INTO COLLECTION
# collection.insert_many(data)

print("DOCS:", collection.count_documents({})) # select *

print("EXP OVER 0:", collection.count_documents({"exp":{"$gt":0}}))
#print("STRENGTH OVER 0 AND EXP = 0:", collection.count_documents({"strength":{"$gt":0}}, "$and", {"exp":{"$eq":0}}))