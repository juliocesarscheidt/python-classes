# Tipagem

As tipagens referem-se à maneira como os tipos de dados são tratados em uma linguagem de programação

Define como os valores podem ser usados e manipulados em um programa


## Tipagem Estática

  Os tipos das variáveis são conhecidos em tempo de compilação,
  e mudanças entre os tipos (conversões/ coerção de tipo/ casts) devem ser explicitas

  Exemplos: java, csharp, c, golang
  
## Tipagem Dinâmica

  O tipo da variável é determinado em tempo de execução pelo interpretador,
  e pode haver mudança do tipo da variavel durante o programa
  
  Exemplos: python, javascript, php


## Iniciando com Python

### Tipos primitivos

```python
# string
nome = "julio"
print(nome)
print(type(nome))

# int
numero = 1
print(type(numero))

# float
flutuante = 1.50
print(flutuante)
# 1.5
print("%.2f" % flutuante)
# 1.50
print(type(flutuante))

# bool
booleano = True
print(type(booleano))
```


### Tipos complexos

#### lista/vetor - lista ordenada de elementos

```python
# lista = [1, 2]
lista = list([1, 2])
print(lista)
# [1, 2]
print(type(lista))

lista.append(3) # adiciona ao final da lista
print(lista)
# [1, 2, 3]
print(lista[2])
# 3
lista.pop(0) # remove o elemento do indice especifico, no caso o primeiro - 0
# 1
print(lista)
# [2, 3]
lista.pop() # remove o ultimo elemento e o retorna
# 3
print(lista)
# [2]
```


#### Dicionario/mapa - armazena chave e valor

```python
dicionario = {"chave_1": "valor_1"}
# dicionario = dict({"chave_1": "valor_1"})
print(dicionario)

dicionario["chave_2"] = "valor_2" # adiciona chave-valor ao dicionario
# dicionario.update({"chave_2": "valor_2"})
del dicionario["chave_1"] # deleta chave do dicionario
print(type(dicionario))
```


#### Conjunto - armazena valores unicos, inordenado

```python
conjunto = {'a', 'b', 'c'}
# conjunto = set({'a', 'b', 'c'})
print(conjunto)

conjunto.add('d')
conjunto.remove('b')
'b' in conjunto
```


#### Tupla - imutavel, nao pode ser alterada

```python
# tupla_simples = 0, 1, 2
tupla_simples = (0, 1, 2)
# tupla_simples = tuple((0, 1, 2))

print(tupla_simples)
print(type(tupla_simples))

tupla_simples[0] = 3
# TypeError: 'tuple' object does not support item assignment

tupla_um_elemento = (0,)
print(tupla_um_elemento)
print(type(tupla_um_elemento))
```
