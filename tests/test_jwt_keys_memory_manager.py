import unittest

from examples.keys.testing_jwt_team import TESTING_KEYS
from yajwt.entities.jwt_key import JwtKeyType
from yajwt.jwt_exceptions import JwtKeyNotFound
from yajwt.keys_manager.jwt_keys_manager import JwtKeysManager
from yajwt.keys_manager.jwt_keys_memory_manager import JwtKeysMemoryManager


class TestJwtKeysMemoryManager(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jwt_keys_manager: JwtKeysManager = None

    def setUp(self) -> None:
        self.jwt_keys_manager = JwtKeysMemoryManager(TESTING_KEYS)

    def test_get_available_private_key(self):
        team_example_private = "testing-private-user"
        jwt_key = self.jwt_keys_manager.get_private_key(team_example_private)
        self.assertEqual(team_example_private, jwt_key.team)
        self.assertEqual(JwtKeyType.PRIVATE_KEY, jwt_key.key_type)

    def test_get_not_found_private_key(self):
        not_found_team = "not-found-team"
        with self.assertRaises(JwtKeyNotFound) as e:
            _ = self.jwt_keys_manager.get_private_key(not_found_team)
        self.assertEqual(
            str(e.exception), f"JwtKey not found for team '{not_found_team}'"
        )

    def test_get_available_public_key(self):
        team_example_public = "testing-public-user"
        jwt_key = self.jwt_keys_manager.get_public_key(team_example_public)
        self.assertEqual(team_example_public, jwt_key.team)
        self.assertEqual(JwtKeyType.PUBLIC_KEY, jwt_key.key_type)

    def test_get_not_found_public_key(self):
        not_found_team = "not-found-team"
        with self.assertRaises(JwtKeyNotFound) as e:
            _ = self.jwt_keys_manager.get_public_key(not_found_team)
        self.assertEqual(
            str(e.exception), f"JwtKey not found for team '{not_found_team}'"
        )
