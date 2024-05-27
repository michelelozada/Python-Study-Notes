> **Tipos de dados**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão dos principais tipos de dados 

### Tipos Numéricos
Nome | Descrição | Exemplos
---  | --- | ---
int | Números inteiros, positivos ou negativos, sem casas decimais | 15, -10
float | Números de ponto flutuante (= números com casas decimais) | 22.7, -8.5

Retorne quais os tipos de dados das variáveis apresentadas abaixo:  
```py

a = 7
print(a, type(a))
# Retorna: 7 <class 'int'>


b = 10.5
print(b, type(b))
# Retorna: 10.5 <class 'float'>
```

&nbsp; 

### Tipos Sequenciais
Nome | Descrição | Exemplos
---  | --- | ---
str | Cadeias de caracteres que armazenam texto | "Linguagem de programação", "Python"
list | Coleções ordenadas e *mutáveis* de elementos | [1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']
tuple | Coleções ordenadas e *imutáveis* de elementos | (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
range |  Intervalo/sequência *imutável* de números inteiros, geralmente usada em loops | range(5), range(1, 3, 6)

Retorne quais os tipos de dados das variáveis apresentadas abaixo:  
```py

d = 'Tipos de variáveis utilizadas em Python!'
print(d, type(d))
# Retorna: Tipos de variáveis utilizadas em Python! <class 'str'>


f = ['a', 2, 'c', 4, 5]
print(f, type(f))

# Retorna: ['a', 2, 'c', 4, 5] <class 'list'>


g = ('Paraná', 'Santa Catarina','Rio Grande do Sul')
print(g, type(g))

# Retorna: ('Paraná', 'Santa Catarina', 'Rio Grande do Sul') <class 'tuple'>
```

&nbsp;  

### Tipos de Mapeamento
Nome | Descrição | Exemplos
---  | --- | ---
dict | Coleções de pares chave-valor, ordenadas e *mutáveis* | {'nome': 'James', 'sobrenome': 'Bond'}, {'a': 10, 'b': 20}

Retorne qual o tipo de dados da variável apresentada abaixo:  
```py

h = {'Nome': 'Davi', "Idade": 18, 'Profissão':'Programador'}
print(h, type(h))

# Retorna: {'Nome': 'Davi', 'Idade': 18, 'Profissão': 'Programador'} <class 'dict'>
```

&nbsp;  

### Tipos de Booleans
Nome | Descrição | Exemplos
---  | --- | ---
bool | Usados para representar a verdade lógica | True, False

Retorne quais os tipos de dados das variáveis apresentadas abaixo:  
```py

e1 = True
e2 = False
print(e1, type(e1), ' - ', e2, type(e2))

# Retorna: True <class 'bool'>  -  False <class 'bool'>
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>