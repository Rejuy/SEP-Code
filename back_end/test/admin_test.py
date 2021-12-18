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



if __name__ == '__main__':
    unittest.main()
