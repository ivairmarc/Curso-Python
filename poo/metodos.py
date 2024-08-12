


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class Usuario:
    
    contador = 0

    def __init__(self, nome, email, senha):
        self.__nome =  nome
        self.__email = email
        self.__senha = senha