import logging

import jwt
from jwt import InvalidTokenError

from yajwt.entities.jwt_key import JwtKey
from yajwt.entities.jwt_token import JwtToken
from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.keys_manager.jwt_keys_manager import JwtKeysManager


class JwtRequestsValidator:
    def __init__(self, jwt_keys_manager: JwtKeysManager):
        self.__jwt_keys_manager = jwt_keys_manager
        self.__logger = logging.getLogger("JwtRequestsValidator")

    def validate(self, jwt_token: str) -> JwtToken:
        payload = self.__get_payload(jwt_token)
        team_name = payload.get("iss")
        if team_name is None:
            error_message = "Unable to get team_name from JWT token."
            self.__logger.error(error_message)
            return JwtToken(False, error_message=error_message)

        return self.validate_user(jwt_token, team_name)

    def __get_payload(self, jwt_token: str) -> dict:
        return jwt.decode(jwt_token, verify=False)

    def __validate(self, jwt_token: str, jwt_key: JwtKey) -> JwtToken:
        try:
            jwt.decode(jwt_token, jwt_key.key, algorithms=jwt_key.algorithm)
            return JwtToken(True, self.__get_payload(jwt_token))
        except InvalidTokenError as e:
            self.__logger.error("Unable to verify %s token %s", jwt_key.team, str(e))
            return JwtToken(False, error_message=str(e))

    def validate_user(self, jwt_token: str, team_name: str) -> JwtToken:
        try:
            jwt_key = self.__jwt_keys_manager.get_public_key(team_name)
            return self.__validate(jwt_token, jwt_key)
        except JwtKeyNotFound as e:
            self.__logger.error(str(e))
            return JwtToken(False, error_message=str(e))
