import pytest

@pytest.mark.wellcome
def test_wellcome(client):
    rv = client.get("/wellcome") 
    assert b'{"Wellcome":" Ollivanders!"}' in rv.data