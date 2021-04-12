from domain.types import *

def create_item_object(item):
    try:
        item_class = item["name"]
    except KeyError:
        item_class = "NormalItem"
    finally:
        return eval(item_class + "(" + item["name"] + ", " + str(item["sell_in"]) + ", " + str(item["quality"]) + ")")