"""Confirm that the users resource handler works as expected."""

import http

from contensis_management import (
    api_client,
    api_response,
    request_handler_abc,
)
from contensis_management.resource_handlers import users

mock_users_json: list[dict] = [
    {
        "created": "2024-09-03T09:51:20.113Z",
        "credentials": {
            "passwordChangeFrequency": 180,
            "provider": {"name": "contensis", "type": "contensis"},
        },
        "custom": {},
        "email": "alice@zengenti.com",
        "expiry": "2029-09-03T09:51:20.113",
        "failedLoginAttempts": 0,
        "failedLoginAttemptsSinceLastSuccess": 0,
        "firstName": "",
        "id": "209e4053-f71b-45a9-ba87-3f5595caaeee",
        "language": "en-GB",
        "lastFailedLogin": None,
        "lastLogin": None,
        "lastName": "",
        "modified": "2024-09-03T09:51:20.113Z",
        "optOutOfNotifications": False,
        "passwordChanged": "2024-09-03T09:51:20.113Z",
        "status": {"locked": False, "passwordResetRequired": False, "suspended": False},
        "successfulLoginAttempts": 0,
        "timezone": "Etc/UTC",
        "username": "Alice",
    },
    {
        "created": "2024-09-02T12:11:49.46Z",
        "credentials": {
            "passwordChangeFrequency": 180,
            "provider": {"name": "contensis", "type": "contensis"},
        },
        "custom": {},
        "email": "bob@zengenti.com",
        "expiry": "2029-09-02T12:11:49.46",
        "failedLoginAttempts": 0,
        "failedLoginAttemptsSinceLastSuccess": 0,
        "firstName": "",
        "id": "6ec2d6d8-0947-4322-ba08-5624a8206a00",
        "language": "en-GB",
        "lastFailedLogin": None,
        "lastLogin": None,
        "lastName": "",
        "modified": "2024-09-02T12:11:49.46Z",
        "optOutOfNotifications": False,
        "passwordChanged": "2024-09-02T12:11:49.46Z",
        "status": {"locked": False, "passwordResetRequired": False, "suspended": False},
        "successfulLoginAttempts": 0,
        "timezone": "Etc/UTC",
        "username": "Bob",
    },
    {
        "created": "2024-07-15T13:47:45.373Z",
        "credentials": {
            "passwordChangeFrequency": 0,
            "provider": {"name": "contensis", "type": "contensis"},
        },
        "custom": {
            "defaultView": "dashboard",
            "earlyAccess_websiteUptimeReporting": "no",
            "relationshipStatus": "0",
        },
        "email": "carol@zengenti.com",
        "expiry": None,
        "failedLoginAttempts": 0,
        "failedLoginAttemptsSinceLastSuccess": 0,
        "firstName": "David",
        "id": "7bdd3065-a4c3-4b61-8154-43ebc266f4ec",
        "language": "en-GB",
        "lastFailedLogin": None,
        "lastLogin": "2024-09-11T08:48:14.443Z",
        "lastName": "Davids",
        "modified": "2024-07-15T13:47:45.373Z",
        "optOutOfNotifications": False,
        "passwordChanged": None,
        "status": {"locked": False, "passwordResetRequired": False, "suspended": False},
        "successfulLoginAttempts": 0,
        "timezone": "Europe/Paris",
        "username": "Carol",
    },
]

mock_paged_users_json: dict = {
    "items": mock_users_json,
    "pageCount": 1,
    "pageIndex": 0,
    "pageSize": 25,
    "totalCount": 3,
}


class MockRequestHandlerSuccessful(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        return api_response.ApiResponse(
            status_code=200, json_data={"access_token": "mock_token"}
        )

    def get(self, url, headers=None):
        """Return a list of projects."""
        return api_response.ApiResponse(
            json_data=mock_paged_users_json, status_code=http.HTTPStatus.OK
        )


def test_list_users() -> None:
    """Test the list users with a mock resource handler."""
    # Arrange
    mock_request_handler = MockRequestHandlerSuccessful()
    client = api_client.ApiClient(mock_request_handler)
    users_handler = users.Users(client)
    # Act
    the_users = users_handler.list()
    # Assert
    the_number_of_users = 3
    assert len(the_users) == the_number_of_users
