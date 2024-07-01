> **Listas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Listas em Python *(mini-revisão)*
```
- Classe associada: list

- Cada item dentro da lista é chamado de elemento (ou mesmo de item) 

- É uma estrutura de dados de sequência mutável, i.e., após a criação da lista, elementos podem ser 
modificados, adicionados ou removidos dali 

- Listas são ordenadas, i.e., sua ordem é baseada na sequência em que os elementos foram ali inseridos 

- Seus elementos são acessados pela posição/por seus índices na lista

- As listas não são limitadas por tipos: podem conter itens do mesmo tipo ou de tipos diferentes 

- Exemplo da sintaxe básica: [1, 2, 3, 4], ['a', 'e', 'i', 'o', 'u']
```

&nbsp; 

## Métodos da classe `list` *(referência rápida)* 

Método | Função
---    | :--
append() | Adiciona um item especificado no final de uma lista
copy() | Retorna uma cópia da lista
clear() | Remove todos os itens da lista 
count() | Retorna o número de ocorrências na lista do item especificado  
extend() | Estende a lista adicionando todos os itens de um iterável
index() | Retorna o índice da primeira ocorrência do item especificado
insert() | Adiciona um item em uma posição especificada da lista 
pop() | Remove e retorna o item de uma lista (o último ou o do índice informado)
remove() | Remove da lista a primeira ocorrência do item informado 
reverse() | Inverte a ordem dos itens da lista 
sort() | Ordena os itens da lista de forma crescente

&nbsp;

## Testando se uma lista possui elementos ou se está vazia
*Em Python, uma lista vazia é considerada um valor falso (False) num contexto booleano. Portanto, quando se usa uma lista em uma condição if, é verificado se a lista está vazia ou não, sendo que uma lista com elementos é considerada True e uma lista vazia é considerada False.*

```py

cesta_frutas = ['maçã', 'mamão', 'laranja']

if cesta_frutas:
  print('Há frutas em casa')
else:
  print('Ir na feira comprar frutas!')
  
# Saída: Há frutas em casa
```
```py

cesta_verduras = []

if cesta_verduras:
  print('Há verduras em casa')
else:
  print('Ir na feira comprar verduras!')
  
# Saída: Ir na feira comprar verduras!    
```

&nbsp;   

## Exemplos de aplicações dos métodos para manipular listas em Python 

#### • Método append()
```py

numeros = [1, 5, 10, 15]
numeros.append(20)
print(numeros)

# Saída: [1, 5, 10, 15, 20]
```

&nbsp;

#### • Método pop()
*\*Informar o argumento index é opcional. Se nenhum índice for especificado, retornará o último item da lista*

```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop()
print(mes_removido)

# Saída: março
```
```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop(1)
print(mes_removido)

# Saída: fevereiro
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>