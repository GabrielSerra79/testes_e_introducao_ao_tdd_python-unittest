try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest

from calculadora import soma, subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_menos_5_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.7, 3.2),
            (-5, -5, -10),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_como_string_deve_retornar_assertionerros(self):
        with self.assertRaises(AssertionError):
            soma('11', 15)

    def test_soma_y_como_string_deve_retornar_assertionerros(self):
        with self.assertRaises(AssertionError):
            soma(11, '15')


    def test_subtrai_15_e_5_deve_retornar_10(self):
        self.assertEqual(subtrai(15, 5), 10)

    def test_subtrai_menos_5_e_5_deve_retornar_10(self):
        self.assertEqual(subtrai(-5, 5), -10)

    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 0),
            (5, 5, 0),
            (5, 15, -10),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_subtrai_x_como_string_deve_retornar_assertionerros(self):
        with self.assertRaises(AssertionError):
            subtrai('11', 15)

    def test_subtrai_y_como_string_deve_retornar_assertionerros(self):
        with self.assertRaises(AssertionError):
            subtrai(11, '15')

if __name__ == '__main__':
    unittest.main(verbosity=2)
