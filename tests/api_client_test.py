""""""

from contensis_management import api_client, api_response, request_handler_abc
from tests.helper_config import env_config


class MockRequestHandler(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, json=None, headers=None):
        return api_response.ApiResponse(
            json_data={"token": "mocked-token"}, status_code=200
        )

    def get(self, url, headers=None):
        return api_response.ApiResponse(
            json_data={"token": "mocked-token"}, status_code=200
        )


def test_api_client() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    handler = MockRequestHandler()
    username = env_config.username
    password = env_config.password
    client = api_client.ApiClient(handler, username, password)
    # # Act
    token = client.token
    # Assert
    assert token is not None
