# argumentos nao nomeados *args
# argumentos nomeados **kwargs

def func1(*args):
  for arg in args:
    print(arg)

func1("Python", "Javascript", "Golang")
# Python
# Javascript
# Golang

def func2(**kwargs):
  print(f'argumentos: {kwargs}')
  print(kwargs.keys())
  for arg in kwargs.values():
    print(arg)

func2(a="Python", b="Javascript",  c="Golang")
# argumentos: {'a': 'Python', 'b': 'Javascript', 'c': 'Golang'}
# dict_keys(['a', 'b', 'c'])
# Python
# Javascript
# Golang
