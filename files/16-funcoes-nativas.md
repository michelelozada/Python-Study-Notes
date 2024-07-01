> **Funções nativas do Python**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Funções nativas do Python *(mini-revisão)*
```
- Também conhecidas por funções embutidas ou built-in functions  

- São funções pré-definidas, integrantes da linguagem  

- Fornecem funcionalidades básicas e essenciais para diferentes necessidades de programação

- Estão sempre disponíveis, i.e., não requerem a importação de módulos externos
```

&nbsp;  

## Funções nativas importantes *(referência rápida)*

#### • Funções de entrada e saída
*Como o nome sugere, manipulam a entrada e saída de dados*

Função | Finalidade 
---    | :--
input() | Permite a entrada de um usuário durante a execução do programa
print() | Exibe mensagens na saída padrão 

&nbsp;  

#### • Funções de conversão de tipos
*Criam/retornam instâncias de classes. Também chamadas de funções construtoras*

Função | Finalidade 
---    | :--
bool() | Converte um valor para um tipo booleano 
dict() | Converte um valor para um  novo dicionário
float() | Converte um valor para um tipo ponto flutuante 
int() | Converte um valor para um tipo inteiro 
list() | Converte um valor para uma nova lista  
set() | Converte um valor para um novo conjunto de dados
str() | Converte um valor para um tipo string 
tuple() | Converte um valor para uma nova tupla

&nbsp;  

#### • Funções matemáticas
*Lidam com operações matemáticas básicas*

Função | Finalidade 
---    | :--
abs() | Retorna o valor absoluto de um número
max() | Retorna o maior item de um iterável (ou o maior de 2 ou mais argumentos)
min() | Retorna o menor item em um iterável (ou o menor de 2 ou mais argumentos)
round() | Retorna um número arredondado para um determinado número de casas decimais
sum() | Retorna a soma de um iterável 

&nbsp;  

#### • Funções de sequência
*Operam em sequências de elementos, como listas, tuplas, strings, etc.*

Função | Finalidade 
---    | :--
enumerate() | Retorna uma sequência de tuplas contendo os índices e valores correspondentes do iterável
len() | Retorna o número de elementos de um objeto (lista, tupla, string, etc.)
sorted() | Retorna uma nova lista ordenada, partindo dos elementos de um iterável
zip() | Combina elementos de múltiplos iteráveis (listas, tuplas, etc), retornados em tuplas

&nbsp;  

#### • Funções de controle de fluxo
*Utilizadas para controlar o fluxo do programa ou aplicar operações em massa a elementos*

Função | Finalidade 
---    | :--
filter() | Filtra itens de um iterável com base em uma função especificada
map() | Aplica uma função a todos os itens de um iterável e retorna uma lista dos resultados
range() | Retorna uma sequência de números 

&nbsp;  

#### • Funções de introspecção e inspeção
*Obtêm informações sobre objetos e tipos de dados em tempo de execução*

Função | Finalidade 
---    | :--
isinstance() | Verifica se objeto é uma instância de uma determinada classe
type() | Retorna o tipo de um objeto em Python

&nbsp;  

## Exemplos de aplicações das funções nativas

#### • Função enumerate()
◦ Na sintaxe da função, o primeiro argumento é o iterável  
◦ Um segundo argumento, referente ao valor inicial do índice, pode estar implícito ou explícito  
◦ Retorna uma sequência de tuplas com os valores dos índices + os próprios elementos de uma sequência iterada  
◦ Nos permite acessar o índice e valor de um item da lista   

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

#### • Função len()
```py

string = "Python"
tamanho = len(string)
print(tamanho)  

# Retorna: 6
```


#### • Função range()
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

#### • Função zip()
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

## Referências extras consultadas
> [Python enumerate() – What is the Enumerate Function in Python?](https://www.freecodecamp.org/news/python-enumerate-what-is-the-enumerate-function-in-python/), artigo de Ihechikara Vincent Abba  

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>