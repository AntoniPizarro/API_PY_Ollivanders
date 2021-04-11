from flask import Flask, render_template
from services.db import data_base as db
from services.db_engine import init_app

app = Flask(__name__)
init_app(app)

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
def getItems():
    return db.get_items()

@app.route('/items/<string:name>', methods=['GET'])
def getItem(name):
    return db.get_item(name)

@app.route('/items', methods=['POST'])
def addItem():
    return db.add_item("pescado", 12.43, "jhutpn85")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5500)