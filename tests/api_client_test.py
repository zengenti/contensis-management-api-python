""""""

from contensis_management import (
    api_client,
    api_response,
    request_handler,
    request_handler_abc,
)
from tests.helper_config import env_config


class MockRequestHandler(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, json=None, headers=None):
        return api_response.ApiResponse(
            json_data={"token": "mocked-token"}, status_code=200
        )

    def get(self, url, headers=None):
        raise NotImplementedError("This should not have been called.")


def test_api_client_success() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = MockRequestHandler()
    alias = "dummy-alias"
    username = "dummy-username"
    password = "dummy-password"
    client = api_client.ApiClient(mock_request_handler, alias, username, password)
    # # Act
    token = client.token
    # Assert
    assert token is not None


def test_api_client_failure() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = request_handler.RequestHandler()
    alias = "develop"
    username = env_config.username
    password = env_config.password
    client = api_client.ApiClient(mock_request_handler, alias, username, password)
    # Act
    token = client.token
    # Assert
    assert token is not None
