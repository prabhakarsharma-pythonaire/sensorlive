import pymongo
from pymongo import MongoClient

connection_string = "mongodb+srv://prabhakarkumar313:9571002370@cluster0.kztw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
print("hel")
print(client.list_database_names())
db = client["machinelearningdb"]
