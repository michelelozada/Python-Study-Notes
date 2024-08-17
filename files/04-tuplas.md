> **Tuplas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;

&nbsp;  
## Tuplas em Python *(mini-revisão)*
```
- Classe associada: tuple

- Cada item dentro da tupla é chamado de elemento (ou mesmo de item) 

- É um estrutura de dados de sequência imutável, i.e., após a criação da tupla, elementos não podem 
ser modificados, adicionados ou removidos dali 

- Tuplas são ordenadas, i.e., sua ordem é baseada na sequência em que os elementos foram ali inseridos

- Podem conter itens de diferentes tipos

- Elementos são acessados pela posição/por seu índice na tupla

- Exemplo da sintaxe básica: (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
```

&nbsp;

## Desempacotamento (ou unpacking) de tuplas 
Técnica para lidar com iteráveis (tuplas, listas, etc.) que permite a atribuição de valores a variáveis individuais, de forma rápida e concisa. 

&nbsp;

↳ Desempacotamento simples
```py

idades = (8, 9, 10)

# Desempacotando a tupla
a, b, c = idades

print(a)  # Saída: 8
print(b)  # Saída: 9
print(c)  # Saída: 10
```

&nbsp;

```py

tupla = (20,)

elemento, = tupla

print(elemento)  # Saída: 20
```

&nbsp;

↳ Desempacotamento com o operador asterisco (*)
Disponível a partir do Python 3, sendo que este operado captura os demais itens de uma tupla  

```py

idades = (8, 9, 10, 11, 12)

# Desempacotando a tupla
a, b, *outras = idades

print(a)       # Saída: 8
print(b)       # Saída: 9
print(outras)  # Saída: [10, 11, 12]
```
```py

idades = (8, 9, 10, 11, 12)

# Desempacotando a tupla
*primeiras, d, e = idades

print(primeiras)  # Saída: [8, 9, 10]
print(d)  # Saída: 11
print(e)  # Saída: 12
```

&nbsp;

## Testando se uma tupla possui elementos ou se está vazia
*Em Python, uma tupla vazia é considerada um valor falso (False) num contexto booleano. Portanto, quando se usa uma tupla em uma condição if, é verificado se a tupla está vazia ou não, sendo que uma tupla com elementos é considerada True e uma tupla vazia é considerada False.* 

```py

numeros = (1, 2, 3)

if numeros:
  print("A tupla de números não está vazia.")
else:
  print("A tupla de números está vazia.")

# Saída: A tupla de número não está vazia.
```
```py

letras = ()
if letras:
  print("A tupla de letras não está vazia")
else:
  print("A tupla de letras está vazia")
  
# Saída: A tupla de letras está vazia
```

&nbsp;

## Verificando se um elemento está presente em uma tupla
É feito através do operador `in`, que verifica se um determinado valor está em uma sequência (como lista, tupla, string, set ou dicionário), retornando um valor booleano a respeito do elemento ter sido encontrado (ou não).

```py

numeros = (1, 2, 3, 4, 5)
print(0 in numeros)

# Saída: False 
```

&nbsp;

## Operações de manipulações de tuplas 

#### • Concatenação de tuplas
*Quando são combinadas duas ou mais tuplas para criar uma nova tupla maior*

```py

numeros = (1, 2, 3)
letras = ('a', 'b', 'c')
combinacao = letras + numeros
print(combinacao)

# Saída: ('a', 'b', 'c', 1, 2, 3)
```

&nbsp;

#### • Acesso a elementos específicos pelo índice
*Quando se utiliza o índice para se obter um elemento específico armazenado dentro de uma tupla*

```py

frutas = ('Laranja', 'Mamão', 'Uva')
print(frutas[1])

# Saída: Mamão
```

&nbsp;

#### • Slicing para extrair partes específicas da tupla
*Para isso, utilize a notação de slicing (`:`)*

```py

vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais[1:4])

# Saída: ('e', 'i', 'o')
```

&nbsp;

#### • Desempacotamento de tuplas
*Para atribuir os elementos de uma tupla a variáveis individuais numa única operação*

```py

apelidos = ('Bia', 'Cida', 'Nando')
a, b, c = apelidos

print(a)  # Saída: Bia
print(b)  # Saída: Cida
print(c)  # Saída: Nando
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>