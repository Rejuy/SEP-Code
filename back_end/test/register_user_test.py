import unittest
from services import register_user_service
from headers import *


class RegisterUserInfoTest(unittest.TestCase):
    standard_user_info = {
        'user_name': 'normal',
        'password': 'Ad000000$',
        'email': 'asd19'
    }

    def testRight(self):
        content = self.standard_user_info.copy()
        self.assertEqual(register_user_service.checkUserInfo(content), VALID_INFO)

    def testUserName1(self):
        content = self.standard_user_info.copy()
        content['user_name'] = 'a'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_USERNAME)

    def testUserName2(self):
        content = self.standard_user_info.copy()
        content['user_name'] = 'aAAAAAAAAAAA'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_USERNAME)

    def testPassword1(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asg1'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_LENGTH)

    def testPassword2(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asg1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_LENGTH)

    def testPassword3(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdg123333'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def testPassword4(self):
        content = self.standard_user_info.copy()
        content['password'] = 'AAAAAAA123'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def testPassword5(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdgAAAAAAAA'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_MISSING_TYPE)

    def testPassword6(self):
        content = self.standard_user_info.copy()
        content['password'] = 'asdgA123}'
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_PASSWORD_ILLEGAL_TYPE)

    def testEmail(self):
        content = self.standard_user_info.copy()
        content['email'] = 'wkg16='
        self.assertEqual(register_user_service.checkUserInfo(content), INVALID_EMAIL)


if __name__ == '__main__':
    unittest.main()
