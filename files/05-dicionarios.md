> **Dicionários**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Dicionários em Python *(mini-revisão)*
```
- Classe associada: dict

- É uma coleção de pares de chave-valor *mutável*, i.e., após a criação do dicionário, os pares 
chave-valor podem ser modificados, adicionados ou removidos  

- Na versões mais recentes do Python, os dicionários são ordenados, baseados na ordem de inserção 
dos valores 

- Item em um dicionário é a combinação de uma chave com o seu valor correspondente. 
  Chave: É o identificador único associado a um valor dentro do dicionário. Cada chave em um dicionário
  deve ser única
  Valor: É o dado armazenado no dicionário que está associado a uma chave específica

- Itens de um dicionário são acessados por meio de suas chaves e podem ser iterados

- Exemplo da sintaxe básica: 

  dicionario = {
    'chave1': 'valor1',  # item 1
    'chave2': 'valor2',  # item 2
    'chave3': 'valor3'   # item 3
  }
```

&nbsp;  

## Métodos da classe dict *(referência rápida)* 

Método | Função
---    | :--
clear() | Remove todos os itens do dicionário
copy() | Retorna uma cópia superficial do dicionário
get() | Retorna o valor da chave especificada ou um valor padrão se a chave não for encontrada
items() | Retorna uma visão dinâmica dos pares chave-valor no dicionário
keys() | Retorna uma visão das chaves atuais no dicionário  
pop() | Remove um item de um dicionário de acordo com a chave especificada e retorna o valor associado a essa chave
popitem() | Remove e retorna um par chave-valor do dicionário. Se o dicionário estiver vazio, lança um KeyError
setdefault() | Retorna o valor para a chave especificada; se a chave não estiver no dicionário, adiciona a chave com o valor padrão
update() | Atualiza o dicionário com os pares chave-valor de outro dicionário, sobrescrevendo as chaves existentes
values() | Retorna uma nova lista dos valores do dicionário

&nbsp;

## Testando se um dicionário possui elementos ou se está vazio
*Em Python, um dicionário vazio é considerado um valor falso (False) num contexto booleano. Portanto, quando se usa um dicionário em uma condição if, é verificado se o dicionário está vazio ou não, sendo que um dicionário com elementos é considerado True e um dicionário vazio é considerado False. 
```py

dici_nomes = {'a': 'Ana', 'b': 'Bia', 'c': 'Celso'}

if dici_nomes:
  print("O dicionário de nomes não está vazio.")
else:
  print("O dicionário de nomes está vazio.")
  
# Saída: O dicionário de nomes não está vazio.
```
```py
dici_idades = {}

if dici_idades:
  print("O dicionário de idades não está vazio.")
else:
  print("O dicionário de idades está vazio.")

# Saída: O dicionário de idades está vazio.
```

&nbsp;

## Verificando se uma determinada chave está presente em um dicionário 
Feito através do operador `in`, que verifica se a chave (key) está em um dicionário e retorna um valor booleano a respeito dela ter sido encontrada (ou não).

```py


dici_nomes = {'a': 'Ana', 'b': 'Bia', 'c': 'Celso'}

print('e' in dici_nomes)
# Saída: False

print('c' in dici_nomes)
# Saída: True
```

&nbsp;

## Verificando se um determinado valor está presente em um dicionário 
Feito através do operador `in` em conjunto com o método `values()`, que verifica se um valor está associado a alguma chave do dicionário, retornando um valor booleano.

```py

dici_nomes = {'a': 'Ana', 'b': 'Bia', 'c': 'Celso'}

print('Celso' in dici_nomes.values())
# Saída: True

print('Dani' in dici_nomes.values())
# Saída: False
```

&nbsp;

## Exemplos de aplicações dos métodos para manipular dicionários

#### Método get()
*Usado para acessar o valor associado a uma chave específica. Se a chave não existir, o método retorna um valor padrão definido no código (ou None se não for especificado).*  

```py

frutas = {
  'a': 'maçã',
  'b': 'banana',
  'c': 'laranja',
  'd': 'morango'
}

print(frutas.get('c', 0))
# Saída: laranja

print(frutas.get('e', 0))
# Saída: 0

print(frutas.get('f'))
# Saída: None
```

&nbsp;

#### Método items()
*Este método retorna um objeto do tipo dict_items, que é uma visão dinâmica e iterável dos pares chave-valor do dicionário original, permitindo acessar e iterar sobre eles.*  

```py
tarefas = {
  '1': 'Lavar a louça',
  '2': 'Varrer a casa',
  '3': 'Fazer o almoço'
}

items_de_tarefas = tarefas.items()
print(type(items_de_tarefas))

# Saída: <class 'dict_items'>


for chave, valor in tarefas.items():
	print(f"{chave}ª tarefa: {valor}")
	
'''  
Retorna: 
1ª tarefa: Lavar a louça
2ª tarefa: Varrer a casa
3ª tarefa: Fazer o almoço
'''
```

&nbsp;

#### Método keys()
*Retorna uma visão das chaves atuais no dicionário. Esta visão pode ser iterada diretamente ou convertida em uma lista usando a função list(), se a necessidade for uma lista estática das chaves.*

```py

frutas = {
  'maçã': 1,
  'banana': 2,
  'laranja': 3,
  'morango': 4
}

print(list(frutas.keys()))

# Saída: ['maçã', 'banana', 'laranja', 'morango']
```

&nbsp;

#### Método pop()
*Remove um item de um dicionário de acordo com a chave especificada e retorna o valor associado a essa chave*  

```py

frutas = {
    'maçã': 1,
    'banana': 2,
    'laranja': 3,
    'morango': 4
}

fruta_excluida = frutas.pop('banana')
print(fruta_excluida)  
# Saída: 2

print(frutas)
# Saída: {'maçã': 1, 'laranja': 3, 'morango': 4}
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>