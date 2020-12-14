import logging
from http import HTTPStatus
from time import time

import requests
from jwt import encode

from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.entities.jwt_key import JwtKey
from yajwt.jwt_keys_manager import JwtKeysManager
from yajwt.jwt_response_mapper import (
    JwtResponseMapper,
    JwtResponse,
)


class JwtRequestsWrapper:
    def __init__(
        self,
        jwt_keys_manager: JwtKeysManager,
        jwt_response_mapper: JwtResponseMapper,
        expiration_time: int,
    ):
        self.__jwt_keys_manager = jwt_keys_manager
        self.__expiration_time = expiration_time
        self.__jwt_response_mapper = jwt_response_mapper
        self.__logger = logging.getLogger("JwtRequestsWrapper")

    # pylint: disable=too-many-arguments
    def get(
        self,
        url: str,
        user: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        timeout: int = None,
    ) -> JwtResponse:
        try:
            jwt_header = self.__build_jwt_header(user)
            headers = {**headers, **jwt_header} if headers else jwt_header

            response = requests.get(
                url, headers=headers, params=params, data=data, timeout=timeout
            )

            return self.__jwt_response_mapper.map(response)
        except (requests.exceptions.RequestException, JwtKeyNotFound) as e:
            return JwtResponse(HTTPStatus.INTERNAL_SERVER_ERROR, exception=e)

    # pylint: disable=too-many-arguments
    def post(
        self,
        url: str,
        user: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None,
        files: dict = None,
        timeout: int = None,
    ) -> JwtResponse:
        try:
            jwt_header = self.__build_jwt_header(user)
            headers = {**headers, **jwt_header} if headers else jwt_header

            response = requests.post(
                url,
                headers=headers,
                params=params,
                data=data,
                files=files,
                timeout=timeout,
            )

            return self.__jwt_response_mapper.map(response)
        except (requests.exceptions.RequestException, JwtKeyNotFound) as e:
            return JwtResponse(HTTPStatus.INTERNAL_SERVER_ERROR, exception=e)

    def __build_jwt_header(self, team: str) -> dict:
        jwt_key = self.__jwt_keys_manager.get_private_key(team)
        token = self.__encode(jwt_key).decode("utf-8")
        self.__logger.info("Using JWT token: '%s'", token)
        return {"Authorization": "Bearer " + token}

    def __encode(self, jwt_key: JwtKey) -> bytes:
        payload = jwt_key.payload
        payload["exp"] = int(time() + self.__expiration_time)
        return encode(payload, jwt_key.key, algorithm=jwt_key.algorithm)
