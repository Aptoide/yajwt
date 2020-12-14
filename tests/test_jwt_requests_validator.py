import os
import unittest

from yajwt.jwt_keys_manager import JwtKeysManager
from yajwt.jwt_requests_validator import JwtRequestsValidator


class TestJwtRequestsValidator(unittest.TestCase):
    EXPIRED_TOKEN = (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ0ZXN0aW5nLXVzZXIiLCJ2"
        "ZXJzaW9uIjoiMSIsImV4cCI6MTYwNzU5NDU5OX0.s_fuw0ut1bOOLwKgbPWDtubqO7X6c"
        "te52jtSalHrzoiMYWeWflHXbCFel9VVeLFt6oDN_Yf2xgMx3bx71W3yUQ21jjqwSCYVR5"
        "B6dw-mM15U7v-KJKbjVpBU_KOkkNyqINJAJaB6imB6zz2UG4Du68NKzlPHbCHt4VGVNIQ"
        "-4cz5kbLMkXoZmX0sO3kTqSXpW4KkB9_8IxPNGYwdaqgsVn22Hlkf9-ER8QDsn-e69Bwx"
        "fGnqf-i5J0s3uWmSvboCciE6TIYkiutH8S93rooHLJb96mglmqLu2rcH3fqr9u1hg28jG"
        "er5LRZCK1N2HsnqSGnjc1MOhnKgX5OlrHIbAg"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jwt_validator: JwtRequestsValidator = None

    def setUp(self) -> None:
        keys_path = os.path.join(os.getcwd(), "examples", "keys")
        jwt_keys_manager = JwtKeysManager(keys_path)
        self.jwt_validator = JwtRequestsValidator(jwt_keys_manager)

    def test_validate_expired_token(self):
        jwt_token = self.jwt_validator.validate(self.EXPIRED_TOKEN)
        self.assertEqual(jwt_token.valid, False)
