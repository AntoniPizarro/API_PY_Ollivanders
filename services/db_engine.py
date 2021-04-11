import click
from mongoengine import *
from flask.cli import with_appcontext
from flask import g

from repository.items import Guilded_rose

def get_bd():
    if 'db' not in g:
        g.db = connect(
            db="ollivanders",
            host="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/ollivanders?retryWrites=true&w=majority",
        )
        g.Guilded_rose = Guilded_rose
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_bd()
    items = [
        {"quality" : 5, "name" : "Teclado", "sell_in" : 27},
        {"quality" : 8, "name" : "Raton", "sell_in" : 15},
        {"quality" : 43, "name" : "Monitor", "sell_in" : 49},
        {"quality" : 50, "name" : "Altavoces", "sell_in" : 84},
        {"quality" : 21, "name" : "Micro", "sell_in" : 34}
    ]
    for item in items:
        print(item)
        Guilded_rose(
            name=item["name"], sell_in=item["sell_in"], quality=item["quality"]
        ).save()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Data Base initialized")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)