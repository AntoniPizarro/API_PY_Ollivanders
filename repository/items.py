from mongoengine import *

items = [
    {"code" : "4mRXZNNF", "name" : "Monitor", "price" : 49.99},
    {"code" : "cda7lZO8", "name" : "Teclado", "price" : 27.95},
    {"code" : "Q06UMEHV", "name" : "Raton", "price" : 15.20},
    {"code" : "rCq7LcLD", "name" : "Altavoces", "price" : 84.99},
    {"code" : "x6pb9VYO", "name" : "Micro", "price" : 34.95}
]

class Guilded_Rose(Document):
    name = StringField()
    price = FloatField()
    code = StringField(required=True)