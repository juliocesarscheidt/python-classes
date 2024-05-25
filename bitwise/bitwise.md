# Bitwise¨& Bit Shift

```text
1    0000 0001
2    0000 0010
3    0000 0011
4    0000 0100
5    0000 0101
6    0000 0110
7    0000 0111
8    0000 1000
9    0000 1001
10   0000 1010
11   0000 1011
12   0000 1100
...
```

## Bitwise

### Bitwise AND (&)

AND só retorna 1 se os DOIS bits forem 1, senão retorna 0

```python
1 & 1
# 1

"""
    1
and 1
    ----
    1
"""
```

```python
2 & 2
# 2

"""
    10
and 10
    ----
    10
"""
```

```python
8 & 4
# 0

"""
    1000
and  100
    ----
    0000
"""
```

> Verificando se um numero é divisivel por 2, aqui deve retornar 0

```python
2 & 1
# 0

3 & 1
# 1

4 & 1
# 0

5 & 1
# 1
```

```python
2 & 1
# 0

"""
    10
and  1
    ----
    00
"""
```

### Bitwise OR (|)

AND retorna 1 se ALGUM dos dois bits forem 1, senão retorna 0

```python
1 | 1
# 1

"""
   1
or 1
   ----
   1
"""
```

```python
2 | 2
# 2

"""
   10
or 10
   ----
   10
"""
```

```python
8 | 4
# 12

"""
   1000
or  100
   ----
   1100
"""
```

```python
12 | 4
# 12

"""
   1100
or  100
   ----
   1100
"""
```

### Bitwise XOR (^)

XOR é "ou exclusivo", retorna 1 se APENAS 1 dos dois bits forem 1
(QUALQUER NUMERO XOR ELE MESMO É IGUAL A ZERO)

```python
1 ^ 1
# 0

"""
      1
xor   1
      ----
      0
"""
```

```python
8 ^ 4
# 12

"""
    1000
xor  100
    ----
    1100
"""
```

```python
12 ^ 4
# 8

"""
   1100
or  100
   ----
   1000
"""
```

### Bitwise NOT

Bitwise NOT para um inteiro de 32-bits "x" produz o resultado de "-(x + 1)"

```text
~256      => -257
  -(256 + 1) = -257

~0        => -1
  -(0 + 1) = -1

~1        => -2
  -(1 + 1) = -2

~5        => -6
  -(5 + 1) = -6

~-8       => 7
  -(-8 + 1) = 7
```

## Bit Shift

### Right Shift (>>) & Left Shift (<<)

move os bits para esquerda ou direta

```python
1 >> 1
# 0

"""
      0001
      ----
>> 1  0000
"""
```

```python
2 >> 1
# 1

"""
      0010
      ----
>> 1  0001
"""
```

```python
11 >> 1
# 5

"""
      1011
      ----
>> 1  0101
"""
```

```python
11 >> 2
# 2

"""
      1011
      ----
>> 2  0010
"""
```

```python
1 << 1
# 2

"""
      0001
      ----
<< 1  0010
"""
```

```python
11 << 2
# 44

"""
      0000 1011
      ----
<< 2  0010 1100
"""
```

```python
1 << 8
# 256

"""
       0 0000 0001
<<8    1 0000 0000
"""

int('100000000', 2) # ou int(0b100000000)
# 256

bin(256)
# 0b100000000
```
