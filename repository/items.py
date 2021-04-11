from mongoengine import *

class Guilded_rose(Document):
    name = StringField()
    price = FloatField()
    code = StringField(required=True)
    def to_json(self):
        return {"name": self.name,
                "price": self.price,
                "code": self.code}