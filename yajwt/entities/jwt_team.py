from dataclasses import dataclass
from typing import Optional

from yajwt.entities.jwt_key import JwtKey


@dataclass(frozen=True)
class JwtTeam:
    public_key: Optional[JwtKey] = None
    private_key: Optional[JwtKey] = None
