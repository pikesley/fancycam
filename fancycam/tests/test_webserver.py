from fancycam import app


def test_get_root():
    """Test the `/` path."""
    response = app.test_client().get("/")
    assert response.status_code == 200
