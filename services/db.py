from flask import jsonify, g
from services.db_engine import get_bd
from repository.models import Guilded_rose
from mongoengine.queryset.visitor import Q
from controller.create_item_object import create_item_object


class data_base:
    @staticmethod
    def ping():
        return jsonify({"Wellcome": " Ollivanders!"})

    @staticmethod
    def get_items(db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Guilded_rose.objects():
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def get_item(name, db, url):
        db = get_bd(db, url)
        items_list = []
        items_list_name = []
        for item in g.Guilded_rose.objects():
            items_list.append(item.to_json())
        for item in items_list:
            if item["name"].lower() == name.lower():
                items_list_name.append(item)
        if len(items_list_name) > 0:
            return jsonify({"items": items_list_name})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def add_item(args, db, url):
        db = get_bd(db, url)
        item = {
            "name": args["name"],
            "sell_in": args["sell_in"],
            "quality": args["quality"],
        }
        Guilded_rose(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        ).save()
        print("item added")

    @staticmethod
    def delete_item(item, db, url):
        db = get_bd(db, url)
        item = g.Guilded_rose.objects(
            Q(name=item["name"])
            & Q(quality=item["quality"])
            & Q(sell_in=item["sell_in"])
        ).first()
        if not item:
            return "The specified item does not exist"
        else:
            item.delete()
            return "Item deleted: " + str(item)

    @staticmethod
    def update_quality(db, url):
        db = get_bd(db, url)
        for item in g.Guilded_rose.objects():
            item_object = create_item_object(item.to_json())
            item_object.update_quality()
            item.sell_in = item_object.sell_in
            item.quality = item_object.quality
            item.save()

    @staticmethod
    def get_item_by_sell_in(sell_in, db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Guilded_rose.objects(sell_in=sell_in):
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def get_item_by_quality(quality, db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Guilded_rose.objects(quality=quality):
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})
