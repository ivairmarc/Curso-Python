"""
PEP 8 
- Utilizar Camel Case para nomes de classes
- Utulizar nomes minusculos, separados por underline para funções ou variaveis
- utilizar 4 espaços para identação
- Duas linhas em branco para separar func, class


# caso tenha muitos importes 
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
"""



class InterarCpf:
    pass


def interar_cpf(cpf):
    alt = 1.79
    peso = 60
    #imc = peso / alt ** 2
    print('*---'*3)
    #print(f'{imc:.2f}')
    print(cpf.zfill(11))

cpf = '9569566'


result = 6/100 * 3000
print(result)

