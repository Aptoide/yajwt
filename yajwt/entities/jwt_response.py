from typing import Optional

from dataclasses import dataclass

from yajwt.entities.jwt_response_status import JwtResponseStatus


@dataclass(frozen=True)
class JwtResponse:
    status: JwtResponseStatus
    json: Optional[dict] = None
    content: Optional[bytes] = None
    exception: Optional[Exception] = None
