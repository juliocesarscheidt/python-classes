
Definindo variáveis para utilização

```python
numero1 = 15
numero2 = 20
```


## Condicionais / controle de fluxo

### if - SE (expressão booleana)

```python
if numero1 > numero2:
  print("numero1 e maior que o numero2")
```

### elif - SE ENTÂO (expressão booleana)

```python
elif numero1 < numero2:
  print("numero1 e menor que o numero2")
```

### else - SENÂO

```python
else:
  print("numero1 e igual ao numero2")
```

### Outro exemplo

```python
if numero1 == numero2:
  print("numero1 e igual ao numero2")
else:
  print("numero1 e diferente do numero2")
```


## Loops / laços

### for - PARA - para cada elemento, faça

```python
for i in range(0, 10):
  print(i)

# iterando em uma lista
lista_a = [1, 2, 3, 4]
for elemento in lista_a:
  print(elemento)

# iterando em um conjunto - set
for elemento in {1, 2, 3, 4}:
  print(elemento)
```


### While - ENQUANTO - enquanto uma expressão for atendida, faça algo

```python
i = 0
while i < 10:
  print(i)
  i += 1
```


## Controle de fluxo

### Break - INTERROMPER - (só pode ser usado em loop)

```python
for i in range(0, 10):
  if i == 5:
    break
  else:
    print(i)
                              
from time import sleep
segundos_decorridos = 0
while True:
  sleep(1)
  segundos_decorridos = segundos_decorridos + 1
  print("segundos_decorridos", segundos_decorridos)
  if segundos_decorridos >= 4:
    break
```


### Continue - CONTINUAR - só pode ser usado em loop

```python
for i in range(0, 10):
  if i == 5:
    continue
  else:
    print(i)
```


### Pass - AVANÇAR - ignorar alguma condição

```python
for i in range(0, 10):
  if i % 2 != 0:
    pass
  else:
    print(i)

if numero1 == numero2:
  pass # apenas ignora esse caso
```
