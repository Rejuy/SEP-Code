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

    def testAddComment1(self):
        comment_info = {
            "class": 1,
            "table": "course_list",  # (class对应的表名)
            "item_id": 1,
            "user": "renjy",
            "upper_comment_id": 0,
            "star": 2,
            "text": "我不怎么喜欢这门课。"
        }
        self.assertEqual(db.addComment(comment_info), True)

    def testGetItem(self):
        result, flag = db.getItem("course_list", 1, 1, ITEM_COURSE_KEY)
        self.assertEqual(flag, True)
        print(result)

    def testAddLike(self):
        self.assertEqual(db.addLike("course", "renjy", 27), True)


if __name__ == '__main__':
    unittest.main()
