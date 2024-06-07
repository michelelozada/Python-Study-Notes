> **Tipos de dados**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão dos principais tipos de dados 
```
Em Python, os tipos de dados estão relacionados às suas classes subjacentes, i.e., cada tipo de dado corresponde a uma classe.   
```

&nbsp;  

### • Tipos Numéricos
Nome | Classe associada | Descrição | Exemplos
---  | --- | --- | ---
int | int | Representa números inteiros, positivos ou negativos | 15, -10
float | float | Representa números de ponto flutuante (= números decimais) | 22.7, -8.5

&nbsp;  

Retorne quais são as classes dos objetos de dados apresentados abaixo:  
```py

a = 7
print(type(a))
# Saída: <class 'int'>


b = 10.5
print(type(b))
# Saída: <class 'float'>
```

&nbsp; 

### • Tipos Sequenciais
Nome | Classe associada | Descrição | Exemplos
---  | --- | --- | ---
str | str | Representa uma sequência de caracteres | "Linguagem de programação", "Python"
list | list | Representa uma sequência *mutável* de elementos | [1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']
tuple | tuple | Representa uma sequência *imutável* de elementos | (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
range | range | Representa uma sequência *imutável* de números inteiros | range(5), range(1, 10, 2)
set | set | Representa uma sequência não ordenada de itens únicos | {1, 2, 3}

&nbsp;  

Retorne quais são as classes dos objetos de dados apresentados abaixo:  
```py

c = 'Tipos de variáveis utilizadas em Python!'
print(type(c))
# Saída: <class 'str'>


d = ['a', 2, 'c', 4, 5]
print(type(d))
# Saída: <class 'list'>


e = ('Paraná', 'Santa Catarina','Rio Grande do Sul')
print(type(e))
# Saída: <class 'tuple'>

f = range(1, 10, 2)
print(type(f))
# Saída: <class 'range'>

g = {1, 2, 3}
print(type(g))
# Saída: <class 'set'>
```

&nbsp;  

### • Tipos de Mapeamento
Nome | Classe associada |  Descrição | Exemplos
---  | --- | --- | ---
dictionary | dict | Representa uma coleção *mutável* de pares chave-valor | {'nome': 'James', 'sobrenome': 'Bond'}, {'a': 10, 'b': 20}

&nbsp;  

Retorne quais é a classe do objeto de dado apresentado abaixo:  
```py

h = {'Nome': 'Davi', "Idade": 18, 'Profissão':'Programador'}
print(type(h))
# Saída: <class 'dict'>
```

&nbsp;  

### • Tipos de Booleans
Nome | Descrição | Exemplos
---  | --- | ---
bool | bool | Representa um valor lógico | True ou False

&nbsp;  

Retorne qual é a classe dos objetos de dados apresentados abaixo:  
```py

i1 = True
i2 = False
print(type(i1), ' - ', type(i2))
# Saída: <class 'bool'>  -  <class 'bool'>
```

## Conversão de tipos de dados (casting)  

&nbsp;  

### • Conversão para int
```py

a = int(5)
b = int(5.7)
c = int("5")

print(a,type(a))  # Retorna: 5 <class 'int'>
print(b,type(b))  # 5 <class 'int'>
print(c,type(c))  # 5 <class 'int'>
print(a + b)  # 10
print(a + c)  # 10
```

&nbsp;  

### • Conversão para float
```py

a = float(5)
b = float(5.7)
c = float("5")
d = float("5.7")

print(a,type(a)) # Retorna: 5.0 <class 'float'>
print(b,type(b)) # 5.7 <class 'float'>
print(c,type(c)) # 5.0 <class 'float'>
print(d,type(d)) # 5.7 <class 'float'>
print(a + b)  # 10.7
print(a + c)  # 10.0
```

&nbsp;  

### • Conversão para string
```py

a = str("exemplo")
b = str(2)
c = str(3.0)

print(a,type(a)) # Retorna: exemplo <class 'str'>
print(b,type(b)) # 2 <class 'str'>
print(c,type(c)) # 3.0 <class 'str'>
print(b + c) # 23.0
```

&nbsp;  

### • Conversão para boolean
```py

print(bool(''))   # False
print(bool('abc')) # True
print(bool(0)) # False
print(bool(2)) # True
```
&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>