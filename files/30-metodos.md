> **Métodos (referência rápida)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Métodos para manipular objetos do tipo string em Python
Método | Função
---    | ---
capitalize() | Converte o 1º caractere de uma string para maiúscula e demais para minúsculas
count() | Retorna o número de ocorrências da substring informada 
endswith() | Retorna True se a string terminar com o prefixo informado 
find() | Retorna o índice de da primeira ocorrência de uma substring informada 
index() | Mesma função do método `find()`, mas retorna erro ValueError se a substring não for encontrada
join() | Concatena elementos 
lower() | Converte os caracteres de uma string para minúsculas
lstrip() | Remove espaços em branco do início de uma string 
replace() | Substitui a ocorrência de uma substring por outra ali informada
rstrip() | Remove espaços em branco do final de uma string 
startswith() | Retorna True se a string começar com o prefixo informado 
split() | Divide uma string em substrings, utilizando um separado informado 
strip() | Remove espaços em branco do início e do final de uma string 
title() | Converte o 1º caractere de cada palavra para maiúscula e demais para minúsculas
upper() | Converte os caracteres de uma string para maiúsculas 

&nbsp;  

### Métodos para manipular listas em Python
Método | Função
---    | ---
append(elemento) | Adiciona um elemento ao final de uma lista
clear() | Remove todos os elementos da lista 
count(elemento) | Retorna o número de ocorrências do elemento especificado na lista 
index(elemento) | Retorna o índice da primeira ocorrência do elemento informado
insert(posição, elemento) | Insere um elemento em uma posição determinada da lista 
pop([indice]) | Remove e retorna o elemento da lista, na posição informada
remove(elemento) | Remove a primeira ocorrência do elemento informado da lista 
reverse() | Inverte a ordem dos elementos na lista 
sort() | Ordena os elementos da lista de forma crescente

&nbsp;

### Exemplos de aplicações dos métodos para manipular strings

### Método lower()
```py

string = "Hello World"
print(string.lower())  

# Retorna: "hello world"
```

&nbsp;

### Exemplos de aplicações dos métodos para manipular listas em Python 

### Método append()
```py

numeros = [1, 5, 10, 15]
numeros.append(20)
print(numeros)

# Retorna: [1, 5, 10, 15, 20]
```

&nbsp;

### Método pop()
```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop()
print(mes_removido)

# Retorna: março
```
```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop(1)
print(mes_removido)

# Retorna: fevereiro
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>