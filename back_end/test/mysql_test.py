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

    def testAddUser3(self):
        user_info = {
            "user_name": "任俊宇",
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
        self.assertEqual(db.updateData("user", "email", "testEmail19", "activated", 1), True)

    def testUpdateData2(self):
        self.assertEqual(db.updateData("course_content", "number", "101", "rate_count", 1), True)
        self.assertEqual(db.updateData("course_content", "number", "101", "rate", 3), True)
        self.assertEqual(db.updateData("course_content", "number", "101", "comment_count", 1), True)
        self.assertEqual(db.updateData("course_content", "number", "101", "heat", 8), True)

    def testUpdateData3(self):
        self.assertEqual(db.updateData("user_like", "id", 4, "comment_id", 35), True)

    def testAddItem1(self):
        info = {
            "type": 5,
            "name": "清声细语4",
            "teacher": "平台测试组",
            "department": 1,
            "credit": 2
        }
        self.assertEqual(db.addItem("course_list", info), True)

    def testAddItem2(self):
        info = {
            "type": 1,
            "name": "第二教室楼",
            "position": "清华大学西南方向",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem3(self):
        info = {
            "type": 1,
            "name": "图书馆北馆（李文正馆）",
            "position": "清华大学西北方向",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info, user_id=4), True)

    def testAddItem4(self):
        info = {
            "type": 1,
            "name": "图书馆西馆（逸夫馆）",
            "position": "清华大学西北方向",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info, user_id=4), True)

    def testAddContent3(self):
        info = {
            "number": 102,
            "type": TYPE_PRACTICE,
            "name": "清声细语实践",
            "teacher": "曾晓龙",
            "department": DEPARTMENT_INFORMATION,
            "schedule": "1-2",
            "credit": 2,
            "rate_count": 5,
            "rate": 5,
            "comment_count": 5,
            "heat": 10
        }
        self.assertEqual(db.addContent("course_content", info), True)

    def testAddContent4(self):
        info = {
            "number": 103,
            "type": TYPE_EXPERIMENT,
            "name": "实验室清声细语探究",
            "teacher": "丁佳华",
            "department": DEPARTMENT_INFORMATION,
            "schedule": "1-4",
            "credit": 4,
            "rate_count": 3,
            "rate": 4,
            "comment_count": 3,
            "heat": 9
        }
        self.assertEqual(db.addContent("course_content", info), True)

    def testAddContent5(self):
        info = {
            "number": 104,
            "type": TYPE_CULTURE,
            "name": "清声细语中的哲学思辩",
            "teacher": "任俊宇",
            "department": DEPARTMENT_CULTURE,
            "schedule": "1-5",
            "credit": 3,
            "rate_count": 10,
            "rate": 1,
            "comment_count": 10,
            "heat": 4
        }
        self.assertEqual(db.addContent("course_content", info), True)

    def testAddItem6(self):
        info = {
            "type": 1,
            "name": "第三教室楼",
            "position": "清华大学学堂路东",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem7(self):
        info = {
            "type": 1,
            "name": "第四教室楼",
            "position": "清华大学学堂路西",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem8(self):
        info = {
            "type": 1,
            "name": "清华学堂",
            "position": "清华大学中部大礼堂东南侧",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem9(self):
        info = {
            "type": 1,
            "name": "第五教室楼",
            "position": "清华大学清华学堂东侧",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem10(self):
        info = {
            "type": 1,
            "name": "第六教学楼",
            "position": "清华大学新民路西",
            "scope": 1
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem10(self):
        info = {
            "type": 1,
            "name": "凯风人文社科图书馆",
            "position": "清华大学学堂路东",
            "scope": 1,
            "user_id": 4
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem11(self):
        info = {
            "type": 1,
            "name": "法律图书馆",
            "position": "清华大学东南方向学堂路东",
            "scope": 1,
            "user_id": 4
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem12(self):
        info = {
            "type": 1,
            "name": "啊哈，根本没有这个地儿",
            "position": "清华大学",
            "scope": 1,
            "user_id": 4
        }
        self.assertEqual(db.addItem("place_list", info), True)

    def testAddItem13(self):
        info = {
            "type": 1,
            "name": "测试",
            "department": 1,
            "credit": 2,
            "teacher": "测试"
        }
        self.assertEqual(db.addItem("course_list", info), True)

    def testGetItemList1(self):
        info = {
            "key_list": BASIC_COURSES_KEY,
            "filter": "",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "content_count": 4
        }

        result = db.getItemList("course_list", info)
        print(result[0])
        self.assertEqual(result[1], True)

    def testGetItemList2(self):
        info = {
            "key_list": BASIC_COURSES_KEY,
            "filter": "",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "content_count": 4,
            "like": "2"
        }

        result = db.getItemList("course_list", info)
        print(result[0])
        self.assertEqual(result[1], True)

    def testGetItemList3(self):
        info = {
            "key_list": BASIC_COURSES_KEY,
            "filter": "",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "content_count": 4,
            "like": "2333"
        }

        result = db.getItemList("course_list", info)
        print(result[0])
        self.assertEqual(result[1], True)

    def testGetItemList4(self):
        info = {
            "key_list": BASIC_PLACE_KEY,
            "filter": "",
            "sort_order": "desc",
            "sort_criteria": "star",
            "index_begin": 0,
            "content_count": 4,
            "like": "学堂路"
        }

        result = db.getItemList("place_list", info)
        print(result[0])
        self.assertEqual(result[1], True)

    def testAddComment1(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 3,
            "user": "renjy",
            "upper_comment_id": 0,
            "star": 3,
            "text": "我对这门课无可奉告。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def testAddComment2(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 3,
            "user": "zengxl",
            "upper_comment_id": 0,
            "star": 4,
            "text": "我对这门课无可奉告呀。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def testGetItem1(self):
        result, flag = db.getItem("food_list", 2, 1, ITEM_FOOD_KEY)
        self.assertEqual(flag, True)
        print(result)

    def testGetItem2(self):
        result, flag = db.getItem("place_list", 3, 5, ITEM_PLACE_KEY)
        self.assertEqual(flag, True)
        print(result)

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
        result, flag = db.getData("comment", ["star"], [2], ["text"])
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

    def testDelComment1(self):
        self.assertEqual(db.delComment("id", 34), True)

    def testDelComment2(self):
        self.assertEqual(db.delComment("id", 35), True)

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

    def testGetUserList(self):
        info = {
            "offset": 0,
            "size": 4
        }
        user_list, flag = db.getUserList(info)
        self.assertEqual(flag, True)
        print(user_list)

    def testCheckDataExistence1(self):
        self.assertEqual(db.checkDataExistence("user", "id", 4), True)

    def testCheckDataExistence2(self):
        self.assertEqual(db.checkDataExistence("user", "id", 14), False)

    def testSelfChangeData1(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", 1), True)

    def testSelfChangeData2(self):
        self.assertEqual(db.selfChangeData("class", ["name"], ["food"], "count", -1), True)


if __name__ == '__main__':
    unittest.main()
