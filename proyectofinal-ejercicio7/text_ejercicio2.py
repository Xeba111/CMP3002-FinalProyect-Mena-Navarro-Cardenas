import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio2_1(self):
        self.assertEqual(main.respuesta_ejercicio2([2,4,6,8,10]), 7)
        main.contador = 0
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])

    def test_ejercicio2_2(self):
        self.assertEqual(main.respuesta_ejercicio2([7,7,7,7,7]), 16)
        main.contador = 0

    def test_ejercicio2_3(self):
        self.assertEqual(main.respuesta_ejercicio2([7,7,7,7,7]), 16)
        main.contador = 0

if __name__ == '__main__':
    unittest.main()
