import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(main.repeat_num([1,2,2,3]),2)

    def test_something_2(self):
        self.assertEqual(main.repeat_num([5,3, 2, 3]),3)

    def test_something_3(self):
        self.assertEqual(main.repeat_num([1, 2, 3, 4, 5, 6, 6]),6)

    def test_something_4(self):
        self.assertEqual(main.repeat_num([1, 2, 3, 4, 5, 6, 1]),1)

    def test_something_5(self):
        self.assertEqual(main.repeat_num([1, 2, 4, 3,3]),3)


if __name__ == '__main__':
    unittest.main()
