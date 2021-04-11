from flask import request, jsonify, g
from services.db_engine import get_bd
from repository.items import Guilded_rose

class data_base:

    @staticmethod
    def ping():
        return jsonify({"Wellcome" : " Ollivanders!"})
    
    @staticmethod
    def get_items():
        db = get_bd()
        items_list = []
        for object in g.Guilded_rose.objects():
            items_list.append(object.to_json())
        if len(items_list) > 0:
            return jsonify({"items" : items_list})
        else:
            return jsonify({"items" : "N/A"})
    
    @staticmethod
    def get_item(name):
        db = get_bd()
        items_list = []
        items_list_name = []
        for object in g.Guilded_rose.objects():
            items_list.append(object.to_json())
        for item in items_list:
            if item["name"].lower() == name.lower():
                items_list_name.append(item)
        if len(items_list_name) > 0:
            return jsonify({"items" : items_list_name})
        else:
            return jsonify({"items" : "N/A"})
    
    @staticmethod
    def add_item(name, price, code):
        db = get_bd()
        item = {"name" : name, "price" : price, "code" : code}
        Guilded_rose(
            name=item["name"], price=item["price"], code=item["code"]
        ).save()