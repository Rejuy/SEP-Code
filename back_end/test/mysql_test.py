import unittest
from headers import *
from services.mysql_service import db


class MySQLServiceTest(unittest.TestCase):
    def testCheckUserExistence1(self):
        email = "asdf"
        self.assertEqual(db.checkUserExistence(email), False)

    def testCheckUserExistence2(self):
        email = "testEmail19"
        self.assertEqual(db.checkUserExistence(email), True)

    def testCheckUserNameExistence1(self):
        user_name = "jiliguala"
        self.assertEqual(db.checkUserNameExistence(user_name), False)

    def testCheckUserNameExistence2(self):
        user_name = "testUser"
        self.assertEqual(db.checkUserNameExistence(user_name), True)

    def testAddUser1(self):
        user_info = {
            "user_name": "testUser",
            "password": "Testpassword1",
            "email": "testEmail19"
        }
        self.assertEqual(db.addUser(user_info), True)

    def testAddUser2(self):
        user_info = {
            "user_name": "testUser2",
            "password": "Ad000000$",
            "email": "asd19"
        }
        self.assertEqual(db.addUser(user_info), True)

    def testDelUser1(self):
        self.assertEqual(db.delUser("id", 5), True)

    def testDelUser2(self):
        self.assertEqual(db.delUser("username", "testUser"), True)

    def testDelUser3(self):
        self.assertEqual(db.delUser("email", "testEmail19"), True)

    def testUpdateData1(self):
        table = "user"
        locate_key = "email"
        locate_value = "testEmail19"
        update_key = "activated"
        update_value = 1
        self.assertEqual(db.updateData(table, locate_key, locate_value, update_key, update_value), True)


if __name__ == '__main__':
    unittest.main()
