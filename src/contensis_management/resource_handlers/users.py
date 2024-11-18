"""User methods for the Contensis Security API."""

import http
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

    def is_in_groups(self, user_id: str, group_names: str) -> bool:
        """Is the user in these groups.

        No content should be returned, only the status code.  If the user is in the
        group(s) the status code will be 204 (success but no content).
        """
        url = f"/api/security/users/{user_id}/groups/{group_names}"
        the_api_response = self.client.head(url=url)
        return (
            the_api_response.status_code == http.HTTPStatus.NO_CONTENT
            and not the_api_response.json_data
        )
