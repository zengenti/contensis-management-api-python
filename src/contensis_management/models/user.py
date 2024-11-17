"""A user model."""

from datetime import datetime

from contensis_management.models import camel_case


class Provider(camel_case.CamelModel):
    """A Contensis user credential provider model."""

    type: str
    name: str


class Credentials(camel_case.CamelModel):
    """A Contensis user credentials model."""

    passwordChangeFrequency: int
    provider: Provider


class Status(camel_case.CamelModel):
    """A Contensis user status model."""

    suspended: bool
    locked: bool
    password_reset_required: bool


class User(camel_case.CamelModel):
    """A Contensis user model."""

    id: str
    username: str
    first_name: str
    last_name: str
    email: str
    timezone: str
    language: str
    custom: dict = {}
    credentials: Credentials
    status: Status
    created: datetime | None = None
    last_login: datetime | None = None
    last_failed_login: datetime | None = None
    modified: datetime | None = None
    expiry: datetime | None = None
    password_changed: datetime | None = None
    opt_out_of_notifications: bool
    failed_login_attempts: int
    failed_login_attempts_since_last_success: int
    successful_login_attempts: int
