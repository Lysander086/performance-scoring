import unittest
from app.config.configuration import Config

class TestConfig(unittest.TestCase):
    def test_resource_dir(self):
        config = Config()
        print(config.resource_dir)

if __name__ == '__main__':
    unittest.main()