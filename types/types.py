from collections import namedtuple


for t in str, int, float, bool, list, dict, set, tuple, object:
    print(type(t))
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>
# <class 'type'>


# tipos primitivos
# strings
texto = "texto"
print(type(texto))
# <class 'str'>
texto = """
novo texto
"""
print(type(texto))
# <class 'str'>
print(isinstance(texto, object))
# True
texto = "texto"
texto = texto + " + novo texto concatenado"  # concatenando textos
print(texto)
# texto + novo texto concatenado
texto = f"{texto} + segundo novo texto concatenado"  # concatenando textos
print(texto)
# texto + novo texto concatenado + segundo novo texto concatenado


# numeros inteiros
numero_inteiro = 20
print(type(numero_inteiro))
# <class 'int'>
print(isinstance(numero_inteiro, object))
# True
numero_inteiro = numero_inteiro + 5
print(numero_inteiro)
# 25

# ponto flutuante
numero_real = 25.0
print(type(numero_real))
# <class 'float'>
print(isinstance(numero_real, object))
# True
print(numero_real)
# 25.0
print("%.4f" % numero_real)
# 25.0000
print("{:.4f}".format(numero_real))
# 25.0000

# somando inteiros com numeros reais gera um numero real
print(numero_real + numero_inteiro)
# 50.0
print(numero_inteiro + numero_real)
# 50.0
print(type(numero_inteiro + numero_real))
# <class 'float'>


# valores logicos
booleano = False
print(type(booleano))
# <class 'bool'>
print(booleano)
# False
booleano = not booleano  # negacao, inverte o valor
print(booleano)
# True


# tipos complexos
# lista - vetor de valores, array
lista = []
# lista = list()
print(type(lista))
# <class 'list'>
lista.append(1)
lista.append(2)
print(lista)
# [1, 2]
print(lista[0])
# 1
matriz = [[1, 2], [3, 4]]
print(type(matriz))
# <class 'list'>
print(matriz)
# [[1, 2], [3, 4]]
print(matriz[0][1])
# 2
print(matriz[1][0])
# 3

matriz_dynamica = list(range(10))
print(matriz_dynamica)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list comprehension [expr for item in lista if cond]
matriz_dynamica = [i for i in range(10) if i % 2 == 0]
print(matriz_dynamica)
# [0, 2, 4, 6, 8]


# dicionario, mapa de chave e valor => key: value
dicionario = {}
# dicionario = dict()
dicionario = {"chave_1": "valor_1"}
print(type(dicionario))
# <class 'dict'>
dicionario.update({"chave_2": "valor_2"})
print(dicionario)
# {'chave_1': 'valor_1', 'chave_2': 'valor_2'}
dicionario["chave_3"] = "valor_3"
print(dicionario)
# {'chave_1': 'valor_1', 'chave_2': 'valor_2', 'chave_3': 'valor_3'}
del dicionario["chave_2"]
print(dicionario)
# {'chave_1': 'valor_1', 'chave_3': 'valor_3'}


# conjunto, nao armazena valores repetidos
# conjunto = {'a', 'b', 'c', 'd'}
conjunto = set()
conjunto.add("a")
conjunto.add("b")
conjunto.add("c")
conjunto.add("d")
conjunto.add("d")  # valor repetido
conjunto.add("d")  # valor repetido
print(type(conjunto))
# <class 'set'>
print(conjunto)  # pode estar em outra ordem
# {'c', 'b', 'd', 'a'}
conjunto.update(["e", "f", "g", "h"])
print(conjunto)
# {'e', 'b', 'd', 'a', 'f', 'g', 'c', 'h'}
print(sorted(conjunto))  # retorna uma lista
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# tupla, imutavel, nao pode ser alterada
tupla_simples = 0, 1, 2
# tupla_simples = (0, 1, 2)
# tupla = tuple()
print(type(tupla_simples))
# <class 'tuple'>
print(tupla_simples)
#  (0, 1, 2)
print(tupla_simples.index(0))
# 0
print(3 in tupla_simples)
# False

tupla_um_elemento = (0,)
# tupla_um_elemento = (0,)
print(type(tupla_um_elemento))
# <class 'tuple'>
print(tupla_um_elemento)
# (0,)

tupla_composta = (tupla_simples, (3, 4, 5))
# tupla = tuple()
print(type(tupla_composta))
# <class 'tuple'>
print(tupla_composta)
# ((0, 1, 2), (3, 4, 5))


Estados = namedtuple("Estados", ["sigla", "nome"])
print(type(Estados))
# <class 'type'>

estado_pr = Estados("PR", "Paraná")
print(estado_pr)
# Estados(sigla='PR', nome='Paraná')
print(estado_pr.nome)
# Paraná

estado_sp = Estados("SP", "São Paulo")
print(estado_sp)
# Estados(sigla='SP', nome='São Paulo')
print(estado_sp.nome)
# São Paulo


# classes, por padrao herdam do object
# class ClasseExemplo(object):
class ClasseExemplo:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "ClasseExemplo str representation"


objeto = ClasseExemplo()
print(type(objeto))
# <class '__main__.ClasseExemplo'>
print(objeto)
# ClasseExemplo str representation
print(isinstance(objeto, ClasseExemplo))
# True
print(isinstance(objeto, object))
# True
print(isinstance(objeto, dict))
# False


# outros tipos
def funcao() -> str:
    return "Hello World"


print(type(funcao))
# <class 'function'>
print(funcao())
# "Hello World"


# comentario

"""
outro comentario
com multiplas linhas
"""
