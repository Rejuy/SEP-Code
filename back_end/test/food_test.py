import unittest
from services.food_service import getFoodsList, getFoodItem
from headers import *


class FoodTest(unittest.TestCase):
    def test1(self):
        raw_info = {
            "food_type": 1,  # 课程类型
            "food_scope": 1,  # 开课院系
            "food_order": 0,  # 排序方式
            "begin": 0,
            "end": 3
        }
        self.assertEqual(getFoodsList(raw_info)[2], True)

    def test2(self):
        print(getFoodItem(1))


if __name__ == '__main__':
    unittest.main()
