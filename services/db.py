from repository.items import items
from flask import request, jsonify

class baseDatos:

    @staticmethod
    def ping():
        return jsonify({"Wellcome" : " Ollivanders!"})
    
    @staticmethod
    def getItems():
        return jsonify({"items" : items})
    
    @staticmethod
    def getItem(name):
        def itemNameVeri(item, name):
            if item["name"] == name:
                return True
            elif item["name"].lower() == name.lower():
                return True
            else:
                return False
        prods = [prod for prod in items if itemNameVeri(prod, name) == True]
        if len(prods) > 0:
            return jsonify({"items" : prods})
        else:
            return jsonify({"items" : "No hay datos"})
    
    @staticmethod
    def addItem():
        items.append(request.json)
        return jsonify({"items" : items})