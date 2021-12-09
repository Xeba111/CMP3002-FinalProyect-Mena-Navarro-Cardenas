import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio4_1(self):
        self.assertEqual(main.respuesta_ejercicio4([3,2,4,3],4,2), [6,6])

    def test_ejercicio4_2(self):
        self.assertEqual(main.respuesta_ejercicio4([1,5,6],3,4), [1, 2, 3, 3])

    # def test_ejercicio3_3(self):
    #     self.assertEqual(main.respuesta_ejercicio2([7,7,7,7,7]), 16)
    #
if __name__ == '__main__':
    unittest.main()
