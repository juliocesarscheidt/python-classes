
## Operadores aritméticos

```text
adição +                    2 + 10    = 12      (se ambos forem int, o resultado é int, senão o resultado é float)  
subtração -                 8 - 2     = 6       (se ambos forem int, o resultado é int, senão o resultado é float)  
multiplicação *             2 * 4     = 8       (se ambos forem int, o resultado é int, senão o resultado é float)  
divisão /                   10 / 5    = 2.0     (resultado é float)  
divisão inteiro //          10 // 5   = 2       (resultado é int)  
exponenciação **            4 ** 2    = 16  
resto %                     5 % 2     = 1  
```

> exemplos

```python
numero1 = 15
numero2 = 20

numero1 + numero2
35
```


## Operadores de comparação - retorna valores booleanos

```text
==                  1 == 1    = True     (compara valores)  
>=                  2 >= 4    = False  
<=                  2 <= 4    = True  
>                   2 > 8     = False  
<                   2 < 8     = True  
!=                  2 != 8    = True     (compara valores)  

is                  compara referência  
```

> exemplos

```python
numero1 == numero2
False

lista_a = [0, 1, 2]
lista_b = [0, 1, 2]

lista_a is lista_b
# False
lista_a == lista_b
# True
```


## Operadores lógicos/booleanos

```text
and         E               (&&)
or          OU              (||)
not         NÃO             (!)
```

> exemplos

```python
# AND
True and True
# True

True and False
# False

False and True
# False

False and False
# False


# OR
True or True
# True

True or False
# True

False or True
# True

False or False
# False


# NOT
not True
# False

not False
# True
```
