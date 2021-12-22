import unittest
from services.admin_service import *
from services.add_item_service import *



class AdminTest(unittest.TestCase):
    def test01checkSecretCode1(self):
        code = "X/hRrvQGaJ3HYVebsklp1TxRAjl6qQ2NR99wa/chOqE="
        self.assertEqual(checkSecretCode(code), True)

    def test02checkSecretCode2(self):
        code = "asdf"
        self.assertEqual(checkSecretCode(code), False)

    def test03getUserCount(self):
        self.assertEqual(getUserCount(), 4)

    def test04getUserList(self):
        info = {
            "offset": 0,
            "size": 4
        }
        result, flag = getUserList(info)
        self.assertEqual(flag, True)
        print(result)

    def test05getItemList1(self):
        raw_info = {
            "secret_code": "",
            "class": 1,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, True)
        print(item_list)

    def test06etItemList2(self):
        raw_info = {
            "secret_code": "",
            "class": 2,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, True)
        print(item_list)

    def test07getItemList3(self):
        raw_info = {
            "secret_code": "",
            "class": 3,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, True)
        print(item_list)

    def test08getItemList4(self):
        raw_info = {
            "secret_code": "",
            "class": 0,
            "offset": 0,
            "size": 2
        }
        item_list, flag = adminGetItemList(raw_info)
        self.assertEqual(flag, False)
        print(item_list)

    def test09OperateItem1(self):
        raw_info = {
            "secret_code": "X/hRrvQGaJ3HYVebsklp1TxRAjl6qQ2NR99wa/chOqE=",
            "class": 5,
            "id": 20,
            "operation": 0
        }
        self.assertEqual(operateItem(raw_info), "error")

    def test10OperateItem2(self):
        raw_info = {
            "secret_code": "",
            "class": 1,
            "id": 16,
            "operation": 3
        }
        self.assertEqual(operateItem(raw_info), -1)

    def test11OperateItem3(self):
        info = {
            "type": 1,
            "name": "测试测试",
            "department": 1,
            "credit": 2,
            "teacher": "测试"
        }
        db.addItem("course_list", info)
        id = db.getData("course_list", ["name"], ["测试测试"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "secret_code": "",
            "class": 1,
            "id": id,
            "operation": 0
        }
        self.assertEqual(operateItem(raw_info), 0)

    def test12OperateItem4(self):
        info = {
            "type": 1,
            "name": "测试12",
            "department": 1,
            "credit": 2,
            "teacher": "测试"
        }
        db.addItem("course_list", info)
        id = db.getData("course_list", ["name"], ["测试12"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "secret_code": "",
            "class": 1,
            "id": id,
            "operation": 1
        }
        self.assertEqual(operateItem(raw_info), 1)
        raw_info['operation'] = 0
        operateItem(raw_info)

    def test13AdminEditUser1(self):
        user_info = {
            "user_name": "test",
            "password": "test",
            "email": "testEmail19"
        }
        db.addUser(user_info)
        id = db.getData("user", ["user_name"], ["test"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "user": {
                "id": id,
                "user_name": "admin",
                "email": "testAdmin",
                "activated": 1,
                "image": ""
            },
            "delete": True
        }
        self.assertEqual(editUser(raw_info), True)

    def test14AdminEditUser2(self):
        user_info = {
            "user_name": "test",
            "password": "test",
            "email": "testEmail19"
        }
        db.addUser(user_info)
        id = db.getData("user", ["user_name"], ["test"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "user": {
                "id": id,
                "user_name": "admin",
                "email": "testAdmin",
                "activated": 1,
                "image": ""
            },
            "delete": False
        }
        self.assertEqual(editUser(raw_info), True)
        raw_info['delete'] = True
        editUser(raw_info)

    def test15AdminEditUser3(self):
        user_info = {
            "user_name": "test",
            "password": "test",
            "email": "testEmail19"
        }
        db.addUser(user_info)
        id = db.getData("user", ["user_name"], ["test"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "user": {
                "id": id,
                "activated": "asdf",
            },
            "delete": False
        }
        self.assertEqual(editUser(raw_info), False)
        raw_info['delete'] = True
        editUser(raw_info)

    def test16GetSingleUser1(self):
        user = getSingleUser(110)
        if user:
            flag = True
        else:
            flag = False
        self.assertEqual(flag, False)

    def test17GetSingleUser2(self):
        user = getSingleUser(4)
        if user:
            flag = True
        else:
            flag = False
        self.assertEqual(flag, True)

    def test18GetSingleItem1(self):
        info = {
            "class": 1,
            "id": 110
        }
        item, flag = getSingleItem(info)
        self.assertEqual(flag, True)
        print(item)

    def test19GetSingleItem2(self):
        info = {
            "class": 2,
            "id": 1
        }
        item, flag = getSingleItem(info)
        self.assertEqual(flag, True)
        print(item)

    def test20GetSingleItem3(self):
        info = {
            "class": 3,
            "id": 1
        }
        item, flag = getSingleItem(info)
        self.assertEqual(flag, True)
        print(item)

    def test19GetSingleItem2(self):
        info = {
            "class": 5,
            "id": 1
        }
        item, flag = getSingleItem(info)
        self.assertEqual(flag, False)
        print(item)

    def test20AdminEditItem1(self):
        raw_info = {
            "class": 1010,
            "item": {
                "id": 2003,
                "name": "清声细语测试"
            },
            "delete": False
        }
        self.assertEqual(editItem(raw_info), "error")

    def test21AdminEditItem2(self):
        info = {
            "type": 1,
            "name": "测试21",
            "department": 1,
            "credit": 2,
            "teacher": "测试"
        }
        db.addItem("course_list", info)
        id = db.getData("course_list", ["name"], ["测试21"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "class": 1,
            "item": {
                "id": id,
                "name": "测试21"
            },
            "delete": True
        }
        self.assertEqual(editItem(raw_info), True)

    def test21AdminEditItem2(self):
        info = {
            "type": 1,
            "name": "测试22",
            "department": 1,
            "credit": 2,
            "teacher": "测试"
        }
        db.addItem("course_list", info)
        id = db.getData("course_list", ["name"], ["测试22"], ["id"], get_all=False)[0]['id']
        raw_info = {
            "class": 1,
            "item": {
                "id": id,
                "name": "balabala"
            },
            "delete": False
        }
        self.assertEqual(editItem(raw_info), True)
        raw_info['delete'] = True
        editItem(raw_info)

if __name__ == '__main__':
    unittest.main()
