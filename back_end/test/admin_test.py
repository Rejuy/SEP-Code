import unittest
from services import admin_service



class AdminTest(unittest.TestCase):
    def testGetUserCount(self):
        self.assertEqual(admin_service.getUserCount(), 4)


if __name__ == '__main__':
    unittest.main()
