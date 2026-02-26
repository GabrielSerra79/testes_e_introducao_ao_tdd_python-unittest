import requests
from pprint import pprint

class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            self.dados_obtidos = False
            return 'ERRO 404'


if __name__ == '__main__':
    p1 = Pessoa('Loco', 'Muito')

    pprint(p1.obter_todos_os_dados())
