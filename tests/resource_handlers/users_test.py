"""Confirm that the users resource handler works as expected."""

from contensis_management import (
    api_client,
    request_handler,
)
from contensis_management.resource_handlers import users
from tests.helper_config import env_config


def list_users_for_real() -> None:
    """Genuine test of the list of users resource handler for debugging."""
    # Arrange
    alias = env_config.alias
    username = env_config.username
    password = env_config.password
    handler = request_handler.RequestHandler()
    client = api_client.ApiClient(handler, alias, username, password)
    users_handler = users.Users(client)
    # Act
    the_users = users_handler.list()
    # Assert
    assert the_users is not None
