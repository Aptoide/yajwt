import os

from yajwt.jwt_keys_manager import JwtKeysManager
from yajwt.jwt_requests_validator import JwtRequestsValidator

if __name__ == "__main__":
    # set up your public/private keys directory
    keys_path = os.path.join(os.getcwd(), "examples", "keys")
    jwt_keys_manager = JwtKeysManager(keys_path)
    jwt_validator = JwtRequestsValidator(jwt_keys_manager)

    # validate needs "iss" on payload
    token = (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ0ZXN0aW5nLXVzZXIiLCJ2"
        "ZXJzaW9uIjoiMSIsImV4cCI6MTYwNzU5NDU5OX0.s_fuw0ut1bOOLwKgbPWDtubqO7X6c"
        "te52jtSalHrzoiMYWeWflHXbCFel9VVeLFt6oDN_Yf2xgMx3bx71W3yUQ21jjqwSCYVR5"
        "B6dw-mM15U7v-KJKbjVpBU_KOkkNyqINJAJaB6imB6zz2UG4Du68NKzlPHbCHt4VGVNIQ"
        "-4cz5kbLMkXoZmX0sO3kTqSXpW4KkB9_8IxPNGYwdaqgsVn22Hlkf9-ER8QDsn-e69Bwx"
        "fGnqf-i5J0s3uWmSvboCciE6TIYkiutH8S93rooHLJb96mglmqLu2rcH3fqr9u1hg28jG"
        "er5LRZCK1N2HsnqSGnjc1MOhnKgX5OlrHIbAg"
    )
    jwt_token = jwt_validator.validate(token)
    if jwt_token.valid:
        print(jwt_token.payload)
    print(jwt_token)
