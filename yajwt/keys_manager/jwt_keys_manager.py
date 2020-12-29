from abc import ABC, abstractmethod

from yajwt.entities.jwt_key import JwtKey


class JwtKeysManager(ABC):
    @abstractmethod
    def get_private_key(self, team: str) -> JwtKey:
        pass

    @abstractmethod
    def get_public_key(self, team: str) -> JwtKey:
        pass
