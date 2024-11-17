"""User methods for the Contensis Security API."""

from typing import TYPE_CHECKING, Any, List

from contensis_management.models import user

if TYPE_CHECKING:  # to avoid circular imports.
    from contensis_management import api_client


class Users:
    """A class to handle users in the Contensis Security API."""

    def __init__(self, the_api_client: "api_client.ApiClient"):
        """Initialize the Users class."""
        self.client = the_api_client

    def get(self, user_id: str):
        """Get a user from the Contensis Security API."""
        return self.client.get(f"/api/management/users/{user_id}")

    def list(self) -> List[Any]:
        """Get a list of the users from the Contensis Security API."""
        url = "/api/security/users/"
        the_api_response = self.client.get(url=url)
        the_user_list = the_api_response.json_data["items"]
        return [user.User(**item) for item in the_user_list]
