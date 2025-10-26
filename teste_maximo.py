import unittest
from io import StringIO
from unittest.mock import patch
from main import maximo


class TestMaximo(unittest.TestCase):
    def test_primeiro_menor_que_segundo(self):
        with patch('sys.stdout', new=StringIO()) as saida:
            maximo(10, 20)
            self.assertEqual(saida.getvalue().strip(), "O numero 20 é o maior")

    def test_segundo_menor_que_primeiro(self):
        with patch('sys.stdout', new=StringIO()) as saida:
            maximo(50, 30)
            self.assertEqual(saida.getvalue().strip(), "O numero 50 é o maior")

    def test_numeros_iguais(self):
        with patch('sys.stdout', new=StringIO()) as saida:
            maximo(7, 7)
            self.assertEqual(saida.getvalue().strip(), "O numero 7 é o maior")


if __name__ == '__main__':
    unittest.main()
