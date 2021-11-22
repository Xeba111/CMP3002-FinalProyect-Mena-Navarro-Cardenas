import unittest
import Ejercicio2


class MyTestCase(unittest.TestCase):

    def test_insert(self):
        rset = Ejercicio2.RandomizedSet()
        rset.insert(1)
        rset.insert(2)
        self.assertFalse(rset.insert(1), rset.Remove(10))

    def test_remove(self):
        rset = Ejercicio2.RandomizedSet()
        self.assertFalse(rset.Remove(1))


if __name__ == '__main__':
    for i in range(1, 5):
        unittest.main()
