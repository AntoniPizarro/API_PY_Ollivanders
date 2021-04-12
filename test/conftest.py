import pytest
from controller.factory import crate_app
@pytest.fixture
def client():
    app = crate_app()
    return app.test_client()