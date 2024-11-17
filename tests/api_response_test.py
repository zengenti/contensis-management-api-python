"""Just confirm that the dataclass has the expected properties."""

import http

from contensis_management import api_response


def test_api_response():
    """Make sure the ApiResponse dataclass has the expected properties."""
    # Act
    response = api_response.ApiResponse(
        status_code=200,
        json_data={"key": "value"},
        headers={"header": "value"},
    )
    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert response.json_data == {"key": "value"}
    assert response.headers == {"header": "value"}
