> **Dicionários**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão sobre dicionários em Python
```
- Classe associada: dict

- É uma coleção de pares de chave-valor *mutável*, i.e., após a criação do dicionário, os pares 
chave-valor podem ser modificados, adicionados ou removidos  

- Na versões mais recentes do Python, os dicionários são ordenados, baseados na ordem de inserção 
dos valores 

- Os elementos de um dicionário são acessados por meio de suas chaves e podem ser iterados

- Exemplo da sintaxe básica: {'nome': 'James', 'sobrenome': 'Bond'}, {'a': 10, 'b': 20}
```

&nbsp; 

### 1 - Declaração inicial
`ficha_livro` é uma instância da classe dict  
```py

ficha_livro = {
  'Título': 'Harry Potter e a Pedra Filosofal',
  'Título original': 'Harry Potter and the Philosopher\'s Stone',
  'Autor(a)': 'Rowling, J.K.',
  'Editora': 'Rocco',
  'Páginas': '264 páginas'
}



'''
Retorna: {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas'}
'''
```

&nbsp;

### 2 - Retorno do tipo da estrutura de dados acima
```py

print(type(ficha_livro))  # <class 'dict'>
```

&nbsp;

### 3 - Número de elementos que este dicionário contém:
```py

print(len(ficha_livro),'elementos')  # 5 elementos
```

&nbsp;

### 4 - Consulta do valor associado à chave 'editora':
```py

print(ficha_livro.get('Editora'))  # Rocco

#ou
	
print(ficha_livro['Editora']) # Rocco
```

&nbsp;

### 5 - Verificação de se as chaves 'Páginas' e 'Capítulos' constam ou não neste dicionário:
```py

print('Páginas' in ficha_livro)  # True
print('Capítulos' in ficha_livro) # False
```

&nbsp;


### 6 - Atualizando o valor de uma chave
```py

ficha_livro['Autor(a)'] = 'J.K. Rowling'
```

&nbsp;

### 7 - Adição de uma nova chave e respectivo valor
```py

ficha_livro['Ano de publicação'] = 2000
print(ficha_livro)

'''
{'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000}

'''
```

&nbsp;

### 8 - Criação de um dicionário independente baseado no primeiro, seguido da alteração dos valores abaixo:
```py

ficha_livro2 = ficha_livro.copy()
ficha_livro2['Título'] = 'Harry Potter e o Prisioneiro de Azkaban'
ficha_livro2['Título original'] = 'Harry Potter and the Prisoner of Azkaban'
ficha_livro2['Páginas']= '288 páginas'
ficha_livro2['Ano de publicação'] = 2007
print(ficha_livro2)

'''
{'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban',
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007}

'''
```

&nbsp;

### 9 - Para ambas as listas, inclusão da informação de que se trata da 1ª edição dos livros.
```py

edition ={
  'Edição': '1ª ed.',
}
ficha_livro.update(edition)
ficha_livro2.update(edition)
print(ficha_livro)
print(ficha_livro2)

'''
{'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}
{'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban',
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007, 'Edição': '1ª ed.'}
'''
```

&nbsp;

### 10 - Considerando-se somente o primeiro dicionário:

### 10.1 - Retorno de uma lista com os pares chave-valor do dicionário
```py

print(ficha_livro.items())

'''
dict_items([('Título', 'Harry Potter e a Pedra Filosofal'), ('Título original', "Harry Potter and the Philosopher's
Stone"), ('Autor(a)', 'J.K. Rowling'), ('Editora', 'Rocco'), ('Páginas', '264 páginas'), ('Ano de publicação', 2000),
('Edição', '1ª ed.')])
'''
```

&nbsp;

### 10.2 - Retorno de uma lista apenas com as chaves do dicionário
```py

chaves = ficha_livro.keys()
print(chaves)

'''
dict_keys(['Título', 'Título original', 'Autor(a)', 'Editora', 'Páginas', 'Ano de publicação', 'Edição'])
'''
```

&nbsp;

### 10.3 - Retorno de uma lista apenas com os valores do dicionário
```py

valores = ficha_livro.values()
print(valores)

'''
dict_values(['Harry Potter e a Pedra Filosofal', "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 'Rocco',
'264 páginas', 2000, '1ª ed.'])
'''
```

&nbsp;

### 10.4 - Criação de um novo dicionário a partir das duas listas acima:
```py

novo_dicionario = dict(zip (chaves,valores))
print(novo_dicionario)

'''
{'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}
'''
```

&nbsp;

### 10.5 - Remoção do dicionário do valor e chave associada referente ao número de páginas
```py

novo_dicionario.pop('Páginas')
print(novo_dicionario)

'''
{'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}
'''
```

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

## Exemplos de aplicações dos métodos para manipular dicionários

### Método items()
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

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>