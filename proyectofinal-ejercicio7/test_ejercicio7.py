import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio7_1(self):
        self.assertEqual(main.respuesta_ejercicio7([2,4,6,8,10]), 7)
        main.contador = 0

    def test_ejercicio7_2(self):
        self.assertEqual(main.respuesta_ejercicio7([7,7,7,7,7]), 16)
        main.contador = 0

    def test_ejercicio7_3(self):
        self.assertEqual(main.respuesta_ejercicio7([1,2,3,4,5,6,7,8,9,10]), 55)
        main.contador = 0

    def test_ejercicio7_4(self):
        self.assertEqual(main.respuesta_ejercicio7([-10,-3,1,5,8,11,15]), 3)
        main.contador = 0

    def test_ejercicio7_5(self):
        self.assertEqual(main.respuesta_ejercicio7([-12,-6,-8,2,5,7,8,9,10,12]), 9)
        main.contador = 0

if __name__ == '__main__':
    unittest.main()
