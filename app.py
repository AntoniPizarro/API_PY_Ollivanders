from flask import Flask, redirect
from services.db import data_base as db
from services.db_engine import init_app
import json

app = Flask(__name__)
init_app(app)


# GET

@app.route('/')
def ping():
    return db.ping()

@app.route('/wellcome')
def wellcome():
    return db.ping()

@app.route('/items', methods=['GET'])
def get_items():
    return db.get_items()

@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    return db.get_item(name)

@app.route('/items/sell_in/<string:sell_in>', methods=['GET'])
def get_item_by_sell_in(sell_in):
    return db.get_item_by_sell_in(sell_in)

@app.route('/items/quality/<string:quality>', methods=['GET'])
def get_item_by_quality(quality):
    return db.get_item_by_quality(quality)    

@app.route('/items/update', methods=['GET'])
def update_item():
    db.update_quality()
    return redirect("../items", code=302)


# POST

@app.route('/items/add/<string:item>', methods=['POST'])
def add_item(item):
    db.add_item(json.loads(item))
    return redirect("../../items", code=302)

@app.route('/items/delete/<string:item>', methods=['POST'])
def delete_item(item):
    db.delete_item(json.loads(item))
    return redirect("../../items", code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)