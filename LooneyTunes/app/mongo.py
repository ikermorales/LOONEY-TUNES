from pymongo import MongoClient
from flask import Flask, render_template
app = Flask(__name__)

def get_database():
 
   CONNECTION_STRING = "mongodb+srv://Sei:SeitxoUno@cluster2.1u1bp7d.mongodb.net/Usuarios"
  
   # Create a connection
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   dblist = client.list_database_names()
   if "users" in dblist:
        print("Database exists.")
        return client.users
   else:
        return client['users']
        dbname = get_database()
        collection_name = dbname["users"]