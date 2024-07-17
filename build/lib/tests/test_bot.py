import unittest
from instabot import InstagramBot

class TestInstagramBot(unittest.TestCase):
    def test_login(self):
        bot = InstagramBot()
        result = bot.login('test_username', 'test_password')
        self.assertIn('session_id', result)

if __name__ == '__main__':
    unittest.main()
