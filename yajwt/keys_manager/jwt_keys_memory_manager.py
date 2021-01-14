from typing import Dict
from yajwt.entities.jwt_key import JwtKey
from yajwt.entities.jwt_team import JwtTeam
from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.keys_manager.jwt_keys_manager import JwtKeysManager


class JwtKeysMemoryManager(JwtKeysManager):
    def __init__(self, keys: Dict[str, JwtTeam]):
        self.__jwt_keys = keys

    def get_private_key(self, team: str) -> JwtKey:
        if team not in self.__jwt_keys or \
                self.__jwt_keys[team].private_key is None:
            raise JwtKeyNotFound(
                "JwtKey not found for team '{}'".format(team))
        return self.__jwt_keys[team].private_key

    def get_public_key(self, team: str) -> JwtKey:
        if team not in self.__jwt_keys or \
                self.__jwt_keys[team].public_key is None:
            raise JwtKeyNotFound(
                "JwtKey not found for team '{}'".format(team))
        return self.__jwt_keys[team].public_key
