import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio10_1(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1],[2,3],[4,5]], 6), 3)

    def test_ejercicio10_2(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1],[1,2],[2,3],[3,4]], 5), 1)

    def test_ejercicio10_3(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1],[1,2],[2,3],[4,5],[5,6]], 7), 2)

    def test_ejercicio10_4(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,6],[5,4],[7,8],[3,2],[2,1]], 9), 4)

    def test_ejercicio10_5(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1]], 2), 1)

if __name__ == '__main__':
    unittest.main()
