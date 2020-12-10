from dataclasses import dataclass
from enum import Enum

from dataclasses_json import dataclass_json


class JwtKeyType(Enum):
    PUBLIC_KEY = "public"
    PRIVATE_KEY = "private"


@dataclass_json
@dataclass
class JwtKey:
    team: str
    key: str
    payload: dict
    algorithm: str
    key_type: JwtKeyType
