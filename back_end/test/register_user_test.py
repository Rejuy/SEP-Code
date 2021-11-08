import unittest
from services import register_user_service
from headers import *


class RegisterUserInfoTest(unittest.TestCase):
    standard_user_info = {
        'user_name': 'normal',
        'password': 'Ad000000$',
        'email': 'asd19'
    }

    def test_right(self):
        content = self.standard_user_info.copy()
        self.assertEqual(register_user_service.checkUserInfo(content), VALID_INFO)

    def test_user_name1(self):
        content = self.standard_user_info.copy()
        content['user_name'] = 'a'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_USERNAME)

    def test_user_name2(self):
        content = self.standard_user_info.copy()
        content['user_name'] = 'aAAAAAAAAAAA'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_USERNAME)

    def test_password1(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asg1'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_LENGTH)

    def test_password2(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asg1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_LENGTH)

    def test_password3(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdg123333'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def test_password4(self):
        content = self.standard_user_info.copy()
        content['password'] = 'AAAAAAA123'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def test_password5(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdgAAAAAAAA'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def test_password6(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdgA123}'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_ILLEGAL_TYPE)

    def test_email(self):
        content = self.standard_user_info.copy()
        content['email'] = 'wkg16='
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_EMAIL)


if __name__ == '__main__':
    unittest.main()
