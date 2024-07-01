> **Módulo random**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Módulo random do Python *(mini-revisão)*
```

- O módulo random é uma ferramenta que fornece várias funções para a geração números aleatórios

- Também realiza operações relacionadas à aleatoriedade e amostragem de dados

- Já que faz parte da biblioteca padrão do Python, para utilizá-la, basta utilizar a instrução: import random

- Depois de importá-lo, já é possível acessar todas as funcionalidades deste módulo, prefixando-as sempre com 
random. Ex: random.randint(), random.choice(), etc.
```

&nbsp;  

## Funções de geração de números inteiros aleatórios

Função | Finalidade  
---    | ---  
random.randint(a, b) | Retorna um inteiro aleatório N tal que a <= N <= b
random.randrange(start, stop[, step]) | Retorna um inteiro aleatório entre start e stop, com um possível passo especificado

&nbsp;  

#### • Função randint()

```py

import random

print(random.randint(10, 20))

# Na saída, irá retornar um número entre 10 e 20, ambos inclusos como opções
```

&nbsp;  

#### • Função randrange()

```py

import random

print(random.randrange(10, 20))

# Na saída, irá retornar um número entre 10 (este incluso como opção) e 20 (este não incluso)
```

&nbsp;  

## Função de controle e manipulação da semente aleatória

Função | Finalidade  
---    | ---  
seed() | Inicializa o gerador de números aleatórios com um estado específico, determinando a sequência de números aleatórios que serão gerados

&nbsp;  

#### • Função seed()
Sementes aleatórias são valores usados para iniciar o gerador de números pseudoaleatórios (pois são números determinísticos) em um programa de computador. Portanto, quando é definida uma semente aleatória em um programa, está sendo especificado um ponto de partida para a geração de números pseudoaleatórios.

&nbsp;  

↳ Exercício: definindo uma semente aleatória e gerando números aleatórios utilizando a biblioteca random

```py

import random

# Definindo uma semente aleatória
random.seed(123)

# Gerando alguns números aleatórios
print("Números aleatórios gerados:")
for _ in range(5):
  print(random.random())

# Reiniciando a semente aleatória
print("\nReiniciando a semente aleatória e gerando os mesmos números novamente:")
random.seed(123)  # Reiniciando a semente para o mesmo valor
for _ in range(5):
  print(random.random())
```

&nbsp;  

## Funções de amostragem aleatória 
Usadas para embaralhar, selecionar ou extrair subconjuntos aleatórios de dados

Função | Finalidade  
---    | ---  
choice()  | Escolhe apenas um elemento aleatório de uma de uma sequência de elementos
sample()  | Extrai uma amostra aleatória (composta por elementos únicos) de uma sequência de elementos
shuffle() | Usada para embaralhar (ou permutar aleatoriamente) os elementos de uma lista

&nbsp;  

#### • Função choice()
Permite escolher aleatoriamente um único elemento de uma sequência - o que é útil quando você se deseja selecionar um elemento aleatório de uma lista, tupla ou qualquer outra sequência de elemento.

&nbsp; 

↳ Exercício: Escolha aleatória de um nome em uma lista

```py 

import random

nomes = ["Ana", "Barbara", "Carlos", "Davi", "Elen"]

# nomes é a sequência da qual se deseja escolher um elemento aleatório
nome_aleatorio = random.choice(nomes)

print(nome_aleatorio)

# Exemplo de uma das saídas geradas: Carlos
``` 

\* Acima, `random.choice()` escolheu aleatoriamente um nome da lista nomes e o atribuiu à variável nome_aleatorio, sendo que cada item da lista teria a mesma probabilidade de ser escolhido.

&nbsp; 

#### • Função sample()
Realiza uma amostragem aleatória em uma sequência de elementos - o que é útil quando se deseja extrair uma amostra aleatória de uma sequência, sem duplicatas, ou seja, cada elemento na amostra é único.

&nbsp;  

↳ Exercício: Dada a lista de números abaixo, retorne uma lista com três números aleatórios da mesma:

```py 

import random

# a sequência de onde será extraída a amostra
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 3 é o tamanho da amostra que se deseja extrair
amostra = random.sample(numeros, 3)

print(amostra)

# Exemplo de uma amostra aleatória de tamanho 3 da lista numeros, armazenada na lista amostra:
# [40, 100, 10]
```

\* Repare que a função retorna uma nova lista contendo 3 elementos únicos, aleatoriamente selecionados da sequência numeros. Se a sequência numeros possuir elementos duplicados, a amostra gerada não conterá duplicatas.

&nbsp; 

↳ Exercício: Dentro do intervalo de 1 a 50 (ambos inclusos), retorne uma lista com 5 números aleatórios:

```py 

import random

lista = random.sample(range(1,50),5)
print(lista)

# Exemplo de uma das saídas geradas: [39, 9, 22, 41, 27]
```

&nbsp;

#### • Função shuffle() 
Usada para criar uma nova ordem aleatória dos elementos de uma lista, _modificando a lista original, ao invés de retornar uma nova lista_.   


↳ Exercício: Utilizando a função shuffle() para embaralhar os números de uma lista 
```py

import random

# Lista original
lista = [1, 2, 3, 4, 5]

# 'Embaralhamento' da lista
random.shuffle(lista)

# Impressão da lista após o 'embaralhamento'
print(lista)  

# Saída: Elementos dispostos em ordem aleatória 
```


↳ No exemplo abaixo, é usada a semente antes de chamar a função shuffle(), para que o embaralhamento produza sempre o mesmo resultado 

```py

import random

# Lista original
lista = [1, 2, 3, 4, 5]

# Definição a semente
random.seed(40)

# 'Embaralhamento' da lista
random.shuffle(lista)

# Impressão da lista após o 'embaralhamento'
print(lista)  

# Saída: A ordem dos elementos será sempre a mesma para a semente 40
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>