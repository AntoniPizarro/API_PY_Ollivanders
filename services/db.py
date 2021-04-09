from repository.items import items
from flask import request, jsonify, g
from services.db_engine import get_db

class data_base:

    @staticmethod
    def ping():
        return jsonify({"Wellcome" : " Ollivanders!"})
    
    @staticmethod
    def getItems():
        
        return jsonify({"items" : items})
    
    @staticmethod
    def get_item(name):
        database = get_db()
        items = []
        print(g)
        for item in g.guilded_rose.objects(name=name):
            items.append(item)
        if len(items) < 1:
            return {"items":"N/A"}
        else:
            return items 
    
    @staticmethod
    def addItem():
        items.append(request.json)
        return jsonify({"items" : items})