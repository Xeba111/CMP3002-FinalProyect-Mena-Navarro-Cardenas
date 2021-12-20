import unittest
from Ejercicio_5 import Ejercicio5


class MyTestCase(unittest.TestCase):
    def test1(self):
        result = Ejercicio5.fiboTree(4)
        self.assertTrue(result)

    def test2(self):
        result = Ejercicio5.fiboTree(21)
        self.assertTrue(result)

    def test3(self):
        result = Ejercicio5.fiboTree(40)
        self.assertTrue(result)

    def test4(self):
        result = Ejercicio5.fiboTree(200)
        self.assertTrue(result)

    def test5(self):
        result = Ejercicio5.fiboTree(1)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
