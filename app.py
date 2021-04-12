from flask import Flask, render_template, redirect
from services.db import data_base as db
from services.db_engine import init_app
from services.update_quality import update_quality
import json

app = Flask(__name__)
init_app(app)

# GET

@app.route('/')
def ping():
    # devuelve el archivo especificado
    # return db.ping()
    return render_template('index.html')

@app.route('/wellcome')
def wellcome():
    # devuelve el archivo especificado
    return db.ping()

@app.route('/items', methods=['GET'])
def get_items():
    return db.get_items()

@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    return db.get_item(name)
    
@app.route('/test', methods=['GET'])
def test():
    return update_quality()
    

@app.route('/items/update', methods=['GET'])
def update_item():
    db.update_quality()
    return redirect("../items", code=302)

# POST

@app.route('/items/add/<string:item>', methods=['POST'])
def add_item(item):
    return db.add_item(json.loads(item))

@app.route('/items/delete/<string:item>', methods=['POST'])
def delete_item(item):
    return db.delete_item(json.loads(item))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)