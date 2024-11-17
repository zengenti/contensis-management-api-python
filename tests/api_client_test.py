"""Confirm that the API client can authenticate and return a token."""

import pytest

from contensis_management import (
    api_client,
    api_response,
    request_handler,
    request_handler_abc,
)
from tests.helper_config import env_config


class MockRequestHandlerSuccessful(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        mock_token = "a" * 1100
        return api_response.ApiResponse(
            status_code=200, json_data={"access_token": mock_token}
        )

    def get(self, url, headers=None):
        """Do nothing."""
        raise NotImplementedError("This should not have been called.")


def test_api_client_success() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = MockRequestHandlerSuccessful()
    alias = "dummy-alias"
    username = "dummy-username"
    password = "dummy-password"
    client = api_client.ApiClient(mock_request_handler, alias, username, password)
    # # Act
    token = client.token
    # Assert
    assert token is not None
    # and it should be huge.
    a_big_number = 1000  # Tokens seem to be about 1125 characters long.
    assert len(token) > a_big_number


class MockRequestHandlerFailure(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        return api_response.ApiResponse(
            json_data={"error": "IncorrectUsernameorPassword"}, status_code=400
        )

    def get(self, url, headers=None):
        """Do nothing."""
        raise NotImplementedError("This should not have been called.")


def test_api_client_failure() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = MockRequestHandlerFailure()
    alias = "dummy-alias"
    username = "not-the-username"
    password = "not-the-password"
    # Act
    with pytest.raises(PermissionError) as got_an_error:
        api_client.ApiClient(mock_request_handler, alias, username, password)
    # Assert
    assert got_an_error is not None


def api_client_for_real() -> None:
    """Genuine test of the API client for debugging."""
    # Arrange
    alias = env_config.alias
    username = env_config.username
    password = env_config.password
    handler = request_handler.RequestHandler()
    # Act
    client = api_client.ApiClient(handler, alias, username, password)
    # Assert
    assert client.token is not None
    a_big_number = 1000  # Tokens seem to be about 1125 characters long.
    assert len(client.token) > a_big_number
