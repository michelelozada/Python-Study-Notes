> **Funções nativas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### Funções nativas 
- Também chamadas de funções embutidas ou *built-in functions*  
- São funções pré-definidas, integrantes da linguagem  
- Sempre disponíveis (não requerem a importação de módulos adicionais)  

&nbsp;  

#### 1. Funções para manipulação de dados:
Funções | Finalidade 
---     | ---
input() | Recebe (= lê) a entrada de um usuário, via teclado, como uma string
len() | Retorna o comprimento/número de itens de um objeto (lista, tupla, string, etc.)
print() | Exibe (= imprime) um objeto no console 
type() | Retorna o tipo de um objeto 

&nbsp;  

#### 2. Funções para conversão de tipos:
Funções | Finalidade 
---     | ---
bool() | Converte um valor para um tipo booleano
float() | Converte um valor para um tipo ponto flutuante
int() | Converte um valor para um tipo inteiro
list() | Converte um iterável para uma lista
str() | Converte um valor para um tipo string

&nbsp;  

#### 3. Funções matemáticas
Funções | Finalidade 
---     | ---
abs() | Retorna o valor absoluto de um número
max() | Retorna o valor máximo de uma sequência de números
min() | Retorna o valor mínimo de uma sequência de números
round() | Arredonda um número para um determinado número de casas decimais
sum() | Retorna a soma de uma sequência de números

&nbsp;  

#### 4. Funções para iteração e filtragem
Funções | Finalidade 
---     | ---
filter() | Filtra itens de um iterável com base em uma função
map() | Aplica uma função a todos os itens de um iterável
sorted() | Retorna uma lista ordenada a partir dos elementos de um iterável
enumerate() | Retorna  uma sequência de tuplas contendo um índice e o valor correspondente do iterável
range() | Geralmente usado em loops, gera uma sequência de números
zip() | Combina elementos de múltiplos iteráveis (listas, tuplas, etc) em tuplas

&nbsp;  

#### 5. Funções para manipulação de strings
Funções | Finalidade 
---     | ---
format() | Formata uma string
len() | Retorna o comprimento de uma string
str() | Converte um valor para uma string

&nbsp;  

### Exemplos de aplicações das funções para iteração e filtragem

## Função enumerate()
```py

vogais = ['a', 'e', 'i', 'o', 'u']
for indice, valor in enumerate(vogais):
  print(indice, valor)

# Retorna:
0 a
1 e
2 i
3 o
4 u
```

&nbsp;

## Função range()
```py

for i in range(4):
  print(i)
	
# Retorna:
0
1
2
3
```

&nbsp;

## Função zip()
```py

nomes = ["Ana", "Bela", "Cida"]
idades = [12, 24, 48]
for nome, idade in zip(nomes, idades):
  print(nome, idade)
	
# Retorna:	
Ana 12
Bela 24
Cida 48
```

&nbsp;

### Exemplos de aplicações das funções para manipulação das strings

## Função len()
```py

string = "Python"
tamanho = len(string)
print(tamanho)  

# Retorna: 6
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>