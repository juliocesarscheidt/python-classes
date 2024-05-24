# Calculando porcentagens com Python


### Calcular quanto ficaria 500 MAIS 35%

```python
valor_inicial = 500
x = 35

multiplicador = (100 + x) / 100
# 1.35
valor_inicial = valor_inicial * multiplicador
#               500 * 1.35 = 675.0

# atribuicao direta
valor_inicial *= multiplicador
# 675.0
```

```python
# valor_inicial = valor_inicial * (100 + x) / 100
# 675.0

# atribuicao direta
# valor_inicial *= (100 + x) / 100
# 675.0
```

```python
def adicionar_porcentagem(valor, porcentagem):
  return valor * (100 + x) / 100

adicionar_porcentagem(500, 35)
# 675.0
```



### Calcular quanto ficaria 500 MENOS 35%

```python
valor_inicial = 500
x = 35

multiplicador = (100 - x) / 100
# 0.65
valor_inicial = valor_inicial * multiplicador
#               500 * 0.65 = 325.0

# atribuicao direta
valor_inicial *= multiplicador
# 325.0
```

```python
def subtrair_porcentagem(valor, porcentagem):
  return valor * (100 - x) / 100

subtrair_porcentagem(500, 35)
# 325.0
```
