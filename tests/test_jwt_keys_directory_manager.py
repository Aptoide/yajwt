import os
import unittest

from yajwt.entities.jwt_key import JwtKeyType
from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.keys_manager.jwt_keys_directory_manager import JwtKeysDirectoryManager
from yajwt.keys_manager.jwt_keys_manager import JwtKeysManager


class TestJwtKeysDirectoryManager(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jwt_keys_manager: JwtKeysManager = None
        self.team_example = "testing-user"

    def setUp(self) -> None:
        keys_path = os.path.join(os.getcwd(), "examples", "keys")
        self.jwt_keys_manager = JwtKeysDirectoryManager(keys_path)

    def test_get_available_private_key(self):
        jwt_key = self.jwt_keys_manager.get_private_key(self.team_example)
        self.assertEqual(self.team_example, jwt_key.team)
        self.assertEqual(JwtKeyType.PRIVATE_KEY, jwt_key.key_type)

    def test_get_not_found_private_key(self):
        not_found_team = "not-found-team"
        with self.assertRaises(JwtKeyNotFound) as e:
            _ = self.jwt_keys_manager.get_private_key(not_found_team)
        self.assertEqual(
            str(e.exception), "JwtKey not found for team '{}'".format(not_found_team)
        )

    def test_get_available_public_key(self):
        jwt_key = self.jwt_keys_manager.get_public_key(self.team_example)
        self.assertEqual(self.team_example, jwt_key.team)
        self.assertEqual(JwtKeyType.PUBLIC_KEY, jwt_key.key_type)

    def test_get_not_found_public_key(self):
        not_found_team = "not-found-team"
        with self.assertRaises(JwtKeyNotFound) as e:
            _ = self.jwt_keys_manager.get_public_key(not_found_team)
        self.assertEqual(
            str(e.exception), "JwtKey not found for team '{}'".format(not_found_team)
        )
