import unittest
from Ejercicio_2 import Ejercicio2


class MyTestCase(unittest.TestCase):

    def test1(self):
        result = Ejercicio2.RandomizedSet()
        self.assertTrue(result.insert(1), result.insert(2))

    def test2(self):
        result = Ejercicio2.RandomizedSet()
        self.assertFalse(result.remove(1))

    def test3(self):
        result = Ejercicio2.RandomizedSet()
        result.insert(1)
        result.insert(2)
        self.assertTrue(result.remove(1), result.remove(2))

    def test4(self):
        result = Ejercicio2.RandomizedSet()


    #def test5(self):


unittest.main()
