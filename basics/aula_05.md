
## Primeiro script

script.py

```python
name = input("Digite seu nome:")
print("name", name)

if name.lower().startswith("a"):
  print(f"O nome {name} começa com a")
else:
  print(f"O nome {name} NÃO começa com a")
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
def dizer_ola(nome: str, idade: int) -> None:
  print("ola pessoa " + nome + " de idade " + str(idade)) # concatenação

  print("ola pessoa {} de idade {}".format(nome, idade)) # format - template

  # %d int | %f float | %s string | %x hexadecimal | etc
  print("ola pessoa %s de idade %d" % (nome, idade)) # especificação de formato - template
  print("ola pessoa %(nome)s de idade %(idade)d" % {"nome": nome, "idade": idade}) # especificação de formato - template

  print(f"ola pessoa {nome} de idade {idade}") # template - string interpolation - Python 3.6+

# invocação regular
dizer_ola("julio", 50)

# usando argumentos nomeados
dizer_ola(nome="julio", idade=50)
# dizer_ola(idade=50, nome="julio")
```


```python
def calcular_ano_bissexto(ano: int) -> bool:
  # ano é bissexto se dividido por 4 o resto for 0
  return ano % 4 == 0

print(calcular_ano_bissexto(2024))
# True

# usando unpacking
ano_dict = {"ano": 2025}
print(calcular_ano_bissexto(**ano_dict))
# False

# com valor padrão
def calcular_ano_bissexto_com_valor_padrao(ano: int = 2024) -> bool:
  return ano % 4 == 0
print(calcular_ano_bissexto())
# True
```
