import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio1_1(self):
        self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])

    def test_ejercicio1_2(self):
        self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], -1, 3, 5), [-23, -5, 1, 7])

    def test_ejercicio1_3(self):
        self.assertEqual(main.respuesta_ejercicio1([-6, -3, 0, 1, 4], -2, 4, 10), [-86, -20, -6, 10, 12])

    def test_ejercicio1_4(self):
        self.assertEqual(main.respuesta_ejercicio1([-10, -5, 1, 1, 12], 3, -5, 12), [10, 10, 112, 362, 384])

    def test_ejercicio1_5(self):
        self.assertEqual(main.respuesta_ejercicio1([-10, -6, -2, -1, 0], 4, 5, 7), [6, 7, 13, 121, 357])

if __name__ == '__main__':
    unittest.main()
