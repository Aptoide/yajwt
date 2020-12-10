import logging
import re

import requests

from yajwt.entities.jwt_response import JwtResponse
from yajwt.entities.jwt_response_status import JwtResponseStatus


class JwtResponseMapper:
    def __init__(self):
        self.__logger = logging.getLogger("JwtResponseMapper")

    def map(self, response: requests.Response) -> JwtResponse:
        if re.search(r"20\d", str(response.status_code)):
            return self.__get_successful_response(response)
        elif response.status_code == 404:
            return JwtResponse(JwtResponseStatus.NOT_FOUND)
        self.__logger.error(f"Request failed with status code '{response.status_code}'")
        return JwtResponse(JwtResponseStatus.ERROR, content=response.content)

    def __get_successful_response(self, response: requests.Response) -> JwtResponse:
        status = self.__get_successful_status(response)
        if response.content is None:
            return JwtResponse(status)
        elif "application/json" in response.headers.get("Content-Type"):
            return JwtResponse(status, json=response.json())
        else:
            return JwtResponse(status, content=response.content)

    def __get_successful_status(self, response: requests.Response) -> JwtResponseStatus:
        if response.status_code in [200, 202, 203, 204]:
            return JwtResponseStatus.OK
        elif response.status_code == 201:
            return JwtResponseStatus.PROCESSING
