import pytest
from flask import g
from mongoengine import connect

from controller.factory import create_app
from repository.models import Guilded_rose
from services.db_engine import items


@pytest.fixture(autouse=True)
def client():
    db = "ollivanders-test"
    host = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/ollivanders-test?retryWrites=true&w=majority"
    app = create_app(db, host)
    app.app_context().push()
    SetupTestDB.init_mock_db()
    return app.test_client()


class SetupTestDB:

    @staticmethod
    def get_db():
        '''
        Se conecta a una base de datos destinada a ser testeada y la devuelve al objeto grlobal g de Flask
        '''
        if "db" not in g:
            g.db = connect(
                db="ollivanders-test",
                host="mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/ollivanders-test?retryWrites=true&w=majority",
            )
            g.Guilded_rose = Guilded_rose
        return g.db

    @staticmethod
    def init_mock_db():
        '''
            Crea una base de datos moqueada
        '''
        db = SetupTestDB.get_db()
        Guilded_rose.drop_collection()
        for item in items:
            Guilded_rose(
                name=item["name"],
                sell_in=item["sell_in"],
                quality=item["quality"],
            ).save()