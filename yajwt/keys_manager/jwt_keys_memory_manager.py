from typing import Dict
from yajwt.entities.jwt_key import JwtKey, JwtKeyType
from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.keys_manager.jwt_keys_manager import JwtKeysManager


class JwtKeysMemoryManager(JwtKeysManager):
    def __init__(self, keys: Dict[str, JwtKey]):
        self.__jwt_keys = keys

    def get_private_key(self, team: str) -> JwtKey:
        if (
            team not in self.__jwt_keys
            or self.__jwt_keys[team].key_type is not JwtKeyType.PRIVATE_KEY
        ):
            raise JwtKeyNotFound(f"JwtKey not found for team '{team}'")
        return self.__jwt_keys[team]

    def get_public_key(self, team: str) -> JwtKey:
        if (
            team not in self.__jwt_keys
            or self.__jwt_keys[team].key_type is not JwtKeyType.PUBLIC_KEY
        ):
            raise JwtKeyNotFound(f"JwtKey not found for team '{team}'")
        return self.__jwt_keys[team]
