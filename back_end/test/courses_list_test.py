import unittest
from services.course_service import getCoursesList
from headers import *


class RegisterUserInfoTest(unittest.TestCase):
    def test1(self):
        raw_info = {
            "course_type": 0,  # 课程类型
            "course_department": 0,  # 开课院系
            "course_order": 0,  # 排序方式
            "begin": 0,
            "end": 3
        }
        self.assertEqual(getCoursesList(raw_info)[2], True)

    def test2(self):
        raw_info = {
            "filter": COURSE_DEPARTMENT,
            "filter_value": DEPARTMENT_INFORMATION,
            "sort_order": DESCENDING,
            "sort_criteria": COMMENT_COUNT_ORDER,
            "index_begin": 0,
            "content_count": 2
        }
        self.assertEqual(getCoursesList(raw_info)[1], True)


if __name__ == '__main__':
    unittest.main()
