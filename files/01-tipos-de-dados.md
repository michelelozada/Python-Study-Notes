> **Tipos de dados**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Tipos de Dados *(mini-revisão)*
```
- Em Python, os tipos de dados estão relacionados às suas classes subjacentes, i.e., cada tipo de dado 
corresponde a uma classe.   

- Os principais tipos de dados são: 
  os numéricos (int e float)
  os sequenciais (string, list, tuple, range, set)
  de mapeamento (dictionary)
  booleans (bool)
  
- O processo de conversão de um tipo de dado em outro chama-se casting.
```

&nbsp;  

## Principais Tipos de Dados *(referência rápida)* 

### • Tipos Numéricos
Nome | Classe associada | Descrição | Exemplos
---  | --- | :-- | ---
int | int | Representa números inteiros, positivos ou negativos | 15, -10
float | float | Representa números de ponto flutuante (= números decimais) | 22.7, -8.5

&nbsp;  

↳ Retorne quais são as classes dos objetos de dados apresentados abaixo:  
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
---  | --- | :-- | ---
str | str | Representa uma sequência de caracteres | "Linguagem de programação", "Python"
list | list | Representa uma sequência *mutável* de elementos | [1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']
tuple | tuple | Representa uma sequência *imutável* de elementos | (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
range | range | Representa uma sequência *imutável* de números inteiros | range(5), range(1, 10, 2)
set | set | Representa uma sequência não ordenada de itens únicos | {1, 2, 3}

&nbsp;  

↳ Retorne quais são as classes dos objetos de dados apresentados abaixo:  
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
---  | --- | :-- | ---
dictionary | dict | Representa uma coleção *mutável* de pares chave-valor | {'nome': 'James', 'sobrenome': 'Bond'}, {'a': 10, 'b': 20}

&nbsp;  

↳ Retorne qual é a classe do objeto de dado apresentado abaixo:  
```py

h = {'Nome': 'Davi', "Idade": 18, 'Profissão':'Programador'}
print(type(h))
# Saída: <class 'dict'>
```

&nbsp;  

### • Tipos de Booleans
Nome | Descrição | Exemplos
---  | :-- | ---
bool | bool | Representa um valor lógico | True ou False

&nbsp;  

↳ Retorne qual é a classe dos objetos de dados apresentados abaixo:  
```py

i1 = True
i2 = False
print(type(i1), ' - ', type(i2))
# Saída: <class 'bool'>  -  <class 'bool'>
```

&nbsp;  

## Conversão de tipos de dados (casting)  

### • Conversão para int
```py

a = int(5)
b = int(5.7)
c = int("5")

print(type(a))  # Saída: <class 'int'>
print(type(b))  # Saída: <class 'int'>
print(type(c))  # Saída: <class 'int'>
```

&nbsp;  

### • Conversão para float
```py

a = float(5)
b = float(5.7)
c = float("5")
d = float("5.7")

print(type(a)) # Saída: <class 'float'>
print(type(b)) # Saída: <class 'float'>
print(type(c)) # Saída: <class 'float'>
print(type(d)) # Saída: <class 'float'>
```

&nbsp;  

### • Conversão para string
```py

a = str(2)
b = str(3.0)

print(type(a)) # Saída: <class 'str'>
print(type(b)) # Saída: <class 'str'>

print(a + b) # 23.0
```

&nbsp;  

### • Conversão para boolean
```py

print(bool('')) # Saída: False
print(bool('abc')) # Saída: True
print(bool(0)) # Saída: False
print(bool(2)) # Saída: True
```

&nbsp;

### • Conversão de uma tupla para lista:

```py

tupla = (10, 20, 30)
lista = list(tupla) # Resultado: [10, 20, 30]
```

&nbsp;

### • Conversão de uma string para lista de carateres:
```py

string = "hola"
lista = list(string)  # Saída: ['h', 'o', 'l', 'a']
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>