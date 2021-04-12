from flask import jsonify, g
from services.db_engine import get_bd
from repository.models import Guilded_rose
from mongoengine.queryset.visitor import Q
from controller.create_item_object import create_item_object

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
    def add_item(args):
        db = get_bd()
        item = {"name" : args["name"], "sell_in" : args["sell_in"], "quality" : args["quality"]}
        Guilded_rose(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        ).save()
    
    @staticmethod
    def delete_item(item):
        db = get_bd()
        item = g.Guilded_rose.objects(Q(name=item['name'])
                              & Q(quality=item['quality'])
                              & Q(sell_in=item['sell_in'])).first()
        if not item:
            return "The specified item does not exist"
        else:
            item.delete()
            return "Item deleted: " + str(item)
    
    @staticmethod
    def update_quality():
        db = get_bd()
        for item in g.Guilded_rose.objects():
            item_object = create_item_object(item.to_json())
            item_object.update_quality()
            item.sell_in = item_object.sell_in
            item.quality = item_object.quality
            item.save()
