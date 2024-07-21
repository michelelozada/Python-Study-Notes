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

- Podem conter itens de diferentes tipos

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
extend() | Estende uma lista adicionando todos os itens de um iterável
index() | Retorna o índice da primeira ocorrência do item especificado
insert() | Adiciona um item em uma posição especificada da lista 
pop() | Remove e retorna o item de uma lista, a partir de seu índice 
remove() | Remove da lista o item informado, em sua primeira ocorrência encontrada
reverse() | Inverte a ordem dos itens da lista 
sort() | Ordena os itens da lista de forma crescente

&nbsp;

## Aplicação de slicing em listas 

↳ Criação de sublistas a partir de uma lista
```py

numeros = [1 , 2, 3, 4, 5, 6 , 7, 8, 9, 10]

numeros_pares = numeros[1::2]
numeros_impares = numeros[::2]

print(numeros_pares)   # Saída: [2, 4, 6, 8, 10]
print(numeros_impares) # Saída: [1, 3, 5, 7, 9]
```

&nbsp;

↳ Inversão da ordem de elementos da lista 
```py

print(numeros[::-1])

# Saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

&nbsp;

## Desempacotamento (ou unpacking) de listas
Técnica para lidar com iteráveis (tuplas, listas, etc.) que permite a atribuição de valores a variáveis individuais, de forma rápida e concisa. 

↳ Desempacotamento simples
```py

nomes = ['Ana', 'Beatriz', 'Celso']

# Desempacotando a lista
a, b, c = nomes

print(a)  # Saída: Ana
print(b)  # Saída: Beatriz
print(c)  # Saída: Celso
```

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
*Adiciona um item especificado no final de uma lista*  

```py

numeros = [1, 5, 10, 15]
numeros.append(20)
print(numeros)

# Saída: [1, 5, 10, 15, 20]
```

&nbsp;

#### • Método extend()
*Estende uma lista adicionando todos os itens de um iterável*  

```py

vogais = ['a', 'e']
vogais.extend(['i','o','u'])
print(vogais)

# Saída: ['a', 'e', 'i', 'o', 'u']
```

&nbsp;

#### • Método insert()
*Adiciona um item em uma posição especificada da lista*

```py

vogais = ['a', 'e', 'o', 'u' ]
vogais.insert(2, 'i')
print(vogais)

# Saída: ['a', 'e', 'i', 'o', 'u']
```

&nbsp;

#### • Método pop()
*Remove e retorna o item de uma lista, a partir do índice fornecido como argumento. Se nenhum índice for especificado, removerá e retornará o último item da lista*

```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop(1)
print(mes_removido)

# Saída: fevereiro
```
```py

meses = ["janeiro", "fevereiro", "março"]
mes_removido = meses.pop()
print(mes_removido)

# Saída: março
```

&nbsp;

#### • Método remove()
*Remove da lista o item informado, em sua primeira ocorrência encontrada. Corresponde ao valor do elemento que foi passado como argumento.*

```py

letras = ['a', 'b', 'c', 'a']
letras.remove('a')
print(letras)

# Saída: ['b','c', 'a']
```

&nbsp;

#### • Método sort()
*Ordena os itens da lista de forma crescente, modificando a lista original. (Para o caso de desejar retornar uma nova lista com itens ordenados, use a função nativa sorted())*

```py

frutas = ['limão', 'laranja', 'mamão', 'amora']
frutas.sort()
print(frutas)

# Saída: ['amora', 'laranja', 'limão', 'mamão']
```

&nbsp;

#### • Método zip()
*Gera objeto do tipo zip que permite combinar iteráveis (listas, tuplas, etc) em pares de tuplas* 

```py
marca = ['Citröen', 'Renault', 'Peugeot']
modelo = ['C3', 'Clio', '208']

# Para visualizar o resultado, objeto zip foi convertido em lista
resultado = list(zip(marca, modelo))

print(resultado)

# Saída: [('Citröen', 'C3'), ('Renault', 'Clio'), ('Peugeot', '208')]
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>