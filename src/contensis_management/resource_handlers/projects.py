"""Project methods for the Contensis Management API."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # to avoid circular imports.
    from contensis_management import api_client


class Projects:
    """A class to handle projects in the Contensis Management API."""

    def __init__(self, the_api_client: "api_client.ApiClient"):
        """Initialize the Projects class."""
        self.client = the_api_client

    def get(self, project_id: str):
        """Get a project from the Contensis Management API."""
        return self.client.get(f"/api/management/projects/{project_id}")

    def list(self):
        """Get a list of the projects in the Contensis Management API."""
        return self.client.get("/api/management/projects/")
