from flask import Flask
from repository.items import items
from services.db import baseDatos as db

app = Flask(__name__)

@app.route('/wellcome')
def ping():
    return db.ping()

@app.route('/items', methods=['GET'])
def getItems():
    return db.getItems()

@app.route('/items/<string:name>', methods=['GET'])
def getItem(name):
    return db.getItem(name)

@app.route('/items', methods=['POST'])
def addItem():
    return db.addItem()



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)