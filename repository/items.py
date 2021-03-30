from pymongo import MongoClient

def insert():
    cliente = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/?retryWrites=true&w=majority')
    db = cliente['ollivanders']
    for item in items:
        doc = db.guilded_rose.find(item["code"])
        if doc.count() == 0:
            db.guilded_rose.insert_one(item)