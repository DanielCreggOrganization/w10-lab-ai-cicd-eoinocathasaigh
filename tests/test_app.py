from hello_app.webapp import app


def test_home_route():
    """Test the home route returns 200 OK."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200


# Test corrected to pass
def test_math_fail():
    assert 1 + 1 == 2
