from enum import Enum


class JwtResponseStatus(Enum):
    OK = 200
    PROCESSING = 201
    ERROR = 400
    NOT_FOUND = 404
    EXCEPTION = 500
