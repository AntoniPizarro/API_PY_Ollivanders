import pytest
from controller.factory import createApp
@pytest.fixture
def client():
    app = createApp()
    return app.test_client()