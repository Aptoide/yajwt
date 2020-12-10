import logging
import sys
import unittest

if __name__ == "__main__":
    logging.disable(logging.ERROR)
    loader = unittest.TestLoader()
    tests = loader.discover(".")
    testRunner = unittest.runner.TextTestRunner(verbosity=2)
    result = testRunner.run(tests)
    sys.exit(not result.wasSuccessful())
