from services.db import data_base
from app import * #OUT OF CONTEXT
import pytest


@pytest.mark.db
def test_get_item(client):
    rv = client.get('/items/NormalItem')
    assert b'{"name": "NormalItem", "quality": 0, "sell_in": -1}' in rv.data 
