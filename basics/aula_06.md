
## args e kwargs

- argumentos nao nomeados *args  
- argumentos nomeados **kwargs

```python
def func1(*args):
  print(type(args))
  for arg in args:
    print(arg)

func1("Python", "Javascript", "Golang")
# <class 'tuple'>
# Python
# Javascript
# Golang

# nao funciona
# func1(a="Python", b="Javascript", c="Golang")
```

```python
def func2(**kwargs):
  print(f"argumentos: {kwargs}")
  print(type(kwargs))
  print(list(kwargs.keys()))
  for key in kwargs.keys():
    print(kwargs[key])

func2(a="Python", b="Javascript", c="Golang")
# argumentos: {'a': 'Python', 'b': 'Javascript', 'c': 'Golang'}
# <class 'dict'>
# ['a', 'b', 'c']
# Python
# Javascript
# Golang
```


## Módulos

```python
from internal_module.script import calcular_ano_bissexto

print(calcular_ano_bissexto(2024))
# True
```


## Pacotes

pip - package manager do Python, usado para instalar pacotes

Pacote math já vem por padrão na instalação do Python

```python
from math import sqrt # importa uma função específica
# import math # importa o pacote inteiro/todos os modulos
# from math import sqrt as square_root # importação com alias

print(sqrt(4))
# 2.0
# print(math.sqrt(16))
# print(square_root(16))
```
