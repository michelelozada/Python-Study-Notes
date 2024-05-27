> **Funções**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Resumo
As funções em Python podem ser:  
1. embutidas  
1. personalizadas  

&nbsp;  

### 1. Funções embutidas  
- Também chamadas de funções nativas ou *built-in functions*  
- São funções pré-definidas, integrantes da linguagem  
- Sempre disponíveis (não requerem a importação de módulos adicionais)  

&nbsp;  

#### 1.1. Para manipulação de dados:
Funções | Finalidade 
---     | ---
input() | Recebe (= lê) a entrada de um usuário, via teclado, como uma string
len() | Retorna o comprimento/número de itens de um objeto (lista, tupla, string, etc.)
print() | Exibe (= imprime) um objeto no console 
type() | Retorna o tipo de um objeto 

&nbsp;  

#### 1.2 Para conversão de tipos:
Funções | Finalidade 
---     | ---
bool() | Converte um valor para um tipo booleano
float() | Converte um valor para um tipo ponto flutuante
int() | Converte um valor para um tipo inteiro
list() | Converte um iterável para uma lista
str() | Converte um valor para um tipo string

&nbsp;  

#### 1.3 Funções matemáticas
Funções | Finalidade 
---     | ---
abs() | Retorna o valor absoluto de um número
max() | Retorna o valor máximo de uma sequência de números
min() | Retorna o valor mínimo de uma sequência de números
round() | Arredonda um número para um determinado número de casas decimais
sum() | Retorna a soma de uma sequência de números

&nbsp;  

#### 1.4 Para iteração e filtragem
Funções | Finalidade 
---     | ---
filter() | Filtra itens de um iterável com base em uma função
map() | Aplica uma função a todos os itens de um iterável
sorted() | Retorna uma lista ordenada a partir dos elementos de um iterável
enumerate() | Retorna  uma sequência de tuplas contendo um índice e o valor correspondente do iterável
range() | Geralmente usado em loops, gera uma sequência de números
zip() | Combina elementos de múltiplos iteráveis (listas, tuplas, etc) em tuplas

&nbsp;  

#### 1.5 Para manipulação de strings
Funções | Finalidade 
---     | ---
format() | Formata uma string
len() | Retorna o comprimento de uma string
str() | Converte um valor para uma string

&nbsp;  

### 2. Funções personalizadas 
- São criadas no código pelo usuário para resolver uma necessidade específica  
- Definidas através da palavra-chave `def` seguida pelo nome da função, (se existirem) dos parâmetros e do bloco de código desejado 

```py

def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)

calculo = fatorial(3)
print(calculo)

# Retorna: 6
```
```py

def multiplicacao(a, b):
  return a * b

# Chamando a função multiplciação
calculo = multiplicacao(4, 5)  
print(calculo)  

# Retorna: 20
```

&nbsp;  

Criar funções para cálculo de notas de um aluno, sendo que:  
- A atividade prática deve ter peso de 40%.  
- O exame final deve ter peso de 60%.  
- Deve ser informado se o aluno foi aprovado ou não na disciplina (a média da escola é 7).  

```py 

# As funções
def nota_efetiva_pratica(nota_obtida1, peso = 0.4):
  global nota_efetiva1
  nota_efetiva1 = nota_obtida1 * peso

def nota_efetiva_exame(nota_obtida2, peso = 0.6):
  global nota_efetiva2
  nota_efetiva2 = nota_obtida2 * peso

def imprime_resultado(notas_finais):
  sum = 0
  cont = 0
  for nota in notas_finais:
		sum = sum + nota
		cont = cont + 1
		print(str(cont)+'a. avaliação: Nota',nota)
		print(f'Nota final obtida: {sum:.1f}')
	if sum >= 7.0:
		print('>> Status: O aluno foi aprovado')
	else:
		print('>> Status: O aluno ficou para recuperação')

# O programa principal

# Input das notas obtidas pelo aluno
nota_obtida1 = float(input('Entre com a nota obtida na atividade prática (representa 40% da nota final): '))
nota_obtida2 = float(input('Entre com a nota obtida no exame (representa 60% da nota final): '))

# Chamando funções para cálculo das notas efetivas, de acordo com seus pesos
nota_efetiva_pratica(nota_obtida1)
nota_efetiva_exame(nota_obtida2)

# Inclusão em lista das notas obtidas
notas_finais = [nota_efetiva1, nota_efetiva2]

# Impresão do informativo das notas
print('\nDesempenho do aluno:')
imprime_resultado(notas_finais)


'''
Output 

Entre com a nota obtida na atividade prática (representa 40% da nota final): 7.5
Entre com a nota obtida no exame (representa 60% da nota final): 6.5

Desempenho do aluno:
1a. avaliação: Nota 3.0
2a. avaliação: Nota 3.9
Nota final obtida: 6.9
>> Status: O aluno ficou para recuperação
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>