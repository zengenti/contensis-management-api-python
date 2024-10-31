"""Abstract base class for RequestHandler classes.

This is so the RequestHandler classes can be easily swapped out for testing.
"""

from abc import ABC, abstractmethod

from contensis_management import api_response


class RequestHandlerABC(ABC):
    """Abstract base class for RequestHandler classes."""

    @abstractmethod
    def post(self, url: str, json=None, headers=None) -> api_response.ApiResponse:
        """Send a POST request to the specified URL."""

    @abstractmethod
    def get(self, url: str, headers=None) -> api_response.ApiResponse:
        """Send a GET request to the specified URL."""
