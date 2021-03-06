import unittest

from pixelated.register import validate_username, validate_password


class TestRegister(unittest.TestCase):

    def test_username_raises_error_when_it_contains_uppercase_letters(self):
        with self.assertRaises(ValueError):
            validate_username('INVALIDUSERNAME')

    def test_username_raises_error_when_it_contains_special_characters(self):
        with self.assertRaises(ValueError):
            validate_username('invalid@username')

    def test_password_raises_error_if_shorter_than_8_characters(self):
        with self.assertRaises(ValueError):
            validate_password('short')

    def test_username_pass_when_valid(self):
        try:
            validate_username('a.valid_username-123')
        except:
            self.fail('Valid username should not raise an exception')
