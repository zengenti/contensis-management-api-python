"""Project methods for the Contensis Management API."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # to avoid circular imports.
    from contensis_management import api_client


class Projects:
    """A class to handle projects in the Contensis Management API."""

    def __init__(self, the_api_client: "api_client.ApiClient"):
        self.client = the_api_client

    def list(self):
        """Get a list of the projects in the Contensis Management API."""
        return self.client.get("/api/management/projects/")
