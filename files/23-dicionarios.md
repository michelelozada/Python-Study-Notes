> **Dicionários**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### Notas
```
- Um dicionário (dict) em Python é uma coleção desordenada de pares chave-valor.
- Permite que você armazene dados de uma maneira estruturada e facilmente acessível através das chaves.
- Portanto, útil para armazenar informações detalhadas e rotuladas.
```

&nbsp; 

### 1 - Declaração inicial
```py

ficha_livro = {
  'Título': 'Harry Potter e a Pedra Filosofal',
  'Título original': 'Harry Potter and the Philosopher\'s Stone',
  'Autor(a)': 'Rowling, J.K.',
  'Editora': 'Rocco',
  'Páginas': '264 páginas'
}

# ou

ficha_livro = {}
ficha_livro['Título'] = 'Harry Potter e a Pedra Filosofal'
ficha_livro['Título original'] = 'Harry Potter and the Philosopher\'s Stone'
ficha_livro['Autor(a)'] = 'Rowling, J.K.'
ficha_livro['Editora'] = 'Rocco'
ficha_livro['Páginas'] = '264 páginas'

print(ficha_livro)


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

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>