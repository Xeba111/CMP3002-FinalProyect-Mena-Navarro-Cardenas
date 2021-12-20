import unittest

import main


class MyTestCase(unittest.TestCase):

    def test_something_1(self):
        self.assertEqual(main.subarrays_odd([5, 4, 4, 5, 1]),8)

    def test_something_2(self):
        self.assertEqual(main.subarrays_odd([5, 3, 1]),4)

    def test_something_3(self):
        self.assertEqual(main.subarrays_odd([1,2, 3]),4)

    def test_something_4(self):
        self.assertEqual(main.subarrays_odd([5,5,1,2]),6)

    def test_something_5(self):
        self.assertEqual(main.subarrays_odd([2,2,1,3,33]),8)


if __name__ == '__main__':
    unittest.main()
