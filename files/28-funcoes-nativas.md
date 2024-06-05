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
[len()](https://github.com/michelelozada/Python-Study-Notes/edit/main/files/28-funcoes-nativas.md#fun%C3%A7%C3%A3o-len) | Retorna o comprimento/número de itens de um objeto (lista, tupla, string, etc.)
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
[enumerate()](https://github.com/michelelozada/Python-Study-Notes/edit/main/files/28-funcoes-nativas.md#fun%C3%A7%C3%A3o-enumerate) | Retorna  uma sequência de tuplas contendo um índice e o valor correspondente do iterável. Ùtil para percorrer 2 listas.
[range(https://github.com/michelelozada/Python-Study-Notes/blob/main/files/28-funcoes-nativas.md#fun%C3%A7%C3%A3o-range)](funcao-range)| Geralmente usado em loops, gera uma sequência de números
[zip()](https://github.com/michelelozada/Python-Study-Notes/edit/main/files/28-funcoes-nativas.md#fun%C3%A7%C3%A3o-zip) | Combina elementos de múltiplos iteráveis (listas, tuplas, etc) em tuplas

&nbsp;  

#### 5. Funções para manipulação de strings
Funções | Finalidade 
---     | ---
format() | Formata uma string
len() | Retorna o comprimento de uma string
str() | Converte um valor para uma string
strip() | Remover espaços em branco (ou outros caracteres especificados) do início e do final de uma string 

&nbsp;  

## Exemplos de aplicações das funções para iteração e filtragem

### Função enumerate()
- Na sintaxe da função, o primeiro argumento é o iterável  
- Um segundo argumento, referente ao valor inicial do índice, pode estar implícito ou explícito  
- Retorna uma sequência de tuplas com os valores dos índices + os próprios elementos de uma sequência iterada  
- Nos permite acessar o índice e valor de um item da lista   

```py

estacoes = ['primavera', 'verao', 'outono', 'inverno']
enumEstacoes = enumerate(estacoes)

print(list(enumEstacoes))

Retorna:
[(0, 'primavera'), (1, 'verao'), (2, 'outono'), (3, 'inverno')]
```
```py

estacoes = ['primavera', 'verão', 'outono', 'inverno']

# Aqui `start` está implícito e valor índice começa, portanto, como zero 

for indice, estacao in enumerate(estacoes):
  print(f'índice: {indice} - item: {estacao}')
	
Retorna: 
índice: 0 - item: primavera
índice: 1 - item: verão
índice: 2 - item: outono
índice: 3 - item: inverno
```	
```py

estacoes = ['primavera', 'verão', 'outono', 'inverno']

# Aqui `start` foi definido para que o valor inicial do índice comece como 1 

for indice, estacao in enumerate(estacoes, start=1):
  print(f'índice: {indice} - item: {estacao}')

	
Retorna: 
índice: 1 - item: primavera
índice: 2 - item: verão
índice: 3 - item: outono
índice: 4 - item: inverno	

```

&nbsp;

### Função range()
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

### Função zip()
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

## Exemplos de aplicações das funções para manipulação das strings

### Função len()
```py

string = "Python"
tamanho = len(string)
print(tamanho)  

# Retorna: 6
```

&nbsp;

### :link: Links de apoio consultados
[Python enumerate() – What is the Enumerate Function in Python?](https://www.freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python/) por Ihechikara Vincent Abba

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>