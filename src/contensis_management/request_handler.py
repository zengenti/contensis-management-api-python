"""Implementation of the RequestHandler class using the requests library."""

import logging

import requests

from contensis_management import api_response, request_handler_abc

LOGGER = logging.getLogger(__name__)


class RequestHandler(request_handler_abc.RequestHandlerABC):
    """A class to handle requests to the Contensis API."""

    timeout = 10

    def get(self, url: str, headers=None) -> api_response.ApiResponse:
        """Send a GET request to the specified URL."""
        response = requests.get(url, headers=headers, timeout=self.timeout)
        return api_response.ApiResponse(
            status_code=response.status_code,
            json_data=response.json(),
            headers=dict(response.headers),
        )

    def post(self, url, json=None, headers=None) -> api_response.ApiResponse:
        """Send a POST request to the specified URL with the specified data."""
        response = requests.post(url, json=json, headers=headers, timeout=self.timeout)
        return api_response.ApiResponse(
            status_code=response.status_code,
            json_data=response.json(),
            headers=dict(response.headers),
        )
