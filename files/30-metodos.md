> **Métodos (referência rápida)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;

&nbsp;  
## Métodos para manipular e verificar strings em Python

### Para verificação de conteúdo de strings:
Método | Função
---    | ---
str.isalnum() | Verifica se todos os caracteres da string são letras ou dígitos
str.isalpha() | Verifica se todos os caracteres da string são letras e se string não está vazia
str.isdigit() | Verifica se todos os caracteres da string são dígitos
str.islower() | Verifica se todos os caracteres da string estão em minúsculas
str.isspace() | Verifica se todos os caracteres da string são espaços em branco
str.isupper() | Verifica se todos os caracteres da string estão em maiúsculas

&nbsp;  

### Para manipulação de conteúdo:
Método | Função
---    | ---
str.capitalize() | Converte o 1º caractere de uma string para maiúscula e demais para minúsculas
str.lower() | Converte os caracteres de uma string para minúsculas
str.replace(old, new) | Substitui a ocorrência de uma substring por outra ali informada
str.split(separator) | Divide a string em uma lista de substrings usando o separador informado
str.strip() | Remove espaços em branco do início e do fim da string
str.title() | Converte o 1º caractere de cada palavra para maiúscula e demais para minúsculas
str.upper() | Converte todos os caracteres da string para maiúsculas

&nbsp;  

### Para pesquisa de conteúdo:
Método | Função
---    | ---
str.endswith(suffix) | Verifica se a string termina com o prefixo informado  
str.find(sub) | Retorna o índice da 1ª ocorrência da substring informada ou -1 se não for encontrada
str.index(sub) | Mesma função do método `find()`, mas retorna erro ValueError se a substring não for encontrada
str.startswith(prefix) | Verifica se a string começa com a substring informada

&nbsp;  

### Outros:
Método | Função
---    | ---
count() | Retorna o número de ocorrências da substring informada 
join() | Concatena elementos 
lstrip() | Remove espaços em branco do início de uma string 
rstrip() | Remove espaços em branco do final de uma string 

&nbsp;  

### Métodos para manipular listas em Python
Método | Função
---    | ---
append(elemento) | Adiciona um item ao final de uma lista
clear() | Remove todos os itens da lista 
count(elemento) | Retorna o número de ocorrências na lista do item especificado  
index(elemento) | Retorna o índice da primeira ocorrência do item informado
insert(posição, elemento) | Adiciona um item em uma posição especificada da lista 
pop([indice]) | Remove e retorna o item de uma lista (segundo o índice informado)
remove(elemento) | Remove da lista a primeira ocorrência do item informado 
reverse() | Inverte a ordem dos itens na lista 
sort() | Ordena os itens da lista de forma crescente

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
* Informar o argumento index é opcional  
* Se nenhum índice for especificado, retorna o último item da lista  
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