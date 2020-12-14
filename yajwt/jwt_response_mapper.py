import logging
import re
from http import HTTPStatus

import requests

from yajwt.entities.jwt_response import JwtResponse


class JwtResponseMapper:
    def __init__(self):
        self.__logger = logging.getLogger("JwtResponseMapper")

    def map(self, response: requests.Response) -> JwtResponse:
        if re.search(r"20\d", str(response.status_code)):
            return self.__get_successful_response(response)

        self.__logger.error("Request failed with '%s'", response.status_code)
        return JwtResponse(self.__get_status(response), content=response.content)

    def __get_successful_response(self, response: requests.Response) -> JwtResponse:
        status = self.__get_status(response)
        if response.content is None:
            return JwtResponse(status)
        if "application/json" in response.headers.get("Content-Type"):
            return JwtResponse(status, json=response.json())
        return JwtResponse(status, content=response.content)

    def __get_status(self, response: requests.Response) -> HTTPStatus:
        return HTTPStatus(response.status_code)
