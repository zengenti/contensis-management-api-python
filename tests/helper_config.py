"""Allow access to environment variables for testing purposes."""

import os

from dotenv import load_dotenv


class EnvConfig:
    """Access environment variables for testing purposes."""

    def __init__(self):
        # Load .env file if it exists
        load_dotenv()

    def _get(self, key, default=None):
        # Prioritize environment variables over .env
        return os.environ.get(key) or os.getenv(key) or default

    @property
    def username(self):
        """Return the username for the Contensis API."""
        return self._get("USERNAME")

    @property
    def password(self):
        """Return the password for the Contensis API."""
        return self._get("PASSWORD")


# Create a singleton instance
env_config = EnvConfig()
