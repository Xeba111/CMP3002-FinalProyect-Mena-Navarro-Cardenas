import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(main.list1.insertVal(main.m5),{1,2,3,4,5})
    def test_something_2(self):
        self.assertEqual(main.list2.insertVal(main.n5),{1,4,5,4,9})

if __name__ == '__main__':
    unittest.main()
