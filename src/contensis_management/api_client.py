"""Contensis API client module."""

import http
import logging

from contensis_management import api_response, request_handler_abc
from contensis_management.resource_handlers import projects, users

LOGGER = logging.getLogger(__name__)


class ApiClient:
    """A class to authenticate with the Contensis API."""

    def __init__(
        self,
        the_handler: request_handler_abc.RequestHandlerABC,
        alias: str = "",
        username: str = "",
        password: str = "",
    ):
        """Initialize the API client."""
        self.the_handler = the_handler
        self.alias = alias
        self.base_url = f"https://cms-{alias}.cloud.contensis.com"
        self.token = self._authenticate(username, password)
        # Initialize grouped resources
        self.projects = projects.Projects(self)
        self.users = users.Users(self)

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
        the_api_response = self.the_handler.post(url=url, headers=headers, data=data)
        if (
            the_api_response.json_data.get("error")
            or the_api_response.status_code != http.HTTPStatus.OK
        ):
            LOGGER.error("Error authenticating with the Contensis API.")
            raise PermissionError(the_api_response.json_data)
        return the_api_response.json_data["access_token"]

    def get(self, url: str) -> api_response.ApiResponse:
        """Send a GET request to the specified URL."""
        headers = {"Authorization": f"Bearer {self.token}"}
        the_api_response = self.the_handler.get(
            url=f"{self.base_url}{url}", headers=headers
        )
        return api_response.ApiResponse(
            status_code=the_api_response.status_code,
            headers=the_api_response.headers,
            json_data=the_api_response.json_data,
        )
