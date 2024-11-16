"""Contensis API client module."""

import logging

from contensis_management import request_handler_abc, projects

LOGGER = logging.getLogger(__name__)


class ApiClient:
    """A class to authenticate with the Contensis API."""

    def __init__(
        self,
        the_handler: request_handler_abc.RequestHandlerABC,
        alias: str,
        username: str,
        password: str,
    ):
        self.the_handler = the_handler
        self.alias = alias
        self.base_url = f"https://cms-{alias}.cloud.contensis.com"
        self.token = self._authenticate(username, password)
        # Initialize grouped resources
        self.projects = projects.Projects(self)

    def _authenticate(self, username, password):
        """Authenticate with the Contensis API and return the token."""
        url = f"{self.base_url}/authenticate/connect/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        data = {
            "scope": (
                "openid offline_access Security_Administrator "
                "ContentType_Read ContentType_Write ContentType_Delete "
                "Entry_Read Entry_Write Entry_Delete Project_Read Project_Write "
                "Project_Delete Workflow_Administrator"
            ),
            "grant_type": "contensis_classic",
            "username": username,
            "password": password,
        }
        api_response = self.the_handler.post(url=url, headers=headers, data=data)
        if api_response.json_data.get("error") or api_response.status_code != 200:
            LOGGER.error("Error authenticating with the Contensis API.")
            raise PermissionError(api_response.json_data)
        return api_response.json_data["access_token"]

    def get(self, url: str):
        """Send a GET request to the specified URL."""
        headers = {"Authorization": f"Bearer {self.token}"}
        return self.the_handler.get(url=f"{self.base_url}{url}", headers=headers)
