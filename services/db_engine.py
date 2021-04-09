import click
from mongoengine import *
from flask.cli import with_appcontext
from flask import g

from repository.items import Guilded_Rose

def get_db():
    if 'db' not in g:
        g.db = connect(
            db="ollivanders",
            host="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/ollivanders?retryWrites=true&w=majority",
        )
    return g.db

def teardown_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    items = [
        {"code" : "4mRXZNNF", "name" : "Monitor", "price" : 49.99},
        {"code" : "cda7lZO8", "name" : "Teclado", "price" : 27.95},
        {"code" : "Q06UMEHV", "name" : "Raton", "price" : 15.20},
        {"code" : "rCq7LcLD", "name" : "Altavoces", "price" : 84.99},
        {"code" : "x6pb9VYO", "name" : "Micro", "price" : 34.95}
    ]
    for item in items:
        Guilded_Rose(
            name=item["name"], price=item["price"], code=item["code"]
        ).save()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Data Base initialized")


def init_app(app):
    app.teardown_appcontext(teardown_db)
    app.cli.add_command(init_db_command)