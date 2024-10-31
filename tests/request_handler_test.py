"""Confirm that the request handler works as expected.

Using responses to provide a mock response from the requests library.  This is the only
point we are using responses.  The RequestHandler class should be a dependency of the
ApiClient class so a mock RequestHandler can be passed in for testing.
"""

import responses

from contensis_management import api_response, request_handler


@responses.activate
def test_get_request() -> None:
    """Test the get method of the RequestHandler class."""
    # Arrange
    url = "http://a-dummy.com"
    data = {"ok": True, "msg": "Hello, world!"}
    responses.add(responses.GET, url, json=data)
    handler = request_handler.RequestHandler()
    # Act
    response = handler.get(url=url)
    # Assert
    assert isinstance(response, api_response.ApiResponse)
    assert response.status_code == 200
    assert response.json_data == {"ok": True, "msg": "Hello, world!"}


@responses.activate
def test_post_request() -> None:
    """Test the post method of the RequestHandler class."""
    # Arrange
    url = "http://another-dummy.com"
    headers = {"Content-Type": "application/json"}
    data = {"ok": True, "msg": "Hello there!"}
    responses.add(responses.POST, url, json=data)
    handler = request_handler.RequestHandler()
    # Act
    response = handler.post(url, headers=headers)
    # Assert
    assert isinstance(response, api_response.ApiResponse)
    assert response.status_code == 200
    assert response.json_data == data
