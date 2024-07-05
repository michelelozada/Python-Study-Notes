'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> > Acessando valores e fazendo manipulações em dicionários
'''


# 1. Declaração inicial
ficha_livro = {
  'Título': 'Harry Potter e a Pedra Filosofal',
  'Título original': 'Harry Potter and the Philosopher\'s Stone',
  'Autor(a)': 'Rowling, J.K.',
  'Editora': 'Rocco',
  'Páginas': '264'
}


# 2. Retornar o tipo da estrutura de dados acima
print(type(ficha_livro))  # <class 'dict'>

```
Saída: 
<class 'dict'>
```


# 3. Retornar o número de elementos que este dicionário contém
print(len(ficha_livro))  

```
Saída: 
5
```


# 4. Retornar qual o valor associado à chave 'editora'
print(ficha_livro.get('Editora'))

# Ou alternativamente:
	
print(ficha_livro['Editora']) 

```
Saída: 
Rocco
```


# 5. Verificar se as chaves 'Páginas' e 'Capítulos' constam neste dicionário
print('Páginas' in ficha_livro)  # Saída: True
print('Capítulos' in ficha_livro) # Saída: False


# 6. Verificar se os valores '264' e 'Companhia das Letras' estão associados a alguma chave deste dicionário
print('264' in ficha_livro.values())  # Saída: True
print('Companhia das Letras' in ficha_livro.values())  # Saída: False


# 7. Atualizar o valor da chave autor para J.K. Rowling
ficha_livro['Autor(a)'] = 'J.K. Rowling'


# 8. Adicionar uma chave Ano Publicação e atribuir a ela o valor 2000:
ficha_livro['Ano de publicação'] = '2000'


# 9. Criar um dicionário independente, baseado no primeiro e seguido da alteração dos valores abaixo:
'''
Título: Harry Potter e o Prisioneiro de Azkaban
Título original: Harry Potter and the Prisoner of Azkaban
Páginas: 288
Ano de publicação: 2007
'''

ficha_livro2 = ficha_livro.copy()
ficha_livro2['Título'] = 'Harry Potter e o Prisioneiro de Azkaban'
ficha_livro2['Título original'] = 'Harry Potter and the Prisoner of Azkaban'
ficha_livro2['Páginas'] = '288'
ficha_livro2['Ano de publicação'] = '2007'
print(ficha_livro2)

'''
Saída: 
{
  'Título': 'Harry Potter e o Prisioneiro de Azkaban',
  'Título original': 'Harry Potter and the Prisoner of Azkaban',
  'Autor(a)': 'J.K. Rowling',
  'Editora': 'Rocco', 
  'Páginas': '288', 
  'Ano de publicação': '2007'
}

'''

# 10. Para ambas as listas, incluir a informação de que se trata da 1ª edição dos livros
edition = {
  'Edição': '1ª ed.',
}
ficha_livro.update(edition)
ficha_livro2.update(edition)
print(ficha_livro)
print(ficha_livro2)

'''
Saída:
{
  'Título': 'Harry Potter e a Pedra Filosofal', 
  'Título original': "Harry Potter and the Philosopher's Stone", 
  'Autor(a)': 'J.K. Rowling', 
  'Editora': 'Rocco', 
  'Páginas': '264', 
  'Ano de publicação': '2000', 
  'Edição': '1ª ed.'
}
{
  'Título': 'Harry Potter e o Prisioneiro de Azkaban', 
  'Título original': 'Harry Potter and the Prisoner of Azkaban', 
  'Autor(a)': 'J.K. Rowling', 
  'Editora': 'Rocco', 
  'Páginas': '288', 
  'Ano de publicação': '2007', 
  'Edição': '1ª ed.'
}
'''


# 11. Do primeiro dicionário, retornar uma lista com seus pares chave-valor
print(list(ficha_livro.items()))

'''
Saída:
[
  ('Título', 'Harry Potter e a Pedra Filosofal'), 
  ('Título original', "Harry Potter and the Philosopher's Stone"), 
  ('Autor(a)', 'J.K. Rowling'), ('Editora', 'Rocco'), 
  ('Páginas', '264'), 
  ('Ano de publicação', '2000'), 
  ('Edição', '1ª ed.')
]
'''


# 12. Do primeiro dicionário, retornar uma lista apenas com suas chaves
chaves = list(ficha_livro.keys())
print(chaves)

'''
Saída:
[
  'Título', 
  'Título original', 
  'Autor(a)', 
  'Editora', 
  'Páginas', 
  'Ano de publicação', 
  'Edição'
]
'''


# 13. Do primeiro dicionário, retornar uma lista apenas com os valores associados às suas chaves
valores = list(ficha_livro.values())
print(valores)

'''
[
  'Harry Potter e a Pedra Filosofal',
  "Harry Potter and the Philosopher's Stone", 
  'J.K. Rowling', 
  'Rocco', 
  '264', 
  '2000', 
  '1ª ed.'
]
'''


# 14. Criar um novo dicionário a partir das duas listas acima (itens 12 e 13)
novo_dicionario = dict(zip(chaves, valores))
print(novo_dicionario)

'''
{
  'Título': 'Harry Potter e a Pedra Filosofal', 
  'Título original': "Harry Potter and the Philosopher's Stone", 
  'Autor(a)': 'J.K. Rowling', 
  'Editora': 'Rocco', 
  'Páginas': '264', 
  'Ano de publicação': '2000', 
  'Edição': '1ª ed.'
}
'''


# 15. Remover do dicionário acima, o valor e chave associada referente ao número de páginas
novo_dicionario.pop('Páginas')
print(novo_dicionario)

'''
{
  'Título': 'Harry Potter e a Pedra Filosofal', 
  'Título original': "Harry Potter and the Philosopher's Stone", 
  'Autor(a)': 'J.K. Rowling', 
  'Editora': 'Rocco', 
  'Ano de publicação': '2000', 
  'Edição': '1ª ed.'
  }
'''