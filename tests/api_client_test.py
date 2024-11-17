"""Confirm that the API client can authenticate and return a token."""

import pytest

from contensis_management import (
    api_client,
    api_response,
    request_handler_abc,
)


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
    client = api_client.ApiClient(mock_request_handler)
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
    # Act
    with pytest.raises(PermissionError) as got_an_error:
        api_client.ApiClient(mock_request_handler)
    # Assert
    assert got_an_error is not None
