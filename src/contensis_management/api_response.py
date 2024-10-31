"""A standard response object for API requests.

To simplify matters and so we are not bound to the response from the requests library.
"""

from dataclasses import dataclass, field


@dataclass
class ApiResponse:
    """A standard response object for API requests."""

    status_code: int
    json_data: dict
    headers: dict = field(default_factory=dict)
