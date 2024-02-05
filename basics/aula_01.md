# Linguagens de Programação

Uma linguagem de programação é um conjunto de instruções escritas de forma padronizada, agindo como intermediário entre o programador humano e a máquina/computador.

Algoritmos funcionam como "receitas de bolo", onde são descritos o passo a passo que a máquina deve executar.


## Computador entende binario

0         0000
1         0001
2         0010
3         0011
4         0100
5         0101
6         0110
7         0111
8         1000
...



## Linguagens interpretadas

  Linguagem interpretada é uma linguagem de programação em que o código fonte
  é executado por um programa de computador chamado interpretador (ao invés de serem compiladas),
  onde a interpretação e a execução do programa acontecem em tempo real e independente do sistema operacional utilizado.

  Geralmente possuem um REPL (read eval print loop)

  Exemplos: javascript, python, php, ruby, shellscript

## Linguagens compiladas

  Linguagem compilada é uma linguagem de programação em que o código fonte, nessa linguagem,
  é executado diretamente pelo sistema operacional ou pelo processador (ou alguma máquina virtual, ex. JVM do Java),
  após ser traduzido por meio de um processo chamado compilação, usando um programa de computador chamado compilador,
  para uma linguagem de baixo nível, como linguagem de montagem (assembly) ou código de máquina

  Exemplos: java, csharp, c, c++, golang, rust



## Paradigmas

Procedural/imperativa
  Organiza o programa como uma sequência de procedimentos ou rotinas.
  Exemplos: fortran, c

Orientado a objetos OO - programação orientada a objetos POO
  Modela o programa em termos de objetos, que são instâncias de classes que encapsulam dados/atributos e comportamentos/metodos
  Exemplos: csharp, java, c++, typescript
  Outras linguagens como python, php, javascript, incorporam alguns conceitos da POO

Funcional
  Baseia-se no conceito de funções matemáticas, evitando estados mutáveis e dados globais.
  Exemplos: haskell, lisp, scala
  Outras linguagens incorporam conceitos funcionais, como javascript, python, e até java nas versões mais atuais

Orientado a Eventos
  O programa responde a eventos gerados pelo sistema ou usuário
  Exemplos: javascript, visual basic

Existem outras além destas, como Orientada a Aspectos, Baseado em Restrições.



## Base das linguagens

variaveis
  sao armazenadas em memória, e então recuperadas quando acessadas
  possuem endereço na memória
  - algumas linguagens possuem também constantes

funções/metodos - procedimentos
  encapsulam lógicas, trechos, sequencias de instruções em algo que pode ser reutilizado posteriormente



## Sintaxe

Regras que definem a estrutura gramatical dos elementos em um código fonte.

Estabelece como as instruções devem ser escritas para que o compilador ou interpretador da linguagem possa compreendê-las e executá-las corretamente.

Exemplos:
  palavras-chave: if, else, for, while, ...

  delimitadores: delimitam os trechos de código, exemplo ";" "{" "}"

  indentação: necessário uso de indentação com "tab" em algumas linguagem

  comentários:  
    # ...  
    // ...  
    /* ... */  

