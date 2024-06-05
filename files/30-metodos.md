> **Métodos (referência rápida)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;

&nbsp;  
## Métodos da Classe `str` (String)

### Para verificação de conteúdo de strings:
Método | Função
---    | ---
isalnum() | Verifica se todos os caracteres da string são letras ou dígitos
isalpha() | Verifica se todos os caracteres da string são letras e se string não está vazia
isdigit() | Verifica se todos os caracteres da string são dígitos
islower() | Verifica se todos os caracteres da string estão em minúsculas
isspace() | Verifica se todos os caracteres da string são espaços em branco
isupper() | Verifica se todos os caracteres da string estão em maiúsculas

&nbsp;  

### Para manipulação de conteúdo/formatação:
Método | Função
---    | ---
capitalize() | Converte o 1º caractere de uma string para maiúscula e demais para minúsculas
format() | Formata uma string
join() | Concatena elementos 
lower() | Converte os caracteres de uma string para minúsculas
lstrip() | Remove espaços em branco do início de uma string 
replace(old, new) | Substitui a ocorrência de uma substring por outra ali informada
rstrip() | Remove espaços em branco do final de uma string 
split(separator) | Divide a string em uma lista de substrings usando o separador informado
strip() | Remove espaços em branco (ou outros caracteres especificados) do início e do fim da string 
title() | Converte o 1º caractere de cada palavra para maiúscula e demais para minúsculas
upper() | Converte todos os caracteres da string para maiúsculas

&nbsp;  

### Para pesquisa de conteúdo:
Método | Função
---    | ---
count() | Retorna o número de ocorrências da substring informada 
endswith(suffix) | Verifica se a string termina com o prefixo informado  
find(sub) | Retorna o índice da 1ª ocorrência da substring informada ou -1 se não for encontrada
index(sub) | Mesma função do método `find()`, mas retorna erro ValueError se a substring não for encontrada
startswith(prefix) | Verifica se a string começa com a substring informada

&nbsp;  

### Métodos da Classe `list` (Lista)

Método | Função
---    | ---
append(elemento) | Adiciona um item ao final de uma lista
copy() | 
clear() | Remove todos os itens da lista 
count(elemento) | Retorna o número de ocorrências na lista do item especificado  
extend() | 
index(elemento) | Retorna o índice da primeira ocorrência do item informado
insert(posição, elemento) | Adiciona um item em uma posição especificada da lista 
pop([indice]) | Remove e retorna o item de uma lista (segundo o índice informado)
remove(elemento) | Remove da lista a primeira ocorrência do item informado 
reverse() | Inverte a ordem dos itens na lista 
sort() | Ordena os itens da lista de forma crescente

&nbsp;

### Métodos da Classe `dict` (Dicionário)

Método | Função
---    | ---
clear() |
get() |
items() |
keys() |
pop() | 
popitem() | 
setdefault() |
update() | 
values() |

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