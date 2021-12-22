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
        self.assertEqual(db.updateData("course_list", "id", 2010, "activated", 1), True)

    def test18UpdateData2(self):
        self.assertEqual(db.updateData("course_list", "id", 2010, "activated", []), False)

    def test19GetData1(self):
        result, flag = db.getData("course_list", ["name"], ["测试"], ["time"], get_all=False)
        self.assertEqual(flag, True)
        print(result)

    def test20GetData2(self):
        result, flag = db.getData("course_list", ["name"], ["asdfasdf"], ["time"], get_all=False)
        self.assertEqual(flag, False)
        print(result)

    def test21GetData3(self):
        result, flag = db.getData("course_list", ["name"], ["测试"], 2, get_all=False)
        self.assertEqual(flag, False)
        print(result)

    def test22GetData4(self):
        result, flag = db.getData("course_list", ["name"], ["测试"], ["time"])
        self.assertEqual(flag, True)
        print(result)

    def test23GetData5(self):
        result, flag = db.getData("course_list", ["name"], ["asdfasdf"], ["time"])
        self.assertEqual(flag, False)
        print(result)

    def test24GetData6(self):
        result, flag = db.getData("course_list", ["name"], ["测试"], 2)
        self.assertEqual(flag, False)
        print(result)

    def test25AddItem1(self):
        info = {
            "type": 5,
            "name": "单元测试样例",
            "teacher": "平台测试组",
            "department": 1,
            "credit": 2
        }
        self.assertEqual(db.addItem("course_list", info), True)

    def test26AddItem1(self):
        self.assertEqual(db.addItem("course_list", 1), False)

    def test27GetItem1(self):
        info = {
            "id": 2003,
            "begin": 0,
            "count": 3
        }
        result, flag = db.getItem("course_list", 1, info, ITEM_COURSE_KEY)
        self.assertEqual(flag, True)
        print(result)

    def test28GetItem2(self):
        info = {
            "id": 2003,
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
                    "value": "单元测试样例"
                },
                {
                    "key": "department",
                    "value": 1
                }
            ],
            "like": "测试",
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
            "like": "单元测试",
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
            "item_id": 2021,
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
            "item_id": 2021,
            "user": "zengxl",
            "upper_comment_id": -1,
            "star": 4,
            "text": "测试评论2。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def test37DelComment1(self):
        item_id = db.getData("course_list", ["name"], ["单元测试样例"], ["id"], get_all=False)[0]["id"]
        id = db.getData("comment", ["item_id", "user"], [item_id, "renjy"], ["id"], get_all=False)[0]["id"]
        self.assertEqual(db.delComment("id", id), True)

    def test38DelComment2(self):
        item_id = db.getData("course_list", ["name"], ["单元测试样例"], ["id"], get_all=False)[0]["id"]
        id = db.getData("comment", ["item_id", "user"], [item_id, "zengxl"], ["id"], get_all=False)[0]["id"]
        self.assertEqual(db.delComment("id", id), True)

    def test39DelComment3(self):
        self.assertEqual(db.delComment("id", []), False)

    def testAddComment2(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 2003,
            "user": "zhangbw",
            "upper_comment_id": -1,
            "star": 1,
            "text": "测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。测试五十个字。"
        }
        self.assertEqual(db.addComment(comment_info), True)



    def testAddLike(self):
        self.assertEqual(db.addLike("renjy", 29), True)

    def testDelLike(self):
        self.assertEqual(db.delLike("renjy", 29), True)

    def testCheckCommentLiked(self):
        self.assertEqual(db.checkCommentLiked("renjy", 28), False)

    def testGetUserCommentList(self):
        comment_list, flag = db.getUserCommentList("renjy")
        self.assertEqual(flag, True)
        print(comment_list)

    def testGetUserLikeCommentList(self):
        comment_list, flag = db.getUserLikeCommentList("renjy")
        self.assertEqual(flag, True)
        print(comment_list)

    def testCheckItemCommented(self):
        result, flag = db.checkItemCommented("renjy", 1, 1)
        self.assertEqual(flag, True)
        print(result)

    def testGetData1(self):
        result, flag = db.getData("course_list", ["name"], ["测试"], ["time"], get_all=False)
        self.assertEqual(flag, True)
        print(result)

    def testGetData2(self):
        result, flag = db.getData("course_list", ["id"], [2], ["name"])
        self.assertEqual(flag, True)
        print(result)

    def testAddCollection(self):
        self.assertEqual(db.addCollection(1,2,4), True)

    def testDelCollection(self):
        self.assertEqual(db.delCollection(1,2,4), True)

    def testItemCollected1(self):
        self.assertEqual(db.checkItemCollected(1,1,4), True)

    def testItemCollected2(self):
        self.assertEqual(db.checkItemCollected(1,2,4), False)



    def testGetGlobalItemList1(self):
        info = {
            "like": "清",
            "sort_order": "desc",
            "sort_criteria": "heat",
            "index_begin": 0,
            "item_count": 5
        }
        item_list, flag = db.getGlobalItemList(info)
        self.assertEqual(flag, True)
        print(item_list)



    def testCheckDataExistence1(self):
        self.assertEqual(db.checkDataExistence("user", "id", 4), True)

    def testCheckDataExistence2(self):
        self.assertEqual(db.checkDataExistence("user", "id", 14), False)

    def testSelfChangeData1(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", 1), True)

    def testSelfChangeData2(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", -1), True)

    def testRandomItemId1(self):
        id, flag = db.randomItemId("food_list", 4)
        self.assertEqual(flag, True)
        print(id)

    def testUserCount(self):
        count_list, flag = db.getNewUserCount(12)
        self.assertEqual(flag, True)
        print(count_list)


if __name__ == '__main__':
    unittest.main()
