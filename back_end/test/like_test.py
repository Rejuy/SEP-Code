import unittest
from services.like_service import modifyUserLike



class LikeTest(unittest.TestCase):
    def test1(self):
        info = {
            "user": "renjy",
            "comment_id": 29,
            "operation": 0
        }
        self.assertEqual(modifyUserLike(info), True)


if __name__ == '__main__':
    unittest.main()
