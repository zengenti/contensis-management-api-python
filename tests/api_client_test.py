""""""

from contensis_management import api_client
from tests.helper_config import env_config


def test_api_client() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    username = env_config.username
    password = env_config.password
    client = api_client.ApiClient(username, password)
    # # Act
    token = client.token
    # Assert
    assert token is not None
