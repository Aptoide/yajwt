from typing import Optional

from dataclasses import dataclass


@dataclass(frozen=True)
class JwtToken:
    valid: bool
    payload: Optional[dict] = None
