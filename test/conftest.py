import pytest
from flask import g
from mongoengine import connect

from controller.factory import create_app
from repository.models import Guilded_rose
from repository.db_engine import items


@pytest.fixture(autouse=True)
def client():
    app = create_app()
    app.app_context().push()
    SetupTestDB.init_mock_db()
    return app.test_client()


class SetupTestDB:

    @staticmethod
    def get_db():
        g.db = connect("dbtest", host="database://localhost")
        g.Guilded_rose
        return g.db

    @staticmethod
    def init_mock_db():
        db = SetupTestDB.get_db()
        Guilded_rose.drop_collection()
        for item in items:
            Guilded_rose(
                name=item["name"],
                sell_in=item["sell_in"],
                quality=item["quality"],
            ).save()