from services.db import data_base
from repository.models import Guilded_rose
from app import *  # OUT OF CONTEXT
import pytest
from controller.factory import create_app



@pytest.mark.db
def test_delete_item():  # METHOD TEST
    db = "ollivanders-test"
    host = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/ollivanders-test?retryWrites=true&w=majority"
    app = create_app(db, host)
    
    item = {"name": "ItemFake", "sell_in": 12, "quality": 12}
    assert data_base.delete_item(item, DB, HOST) == ("The specified item does not exist")


@pytest.mark.db
def test_get_item_by_sell(client):  # API ROUTE TEST
    rv = client.get("/items/sell_in/6")
    assert b'{"items":[{"name":"Backstage","quality":33,"sell_in":6}]}' in rv.data


@pytest.mark.db
def test_get_item_by_quality(client):  # API ROUTE TEST
    rv = client.get("/items/quality/33")
    assert b'{"items":[{"name":"Backstage","quality":33,"sell_in":6}]}' in rv.data


@pytest.mark.db
def test_get_item_by_name(client):  # API ROUTE TEST
    rv = client.get("/items/NormalItem")
    assert b'{"name":"NormalItem","quality":0,"sell_in":-4}' in rv.data
