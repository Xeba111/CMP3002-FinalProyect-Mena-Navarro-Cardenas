import unittest
from Ejercicio_8 import Ejercicio8
#ej8

class MyTestCase(unittest.TestCase):
    def test1(self):
        result = Ejercicio8.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22])
        self.assertTrue(result)

    def test2(self):
        result = Ejercicio8.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5])
        self.assertTrue(result)

    def test3(self):
        result = Ejercicio8.minInterval([[2, 8], [2, 4], [5, 8], [20, 25]], [2, 8, 5, 22])
        self.assertTrue(result)

    def test4(self):
        result = Ejercicio8.minInterval([[2, 4], [3, 5], [1, 3], [10, 15]], [2, 15, 5, 2])
        self.assertEqual(result,[3, -1, -1, 3])

    def test_5(self):
        result = Ejercicio8.minInterval([[1, 2], [2, 4], [4, 6], [7, 10]], [2, 4, 7, 2])
        self.assertEqual(result,[2,-1,-1,2])




if __name__ == '__main__':
    unittest.main()
