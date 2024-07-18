import unittest
from InstaToolKit import InstagramToolkit

class TestInstagramBot(unittest.TestCase):
    def test_login(self):
        bot = InstagramToolkit()
        result = bot.login('test_username', 'test_password')
        self.assertIn('session_id', result)

if __name__ == '__main__':
    unittest.main()
