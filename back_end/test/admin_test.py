import unittest
from services.admin_service import *



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
        item_list, flag = getInactivatedItemList(raw_info)
        self.assertEqual(flag, True)
        print(item_list)

    def testGetInactivatedImteList2(self):
        raw_info = {
            "secret_code": "",
            "class": 5,
            "order": 2,
            "offset": 0,
            "size": 2
        }
        item_list, flag = getInactivatedItemList(raw_info)
        self.assertEqual(flag, False)


if __name__ == '__main__':
    unittest.main()
