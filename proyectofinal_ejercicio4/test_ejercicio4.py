import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio4_1(self):
        self.assertEqual(main.respuesta_ejercicio4([3,2,4,3],4,2), [6,6])

    def test_ejercicio4_2(self):
        self.assertEqual(main.respuesta_ejercicio4([1,5,6],3,4), [1, 2, 3, 3])

    def test_ejercicio4_3(self):
        self.assertEqual(main.respuesta_ejercicio4([3,4,5,6,1],4,3), [1,6,6])

    def test_ejercicio4_4(self):
        self.assertEqual(main.respuesta_ejercicio4([1,1,1,1,1,1,1,1],1,4), [1, 1, 1, 1])

    def test_ejercicio4_5(self):
        self.assertEqual(main.respuesta_ejercicio4([6,6,6,6,6],4,8), [6, 2, 2, 2, 2, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()
