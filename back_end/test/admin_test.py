import unittest
from services.admin_service import *
from services.add_item_service import *



class AdminTest(unittest.TestCase):
    def testGetUserCount(self):
        self.assertEqual(getUserCount(), 4)

    def testGetInactivatedImteList1(self):
        raw_info = {
            "secret_code": "",
            "class": 3,
            "order": 2,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, True)
        print(item_list)

    def testGetInactivatedItemList2(self):
        raw_info = {
            "secret_code": "",
            "class": 5,
            "order": 2,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, False)
        print(item_list)

    def testOperateItem1(self):
        raw_info = {
            "secret_code": "X/hRrvQGaJ3HYVebsklp1TxRAjl6qQ2NR99wa/chOqE=",
            "class": 3,
            "id": 20,
            "operation": 0
        }
        self.assertEqual(operateItem(raw_info), 0)

    def testOperateItem2(self):
        raw_info = {
            "secret_code": "X/hRrvQGaJ3HYVebsklp1TxRAjl6qQ2NR99wa/chOqE=",
            "class": 3,
            "id": 16,
            "operation": 1
        }
        self.assertEqual(operateItem(raw_info), 1)

    def testAdminEditUser1(self):
        raw_info = {
            "user": {
                "id": 10,
                "user_name": "admin",
                "email": "testAdmin",
                "activated": 1,
                "image": ""
            },
            "delete": True
        }
        self.assertEqual(editUser(raw_info), True)

    def testAdminEditUser2(self):
        raw_info = {
            "user": {
                "id": 11,
                "user_name": "admin",
                "email": "testAdmin",
                "activated": 1,
                "image": ""
            },
            "delete": False
        }
        self.assertEqual(editUser(raw_info), True)

    def testGetSingleUser(self):
        user = getSingleUser(4)
        if user:
            flag = True
        else:
            flag = False
        self.assertEqual(flag, True)
        print(user)

    def testGetSingleItem1(self):
        info = {
            "class": 1,
            "id": 110
        }
        item, flag = getSingleItem(info)
        self.assertEqual(flag, True)
        print(item)

    def testAdminEditItem1(self):
        raw_info = {
            "user": {
                "id": 2003,
                "name": ""
            },
            "delete": False
        }
<<<<<<< Updated upstream
        self.assertEqual(editUser(raw_info), True)
=======
        self.assertEqual(editItem(raw_info), True)
>>>>>>> Stashed changes


if __name__ == '__main__':
    unittest.main()
