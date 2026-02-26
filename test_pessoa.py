"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)
"""

import unittest
from unittest.mock import patch
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa1 = Pessoa('Maitê', 'Mallu')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.pessoa1.nome, str)

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa1.nome, 'Maitê')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.pessoa1.sobrenome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa1.sobrenome, 'Mallu')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.pessoa1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = True

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'CONECTADO')

    def test_attr_dados_obtidos_passa_true(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = True

            self.pessoa1.obter_todos_os_dados()
            self.assertTrue(self.pessoa1.dados_obtidos)


    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = False

            self.assertEqual(self.pessoa1.obter_todos_os_dados(), 'ERRO 404')

    def test_attr_dados_obtidos_passa_false(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = False

            self.pessoa1.obter_todos_os_dados()
            self.assertFalse(self.pessoa1.dados_obtidos)

    def test_attr_dados_obtidos_sequencial_true_false(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.ok = True

            self.pessoa1.obter_todos_os_dados()
            self.assertTrue(self.pessoa1.dados_obtidos)

            mock_request.return_value.ok = False

            self.pessoa1.obter_todos_os_dados()
            self.assertFalse(self.pessoa1.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)
