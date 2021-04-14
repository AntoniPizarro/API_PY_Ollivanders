from domain.types import *


def create_item_object(item):
    types = ["NormalItem", "AgedBrie", "ConjuredItem", "Sulfuras", "Backstage"]
    item_class = ""
    try:
        item_class = types[types.index(item["name"])]
    except ValueError:
        item_class = "NormalItem"
    finally:
        print(item_class + "(\"" + item["name"] + "\", " + str(item["sell_in"]) + ", " + str(item["quality"]) + ")")
        return eval(item_class + "(\"" + item["name"] + "\", " + str(item["sell_in"]) + ", " + str(item["quality"]) + ")")
