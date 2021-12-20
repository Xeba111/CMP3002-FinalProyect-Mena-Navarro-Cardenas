import unittest
from Ejercicio_11 import Ejercicio11


class MyTestCase(unittest.TestCase):
    def test1(self):
        result = Ejercicio11.StrobogrammaticNum(4)
        print(result)
        self.assertTrue(result)
    def test2(self):
        result = Ejercicio11.StrobogrammaticNum(1)
        print(result)
        self.assertTrue(result)
    def test3(self):
        result = Ejercicio11.StrobogrammaticNum(2)
        print(result)
        self.assertTrue(result)
    def test4(self):
        result = Ejercicio11.StrobogrammaticNum(0)
        print(result)
        self.assertTrue(result)
    def test5(self):
        result = Ejercicio11.StrobogrammaticNum(5)
        print(result)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
