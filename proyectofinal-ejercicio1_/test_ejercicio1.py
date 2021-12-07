import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio1(self):
        self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], -1, 3, 5), [-23, -5, 1, 7])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        # self.assertEqual(main.respuesta_ejercicio1([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])

if __name__ == '__main__':
    unittest.main()
