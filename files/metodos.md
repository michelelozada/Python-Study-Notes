> **Métodos (referência rápida)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;

&nbsp;  
## Métodos da Classe `str` (String)

#### Para verificação de conteúdo de strings:
Método | Função
---    | ---
isalnum() | Retorna True se todos os caracteres da string forem letras ou dígitos
isalpha() | Retorna True se todos os caracteres da string forem letras e se string não está vazia
isdigit() | Retorna True se todos os caracteres da string forem dígitos
islower() | Retorna True se todos os caracteres da string estiverem em minúsculas
isspace() | Retorna True se todos os caracteres da string forem espaços em branco
isupper() | Retorna True se todos os caracteres da string estiverem em maiúsculas

&nbsp;  

#### Para manipulação de conteúdo/formatação:
Método | Função
---    | ---
capitalize() | Retorna uma cópia da string em minúsculas
format() | Formata uma string
join() | Junta os elementos de um iterável em uma string única, usando a string original como separador
lower() | Converte os caracteres de uma string para minúsculas
lstrip() | Remove espaços em branco do início de uma string 
replace(old, new) | Substitui a ocorrência da substring antiga por outra ali informada
rstrip() | Remove espaços em branco do final de uma string 
split() | Divide a string em uma lista de substrings usando o separador informado
strip() | Remove espaços em branco (ou outros caracteres especificados) do início e do fim da string 
title() | Converte o 1º caractere de cada palavra para maiúscula e demais para minúsculas
upper() | Retorna uma cópia da string em maiúsculas

&nbsp;  

#### Para pesquisa de conteúdo:
Método | Função
---    | ---
count() | Retorna o número de ocorrências da substring informada 
endswith() | Retorna True se a string termina com o sufixo especificado
find() | Retorna o índice da 1ª ocorrência da substring informada ou -1 se não for encontrada
index() | Mesma função do método `find()`, mas retorna erro ValueError se a substring não for encontrada
startswith(prefix) | Retorna True se a string começa com o prefixo especificado

&nbsp;  

## Métodos da Classe `list` (Lista)

Método | Função
---    | ---
append() | Adiciona um item ao final de uma lista
copy() | Retorna uma cópia da lista
clear() | Remove todos os itens da lista 
count() | Retorna o número de ocorrências na lista do item especificado  
extend() | Estende a lista adicionando todos os itens de um iterável
index() | Retorna o índice da primeira ocorrência do item informado
insert() | Adiciona um item em uma posição especificada da lista 
pop() | Remove e retorna o item de uma lista (segundo o índice informado)
remove(elemento) | Remove da lista a primeira ocorrência do item informado 
reverse() | Inverte a ordem dos itens na lista 
sort() | Ordena os itens da lista de forma crescente

&nbsp;

## Métodos da Classe `dict` (Dicionário)

Método | Função
---    | ---
clear() | Remove todos os itens do dicionário
copy() | Retorna uma cópia superficial do dicionário
get() | Retorna o valor de chave especificada ou o valor padrão se a chave não for encontrada
items() | Retorna uma nova lista dos pares chave-valor no dicionário
keys() | Retorna uma nova lista das chaves do dicionário
pop() |  Remove e retorna o valor para a chave especificada. Se a chave não estiver no dicionário, retorna o valor padrão
popitem() | Remove e retorna um par chave-valor do dicionário. Se o dicionário estiver vazio, lança um KeyError
setdefault() | Retorna o valor para a chave especificada; se a chave não estiver no dicionário, adiciona a chave com o valor padrão
update() | Atualiza o dicionário com os pares chave-valor de outro dicionário, sobrescrevendo as chaves existentes
values() | Retorna uma nova lista dos valores do dicionário

&nbsp;

## Exemplos de aplicações dos métodos acima para manipular strings

#### Método lower()
```py

string = "Hello World"
print(string.lower())  

# Retorna: "hello world"
```

&nbsp;

## Exemplos de aplicações dos métodos para manipular listas em Python 

#### Método append()
```py

numeros = [1, 5, 10, 15]
numeros.append(20)
print(numeros)

# Retorna: [1, 5, 10, 15, 20]
```

&nbsp;

#### Método pop()
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

## Exemplos de aplicações dos métodos para manipular dicionários

#### Método items()
```py

aluno = {
    'nome': 'Enzo',
    'idade': 18,
    'cidade': 'Curitiba'
}

for chave, valor in aluno.items():
	print(f"Chave: {chave}, Valor: {valor}")
	
# Retorna: 
Chave: nome, Valor: Enzo
Chave: idade, Valor: 18
Chave: cidade, Valor: Curitiba
```



<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>