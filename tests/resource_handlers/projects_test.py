"""Confirm that the projects resource handler works as expected."""

from contensis_management import (
    api_client,
    api_response,
    request_handler,
    request_handler_abc,
)
from contensis_management.resource_handlers import projects
from tests.helper_config import env_config

mock_projects_json: list[dict] = [
    {
        "color": "blue",
        "deliverySysExclusions": [],
        "description": "This is the description for the Website project.",
        "id": "website",
        "name": "Website",
        "primaryLanguage": "en-GB",
        "supportedLanguages": ["en-GB", "en-NZ", "en-US", "fr-CA", "de-AT", "de-DE"],
        "uuid": "f12a1234-ebf1-12f5-7f83-f0617f43e6fb",
    },
    {
        "color": "gray",
        "deliverySysExclusions": [],
        "description": "",
        "id": "testNewProject",
        "name": "test new project",
        "primaryLanguage": "en-GB",
        "supportedLanguages": ["en-GB"],
        "uuid": "f1234a89-bcda-9701-4b58-1234c634a26e",
    },
    {
        "color": "green",
        "deliverySysExclusions": [],
        "description": "",
        "id": "danMonolingual",
        "name": "Dan Monolingual",
        "primaryLanguage": "en-GB",
        "supportedLanguages": ["en-GB"],
        "uuid": "4b12345-06d1-97d8-57ef-ad12df847991",
    },
]


class MockRequestHandlerSuccessful(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        return api_response.ApiResponse(
            status_code=200, json_data={"access_token": "mock_token"}
        )

    def get(self, url, headers=None):
        """Return a list of projects."""
        return api_response.ApiResponse(json_data=mock_projects_json, status_code=200)


def test_list_projects() -> None:
    """Test the list projects with a mock resource handler."""
    # Arrange
    handler = MockRequestHandlerSuccessful()
    alias = "dummy-alias"
    username = "dummy-username"
    password = "dummy-password"
    client = api_client.ApiClient(handler, alias, username, password)
    projects_handler = projects.Projects(client)
    # Act
    the_projects = projects_handler.list()
    # Assert
    # There are three projects in the mock data.
    number_of_projects = 3
    assert len(the_projects) == number_of_projects
    # The first project is the Website project.
    assert the_projects[0].id == "website"
    assert the_projects[0].name == "Website"
    assert "This is the description" in the_projects[0].description


def list_projects_for_real() -> None:
    """Genuine test of the list projects resource handler for debugging."""
    # Arrange
    alias = env_config.alias
    username = env_config.username
    password = env_config.password
    handler = request_handler.RequestHandler()
    client = api_client.ApiClient(handler, alias, username, password)
    projects_handler = projects.Projects(client)
    # Act
    the_projects = projects_handler.list()
    # Assert
    assert the_projects is not None
