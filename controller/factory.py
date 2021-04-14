from flask import Flask, redirect
from services.db import data_base as db
from services.db_engine import init_app
import json


def create_app(db_name, host):

    DB = db_name
    HOST = host

    app = Flask(__name__)
    init_app(app, DB, HOST)

    # GET

    @app.route("/")
    def ping():
        return db.ping()

    @app.route("/wellcome")
    def wellcome():
        return db.ping()

    @app.route("/items", methods=["GET"])
    def get_items():
        return db.get_items(DB, HOST)

    @app.route("/items/<string:name>", methods=["GET"])
    def get_item(name):
        return db.get_item(name, DB, HOST)

    @app.route("/items/sell_in/<string:sell_in>", methods=["GET"])
    def get_item_by_sell_in(sell_in):
        return db.get_item_by_sell_in(sell_in, DB, HOST)

    @app.route("/items/quality/<string:quality>", methods=["GET"])
    def get_item_by_quality(quality):
        return db.get_item_by_quality(quality, DB, HOST)

    @app.route("/items/update", methods=["GET"])
    def update_item():
        db.update_quality(DB, HOST)
        return redirect("../items", code=302)

    # POST

    @app.route("/items/add/<string:item>", methods=["POST"])
    def add_item(item):
        db.add_item(json.loads(item))
        return redirect("../../items", code=302)

    @app.route("/items/delete/<string:item>", methods=["POST"])
    def delete_item(item):
        db.delete_item(json.loads(item))
        return redirect("../../items", code=302)

    return app
