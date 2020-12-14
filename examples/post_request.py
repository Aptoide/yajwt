import logging
import os
from http import HTTPStatus

from yajwt.jwt_keys_manager import JwtKeysManager
from yajwt.jwt_requests_wrapper import JwtRequestsWrapper
from yajwt.jwt_response_mapper import JwtResponseMapper

TOKEN_TTL = 60 * 10  # we recommend 10 min

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # set up your public/private keys directory
    keys_path = os.path.join(os.getcwd(), "examples", "keys")
    jwt_keys_manager = JwtKeysManager(keys_path)
    jwt_requests = JwtRequestsWrapper(jwt_keys_manager, JwtResponseMapper(), TOKEN_TTL)

    # make the request
    data = {"param1": 1, "param2": 2}
    response = jwt_requests.post("https://example.com", "testing-user", data=data)
    if response.status == HTTPStatus.OK:
        print(response.json)
    print(response)
