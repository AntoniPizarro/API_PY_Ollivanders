from flask import Flask, render_template
from services.db import data_base as db
from services.db_engine import init_app

def crate_app():
    app = Flask(__name__)

    @app.route('/')
    def ping():
        # devuelve el archivo especificado
        # return db.ping()
        return render_template('index.html')

    @app.route('/wellcome')
    def wellcome():
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

    init_app(app)

    return app