

def cores_favaoritaas(*wargs):
    return wargs * 4


# lst = [1,1,2,3,4,5,4]

# res = [cores_favaoritaas(lst) for num in lst]

# res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in lst]
# print(res)

# print(10 % 2)

# decoradores 
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de  {acompanhamento}, por favor.'


print(saudacao('Marc'))
print(ordenar('frango', 'Batata'))



