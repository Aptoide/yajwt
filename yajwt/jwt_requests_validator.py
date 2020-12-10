import logging

import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError

from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.jwt_keys_manager import JwtKeysManager
from yajwt.entities.jwt_key import JwtKey
from yajwt.entities.jwt_token import JwtToken


class JwtRequestsValidator:
    def __init__(self, jwt_keys_manager: JwtKeysManager):
        self.__jwt_keys_manager = jwt_keys_manager
        self.__logger = logging.getLogger("JwtRequestsValidator")

    def validate(self, jwt_token: str) -> JwtToken:
        payload = self.__get_payload(jwt_token)
        team_name = payload.get("iss")
        if team_name is None:
            self.__logger.error("Unable to get team_name from JWT token.")
            return JwtToken(False)

        try:
            jwt_key = self.__jwt_keys_manager.get_public_key(team_name)
            return self.__validate(jwt_token, jwt_key)
        except JwtKeyNotFound as e:
            self.__logger.error(str(e))
            return JwtToken(False)

    def __get_payload(self, jwt_token: str) -> dict:
        return jwt.decode(jwt_token, verify=False)

    def __validate(self, jwt_token: str, jwt_key: JwtKey) -> JwtToken:
        try:
            jwt.decode(jwt_token, jwt_key.key, algorithms=jwt_key.algorithm)
            return JwtToken(True, self.__get_payload(jwt_token))
        except (ExpiredSignatureError, InvalidSignatureError) as e:
            self.__logger.error(f"Unable to verify {jwt_key.team} token: {str(e)}")
            return JwtToken(False)
