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
type() | Retorna a classe de um objeto em Python 

&nbsp;  

#### 2. Funções para conversão de tipos:
* Essas funções criam/retornam instâncias de classes. Também são chamadas de funções construtoras.  
Funções | Finalidade 
---     | ---
bool() | Converte um valor para um tipo booleano (pertence à classe `bool`)
float() | Converte um valor para um tipo ponto flutuante (pertence à classe `float`)
int() | Converte um valor para um tipo inteiro (pertence à classe `int`)
list() | Converte um iterável para uma lista (pertence à classe `list`)
str() | Converte um valor para um tipo string (pertence à classe `str`)

&nbsp;  

#### 3. Funções matemáticas
Funções | Finalidade 
---     | ---
abs() | Retorna o valor absoluto de um número
max() | Retorna o maior item em um iterável (ou o maior de 2 ou mais argumentos)
min() | Retorna o menor item em um iterável (ou o menor de 2 ou mais argumentos)
round() | Retorna um número arredondado para um determinado número de casas decimais
sum() | Retorna a soma de um iterável 

&nbsp;  

#### 4. Funções para iteração e filtragem
Funções | Finalidade 
---     | ---
filter() | Filtra itens de um iterável com base em uma função especificada
map() | Aplica uma função a todos os itens de um iterável e retorna uma lista dos resultados
sorted() | Retorna uma nova lista, contendo todos os elementos do iterável ordenados
enumerate() | Retorna uma sequência de tuplas contendo os índices e valores correspondentes do iterável
range() | Geralmente usado em loops, retorna uma sequência imutável de números entre dois inteiros
zip() | Combina elementos de múltiplos iteráveis (listas, tuplas, etc), retornados em tuplas

&nbsp;  

#### 5. Funções para manipulação de strings
Funções | Finalidade 
---     | ---
len() | Retorna o comprimento de uma string
str() | Converte um valor para uma string

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

## :link: Referências consultadas
[Python enumerate() – What is the Enumerate Function in Python?](https://www.freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python/), artigo de Ihechikara Vincent Abba

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>