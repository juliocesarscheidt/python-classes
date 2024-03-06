
## Primeiro script

script.py

```python
name = input("Digite seu nome:")
print("name", name)

if name.startswith("j") or name.startswith("J"):
  print(f"O nome {name} começa com J")
else:
  print(f"O nome {name} NÃO começa com J")
```

> Executar

```bash
python script.py
```


## Funções

def - Definir uma função

```python
def funcao() -> str:
  return "Hello World"

print(type(funcao))
# <class 'function'>
print(funcao())
# "Hello World"
```


Função com argumentos

```python
def dizer_ola(nome: str, idade: int):
  print("ola pessoa " + nome + " de idade " + str(idade))
  print("ola pessoa {} de idade {}".format(nome, idade))
  print("ola pessoa %s de idade %d" % (nome, idade))
  print(f"ola pessoa {nome} de idade {idade}")

dizer_ola("julio", 50)
# usando argumentos nomeados
dizer_ola(nome="julio", idade=50)
# dizer_ola(idade=50, nome="julio")
```


```python
def calcular_ano_bissexto(ano: int):
  # ano é bissexto se dividido por 4 o resto for 0
  return ano % 4 == 0

print(calcular_ano_bissexto(2024))
# True

# usando unpacking
ano_dict = {"ano": 2025}
print(calcular_ano_bissexto(**ano_dict))
# False
```


## Módulos

```python
# modulos
from math import sqrt
# import math
# from math import sqrt as square_root

print(sqrt(4))
# 2.0
# print(square_root(16))
# print(math.sqrt(16))

# square root         16 ** (1/2) = 4
print(4 ** (1/2))
```
