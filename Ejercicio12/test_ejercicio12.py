import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        self.assertEqual(main.verticalOrder(main.root1),[[9], [3, 15], [20], [7]])

    def test_something_2(self):
        self.assertEqual(main.verticalOrder(main.root2),[[3], [5, 2, 4], [1, 8, 9], [7], [9]])

    def test_something_3(self):
        self.assertEqual(main.verticalOrder(main.root3),[[3], [2, 1], [9, 4], [5], [6]])

if __name__ == '__main__':
    unittest.main()
