import unittest
import main

class TestCalc(unittest.TestCase):

    def test_ejercicio10_1(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1],[1,2],[3,4],[2,3]], 5), 1)

    def test_ejercicio10_2(self):
        self.assertEqual(main.respuesta_ejercicio10([[0,1],[1,2],[3,4]], 5), 2)

    # def test_ejercicio3_3(self):
    #     self.assertEqual(main.respuesta_ejercicio2([7,7,7,7,7]), 16)
    #
if __name__ == '__main__':
    unittest.main()
