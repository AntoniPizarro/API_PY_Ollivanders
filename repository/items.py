from mongoengine import *

class Guilded_rose(Document):
    name = StringField(required=True)
    sell_in = IntField(required=True)
    quality = IntField(required=True)
    def to_json(self):
        return {"name": self.name,
                "sell_in": self.sell_in,
                "quality": self.quality}