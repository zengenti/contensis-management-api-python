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

    def get(self, user_id: str) -> user.User:
        """Get a single user from the Contensis Security API."""
        url = f"/api/security/users/{user_id}"
        the_api_response = self.client.get(url=url)
        the_user = the_api_response.json_data
        return user.User(**the_user)

    def list(self) -> List[Any]:
        """Get a list of the users from the Contensis Security API."""
        url = "/api/security/users/"
        the_api_response = self.client.get(url=url)
        the_user_list = the_api_response.json_data["items"]
        return [user.User(**item) for item in the_user_list]

    def permissions(self, user_id: str, group_names: str):
        """Get a list of the permissions for a user from the Contensis Security API."""
        url = f"/api/security/users/{user_id}/groups/{group_names}"
        the_api_response = self.client.get(url=url)
        return the_api_response.json_data
