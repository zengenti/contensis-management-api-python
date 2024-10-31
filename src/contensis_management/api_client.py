""""""

import logging

import requests

LOGGER = logging.getLogger(__name__)


class ApiClient:
    """A class to authenticate with the Contensis API."""

    BASE_URL = "https://cms-develop.cloud.contensis.com"

    def __init__(self, username, password):
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

        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()

        # Assuming token is returned in response.json()["access_token"]
        return response.json().get("access_token")
