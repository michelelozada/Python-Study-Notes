> **Set (conjunto de dados)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Sets em Python *(mini-revisão)*
```
- Classe associada: set

- É uma estrutura de dados de sequência em que *apenas itens únicos são armazenados*

- Isso quer dizer que ao tentar adicionar um item que já presente no set, este será ignorado

- É uma sequência não ordenada, pois não mantém uma ordem específica dos elementos 

- É mutável, i.e, permite a adição, remoção ou modificação de elementos dentro da coleção

- Exemplo da sintaxe básica: {1, 2, 3, 6, 5}
```

&nbsp;

## Métodos da classe `set` *(referência rápida)* 

Método | Função
---    | :--
add()  | Adiciona um item ao set; se o elemento já estiver ali, o set não será modificado
clear() | Remove todos os itens do conjunto
discard() | Similar à função remove(); mas se o item não estiver no set, não gera erro
pop() | Remove e retorna um item aleatório do set; se o set estiver vazio, gera erro
update() | Adiciona elementos de um iterável (outro set, lista ou tupla) no set em questão
remove() | Remove o item especificado do set; se o item não estiver no set, gera erro

&nbsp;

## Mais sobre sets

↳ Declarando um set:
```py

conjunto = {1, 2, 3, 6, 5}
```
*\* A variável conjunto é uma instância da classe set em Python.* 

&nbsp;

↳ Repare que um set é uma coleção de elementos únicos: 
```py

conjunto = {1, 2, 2, 2, 1}
print(conjunto) 

Saída: {1, 2}
```

&nbsp;

↳ A ordem dos elementos num set é irrelevante:
```py

print({1, 2, 3} == {2, 1, 3})
# Saída: True

print ({3, 3, 2, 2, 1} == {1, 2, 3}) 
# Saída: True
```

&nbsp;

## Desempacotamento (ou unpacking) de sets
Técnica para lidar com iteráveis (sets, tuplas, listas, etc.) que permite a atribuição de valores a variáveis individuais, de forma rápida e concisa. Como os sets não são ordenados, as variáveis podem assumir qualquer valor dos elementos do conjunto. 

&nbsp;

↳ Desempacotamento simples
```py

idades = {8, 9, 10}

# Desempacotando o set
a, b, c = idades

print(a)  # Nesta saída: 10
print(b)  # Nesta saída: 11
print(c)  # Nesta saída: 12
```

&nbsp;

## Testando se um set possui elementos ou se está vazio
*Em Python, um set vazio é considerado um valor falso (False) num contexto booleano. Portanto, quando se usa um set em uma condição if, é verificado se o set está vazio ou não, sendo que um set com elementos é considerado True e um set vazio é considerado False. 

```py
set_numeros = {1, 2, 3, 4, 5}

if set_numeros:
  print("O set de números não está vazio.")
else:
  print("O set de números está vazio.")
  
# Saída: O set de números não está vazio.  
```
```py
set_letras = {}

if set_letras:
  print("O set de letras não está vazio.")
else:
  print("O set de letras está vazio.")
  
# Saída: O set de letras está vazio.  
```  

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>