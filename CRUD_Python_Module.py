# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host='localhost', port=27017, db='aac', col='animals'): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacUser' 
        PASS = 'password' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.collection.insert_one(data)  # data should be dictionary 
            print("Insert Success")            
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            
        try:
            self.collection.insert_one(data)  # data should be dictionary 
            print("Insert Success")
            return true
        except Exception as e:
            return f"Error: {e}"
            
    # read a single doc
    def get_animal_details(self, query):
        try: 
            doc = self.collection.find(query)
            if doc:
                return list(doc)
            else:
                return "Nothing found"   
        except Exception as e:
            return f"Error: {e}"
        
    def read(self, query):
        return self.get_animal_details(query)
        
    def update_animal_detail(self, query, update_query):
        try:
            doc = self.collection.update_one(query, update_query)
            if doc.modified_count > 0:
                return f"There was {doc.modified_count} detail updated"
                
            else:
                return "Nothing found"   
        except Exception as e:
            return f"Error: {e}"
        
    def delete_animal(self, query):
        try:
            doc = self.collection.delete_one(query)
            if doc.deleted_count > 0:
                return f"There was {doc.deleted_count} items(s) removed from database."
            else:
                return "No documents matched the query."
        except Exception as e:
            return f"Error: {e}"
        
        
addNewAnimal = {
     "rec_num": 22,
    "age_upon_outcome": '5 years',
    "animal_id": 'A615748',
    "animal_type": 'Dog',
    "breed": 'Labrador Retriever Mix',
    "color": 'Black',
    "date_of_birth": '2009-12-11',
    "datetime": '2015-10-26 18:13:00',
    "monthyear": '2015-10-26T18:13:00',
    "name": 'ChowMell',
    "outcome_subtype": 'Normal',
    "outcome_type": 'Alive',
    "sex_upon_outcome": 'Neutered Male',
    "location_lat": 30.7172069757685,
    "location_long": -97.2952833147647,
    "age_upon_outcome_in_weeks": 306.537003968254
  }

#aac_shelter = AnimalShelter(username, password)
#insert_animal = aac_shelter.create(addNewAnimal)

# Create method to implement the R in CRUD.

#query = {"breed": "Labrador Retriever Mix"}
#doc = aac_shelter.get_animal_details(query)
#print(doc)

#update_query =  { "$set": {"breed": "Chihuaha Mix"}}
#updatedAnimal = aac_shelter.update_animal_detail(query, update_query)
#print(updatedAnimal)
                 
#deleteAnimal = aac_shelter.delete_animal(query)
#print(deleteAnimal)