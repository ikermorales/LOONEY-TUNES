
from pymongo import MongoClient
def get_database():
 
   CONNECTION_STRING = "mongodb+srv://Sei:SeitxoUno@cluster2.1u1bp7d.mongodb.net/Usuarios"
  
   # Create a connection
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['users']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":     
   dbname = get_database()

dbname = get_database()
collection_name = dbname["user_1_items"]

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}
collection_name.insert_one(item_1)