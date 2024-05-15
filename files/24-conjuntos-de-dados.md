> **Conjuntos de dados (sets)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### 1. Declarando um set
```py

conjunto = set()
conjunto = set([1,2,3,6,5])
print(conjunto) # Retorna: {1, 2, 3, 5, 6}

# ou

conjunto = {1,2,3,6,5}
print(conjunto) # {1, 2, 3, 5, 6}
```

&nbsp;  

### 2. Um set é uma coleção de elementos únicos, repare: 
```py

conjunto2 = {1,2,2,2,1}
print(conjunto2) # {1, 2}
```

&nbsp;  

### 3. Num set a ordem dos elementos é irrelevante:
```py

print({1,2,3} == {2,1,3}) # True
print ({3,3,2,2,1} == {1,2,3}) # True
```

&nbsp;  

### 4. Determinando o tamanho de um set:
```py

setNomes = {'Ana','Bárbara','Luisa','Antônia','Érica','Márcia'}
print(len(setNomes)) #6
```

&nbsp;  

### 5. Verificando se um elemento consta em um set:
```py

print('Ana' in setNomes) # True
print('Larissa' in setNomes) # False
```

&nbsp;  

### 6. Adicionando elementos a um set:
```py

set1 = {'a','b','c'}
set1.add('d') # para adição de apenas um elemento
print(set1) # {'a', 'b', 'c', 'd'}

set1.update(['e','f','g']) # para adição de mais elementos
print(set1) # {'e', 'f', 'a', 'g', 'b', 'c','d'}
```

&nbsp;  

### 7. Excluindo elementos de um set
```py

set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.remove('c') # definindo o elemento a ser excluido. Necessário que elemento pertença ao set para evitar erro.
print(set) # {'f', 'e', 'a', 'd', 'b'}

# ou

set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.discard('r') # fará o mesmo que remove(), mas sem gerar erro em caso de elemento fora do set
print(set) # {'a', 'c', 'f', 'e', 'd', 'b'}  -> repare que não houve alteração (nem exceção!)

#ou

set= {'a', 'b', 'c', 'd', 'e', 'f'}
excluido = set.pop() # sem definir o elemento a ser excluido
print(excluido) # a
print(set) # {'c', 'b', 'f', 'd', 'e'}

# ou

set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.clear() # exclusão de todos os elementos
print(set) # set()
```

&nbsp;  

### 8. Convertendo uma lista em um conjunto/set
```py

nomes = ['Huguinho','Luisinho','Zezinho']
listaNomes = set(nomes)
print(listaNomes) # {'Huguinho', 'Zezinho', 'Luisinho'}
```

&nbsp;  

### 9. Convertendo um conjunto em um lista
```py

nomes = {'Margarida', 'Minnie','Mickey'}
lista = list(nomes)
print(lista) # ['Mickey', 'Minnie', 'Margarida']
```

&nbsp;  

### 10. Convertendo um conjunto em uma tupla
```py

novoSet = {'Luciano','Paulo','Marcos','Antônio','Eduardo'}
tupla = tuple(novoSet)
print(tupla)  # ('Marcos', 'Antônio', 'Eduardo', 'Paulo', 'Luciano')
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>