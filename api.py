from flask import Flask, jsonify, request
from domain.items import items

app = Flask(__name__)

@app.route('/wellcome')
def ping():
    return jsonify({"Wellcome" : " Ollivanders!"})

@app.route('/items', methods=['GET'])
def getItems():
    return jsonify({"items" : items})

@app.route('/items/<string:name>', methods=['GET'])
def getItem(name):
    prods = [prod for prod in items if itemNameVeri(prod, name) == True]
    if len(prods) > 0:
        return jsonify({"items" : prods})
    else:
        return jsonify({"items" : "No hay datos"})

@app.route('/items', methods=['POST'])
def addItem():
    items.append(request.json)
    return jsonify({"items" : items})

def itemNameVeri(item, name):
    if item["name"] == name:
        return True
    elif item["name"].lower() == name.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)