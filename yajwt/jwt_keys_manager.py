import json
import os
from typing import List

from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.entities.jwt_key import JwtKey, JwtKeyType


class JwtKeysManager:
    def __init__(self, keys_path: os.path):
        self.__keys_path = keys_path
        self.__jwt_keys: List[JwtKey] = []

    def get_private_key(self, team: str) -> JwtKey:
        if not self.__jwt_keys:
            self.__jwt_keys = self.__load_keys()
        return self.__get_key(team, JwtKeyType.PRIVATE_KEY)

    def get_public_key(self, team: str) -> JwtKey:
        if not self.__jwt_keys:
            self.__jwt_keys = self.__load_keys()
        return self.__get_key(team, JwtKeyType.PUBLIC_KEY)

    def __load_keys(self) -> List[JwtKey]:
        jwt_keys = []
        if not os.path.isdir(self.__keys_path):
            raise JwtKeyNotFound("No keys found to be loaded.")

        for filename in os.listdir(self.__keys_path):
            if not filename.endswith(".json"):
                continue

            jwt_json_path = os.path.join(self.__keys_path, filename)
            jwt_json_content = self.__get_key_json_content(jwt_json_path)
            jwt_keys.append(JwtKey.from_dict(jwt_json_content))
        return jwt_keys

    def __get_key_json_content(self, key_path: os.path) -> json:
        with open(key_path, "r", encoding="UTF-8") as file:
            return json.load(file)

    def __get_key(self, team: str, key_type: JwtKeyType) -> JwtKey:
        found_jwt_key = None
        for jwt_key in self.__jwt_keys:
            if jwt_key.team == team and jwt_key.key_type == key_type:
                found_jwt_key = jwt_key
        if not found_jwt_key:
            raise JwtKeyNotFound("JwtKey not found for team '{}'".format(team))
        return found_jwt_key
