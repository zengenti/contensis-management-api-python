"""Contensis API client module."""

import logging

from contensis_management import request_handler_abc

LOGGER = logging.getLogger(__name__)


class ApiClient:
    """A class to authenticate with the Contensis API."""

    BASE_URL = "https://cms-develop.cloud.contensis.com"

    def __init__(
        self,
        the_handler: request_handler_abc.RequestHandlerABC,
        username: str,
        password: str,
    ):
        self.the_handler = the_handler
        self.token = self.authenticate(username, password)

    def authenticate(self, username, password):
        """Authenticate with the Contensis API and return the token."""
        url = f"{self.BASE_URL}/authenticate/connect/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        data = {
            "scope": "openid offline_access Security_Administrator ContentType_Read ContentType_Write ContentType_Delete Entry_Read Entry_Write Entry_Delete Project_Read Project_Write Project_Delete Workflow_Administrator",
            "grant_type": "contensis_classic",
            "username": username,
            "password": password,
        }
        return self.the_handler.post(url, data, headers)
