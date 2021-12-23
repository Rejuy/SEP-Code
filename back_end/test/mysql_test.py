import unittest
from headers import *
from services.mysql_service import db


class MySQLServiceTest(unittest.TestCase):
    def test01CheckUserExistence1(self):
        email = "asdf"
        self.assertEqual(db.checkUserExistence(email), False)

    def test02CheckUserExistence2(self):
        email = "renjy19"
        self.assertEqual(db.checkUserExistence(email), True)

    def test03CheckUserExistence3(self):
        email = [1, 2, 3]
        self.assertEqual(db.checkUserExistence(email), False)

    def test04CheckUserNameExistence1(self):
        user_name = "jiliguala"
        self.assertEqual(db.checkUserNameExistence(user_name), False)

    def test05CheckUserNameExistence2(self):
        user_name = "renjy"
        self.assertEqual(db.checkUserNameExistence(user_name), True)

    def test06CheckUserNameExistence3(self):
        user_name = []
        self.assertEqual(db.checkUserNameExistence(user_name), False)

    def test07CheckDataExistence1(self):
        user_name = "jiliguala"
        self.assertEqual(db.checkDataExistence("user", "user_name", user_name), False)

    def test08CheckDataExistence2(self):
        user_name = "renjy"
        self.assertEqual(db.checkDataExistence("user", "user_name", user_name), True)

    def test09CheckDataExistence3(self):
        user_name = []
        self.assertEqual(db.checkDataExistence("user", "user_name", user_name), False)

    def test10AddUser1(self):
        user_info = {
            "user_name": [],
            "password": "test",
            "email": "testEmail19"
        }
        self.assertEqual(db.addUser(user_info), False)

    def test11AddUser2(self):
        user_info = {
            "user_name": "test",
            "password": "test",
            "email": "test19"
        }
        self.assertEqual(db.addUser(user_info), True)

    def test12DelUser1(self):
        id = db.getData("user", ["user_name"], ["test"], ["id"], get_all=False)[0]["id"]
        self.assertEqual(db.delUser("id", id), True)

    def test13DelUser2(self):
        self.assertEqual(db.delUser("username", []), False)

    def test14GetUser1(self):
        user = db.getUser("id", 4)
        if user:
            flag = True
        else:
            flag = False
        self.assertEqual(flag, True)
        print(user)

    def test14GetUser2(self):
        user = db.getUser("iasdf", 4)
        if user:
            flag = True
        else:
            flag = False
        self.assertEqual(flag, False)
        print(user)

    def test15GetUserList1(self):
        info = {
            "offset": 0,
            "size": 4
        }
        user_list, flag = db.getUserList(info)
        self.assertEqual(flag, True)
        print(user_list)

    def test16GetUserList2(self):
        info = {
            "offset": 0
        }
        user_list, flag = db.getUserList(info)
        self.assertEqual(flag, False)
        print(user_list)

    def test17UpdateData1(self):
        self.assertEqual(db.updateData("course_list", "id", 2022, "activated", 1), True)

    def test18UpdateData2(self):
        self.assertEqual(db.updateData("course_list", "id", 2022, "activated", []), False)

    def test19GetData1(self):
        result, flag = db.getData("course_list", ["name"], ["单元测试样例"], ["time"], get_all=False)
        self.assertEqual(flag, True)
        print(result)

    def test20GetData2(self):
        result, flag = db.getData("course_list", ["name"], ["asdfasdf"], ["time"], get_all=False)
        self.assertEqual(flag, False)
        print(result)

    def test21GetData3(self):
        result, flag = db.getData("course_list", ["name"], ["单元测试样例"], 2, get_all=False)
        self.assertEqual(flag, False)
        print(result)

    def test22GetData4(self):
        result, flag = db.getData("course_list", ["name"], ["单元测试样例"], ["time"])
        self.assertEqual(flag, True)
        print(result)

    def test23GetData5(self):
        result, flag = db.getData("course_list", ["name"], ["asdfasdf"], ["time"])
        self.assertEqual(flag, False)
        print(result)

    def test24GetData6(self):
        result, flag = db.getData("course_list", ["name"], ["单元测试样例"], 2)
        self.assertEqual(flag, False)
        print(result)

    def test25AddItem1(self):
        info = {
            "type": 5,
            "name": "单元测试样例2345",
            "teacher": "平台测试组",
            "department": 1,
            "credit": 2
        }
        self.assertEqual(db.addItem("course_list", info), True)

    def test26AddItem1(self):
        self.assertEqual(db.addItem("course_list", 1), False)

    def test27GetItem1(self):
        info = {
            "id": 2022,
            "begin": 0,
            "count": 3
        }
        result, flag = db.getItem("course_list", 1, info, ITEM_COURSE_KEY)
        self.assertEqual(flag, True)
        print(result)

    def test28GetItem2(self):
        info = {
            "id": 2022,
        }
        result, flag = db.getItem("course_list", 1, info, ITEM_COURSE_KEY)
        self.assertEqual(flag, False)
        print(result)

    def test29GetItemList1(self):
        info = {
            "key_list": BASIC_COURSES_KEY,
            "filter": [
                {
                    "key": "name",
                    "value": "软件工程"
                },
                {
                    "key": "department",
                    "value": 26
                }
            ],
            "like": "软件",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "item_count": 4
        }
        result = db.getItemList("course_list", info)
        print(result[0])
        self.assertEqual(result[2], True)

    def test30GetItemList2(self):
        info = {
            "key_list": BASIC_COURSES_KEY,
            "filter": [],
            "like": "软件工程",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "item_count": 4
        }
        result = db.getItemList("course_list", info)
        print(result[0])
        self.assertEqual(result[2], True)

    def test31GetItemList3(self):
        result = db.getItemList("course_list", 1)
        print(result[0])
        self.assertEqual(result[2], False)

    def test32GetTableCount1(self):
        self.assertEqual(db.getTableCount("user"), 4)

    def test33GetTableCount2(self):
        self.assertEqual(db.getTableCount("as"), -1)

    def test34AddComment1(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 2022,
            "user": "renjy",
            "upper_comment_id": -1,
            "star": 3,
            "text": "测试评论1。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def test35AddComment2(self):
        self.assertEqual(db.addComment(123), False)

    def test36AddComment3(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 2022,
            "user": "zengxl",
            "upper_comment_id": -1,
            "star": 4,
            "text": "测试评论2。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def test38DelComment2(self):
        self.assertEqual(db.delComment("id", 96), True)

    def test39DelComment3(self):
        self.assertEqual(db.delComment("id", []), False)

    def test40AddLike(self):
        self.assertEqual(db.addLike("renjy", 69), True)

    def test41CheckCommentLiked(self):
        self.assertEqual(db.checkCommentLiked("renjy", 69), True)

    def test42DelLike(self):
        self.assertEqual(db.delLike("renjy", 69), True)

    def test43CheckCommentLiked(self):
        self.assertEqual(db.checkCommentLiked("renjy", 69), False)

    def test44GetUserCommentList(self):
        comment_list, flag = db.getUserCommentList("renjy")
        self.assertEqual(flag, True)
        print(comment_list)

    def test45CheckItemCommented(self):
        result, flag = db.checkItemCommented("renjy", 1, 1874)
        self.assertEqual(flag, True)
        print(result)

    def test46AddCollection(self):
        self.assertEqual(db.addCollection(3,1,4), True)

    def test47ItemCollected1(self):
        self.assertEqual(db.checkItemCollected(3,1,4), True)

    def test48DelCollection(self):
        self.assertEqual(db.delCollection(3,1,4), True)

    def test49ItemCollected2(self):
        self.assertEqual(db.checkItemCollected(3,1,4), False)

    def test50GetGlobalItemList1(self):
        info = {
            "like": "清",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "item_count": 5
        }
        item_list, count, flag = db.getGlobalItemList(info)
        self.assertEqual(flag, True)
        print(item_list)

    def test51CheckDataExistence1(self):
        self.assertEqual(db.checkDataExistence("user", "id", 4), True)

    def test52CheckDataExistence2(self):
        self.assertEqual(db.checkDataExistence("user", "id", 123), False)

    def test53SelfChangeData1(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", 1), True)

    def test54SelfChangeData2(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", -1), True)

    def test55RandomItemId1(self):
        id, flag = db.randomItemId("food_list", 4, FOOD_KEY)
        self.assertEqual(flag, True)
        print(id)

    def test56UserCount(self):
        count_list, flag = db.getNewUserCount(12)
        self.assertEqual(flag, True)
        print(count_list)

    def test57GetDatabaseInfo(self):
        data, flag = db.getDatabaseInfo()
        self.assertEqual(flag, True)
        print(data)

    def test58Comments(self):
        data_list, flag = db.getAllComments()
        print(data_list)
        self.assertEqual(flag, True)


if __name__ == '__main__':
    unittest.main()
