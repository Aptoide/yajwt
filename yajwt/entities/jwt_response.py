from http import HTTPStatus
from typing import Optional

from dataclasses import dataclass


@dataclass(frozen=True)
class JwtResponse:
    status: HTTPStatus
    json: Optional[dict] = None
    content: Optional[bytes] = None
    exception: Optional[Exception] = None
