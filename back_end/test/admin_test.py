import unittest
from services.login_service import checkAdminLoginInfo



class AdminTest(unittest.TestCase):
    def test1(self):
        info = {
            "user_name": "admin",
            "password": "thurec123456"
        }
        # vATn0VwIPikmhCI89O6N+JkSjjgDjeVC0bBT2r6Xa58=
        status, mask = checkAdminLoginInfo(info)
        self.assertEqual(status, 0)
        print(mask)


if __name__ == '__main__':
    unittest.main()
