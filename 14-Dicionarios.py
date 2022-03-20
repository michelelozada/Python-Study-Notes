# 1 - Estrutura inicial
ficha_livro = {
    'Título': 'Harry Potter e a Pedra Filosofal',
    'Título original': 'Harry Potter and the Philosopher\'s Stone',
    'Autor(a)': 'Rowling, J.K.',
    'Editora': 'Rocco',
    'Páginas': '264 páginas'
}


# 2 - Retorno do tipo da estrutura de dados acima
print(type(ficha_livro))
# <class 'dict'>


# 3 - Impressão do dicionário
print(ficha_livro)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone", 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas'}


# 4 - Acesso do valor do índice correspondente à editora do livro
print(ficha_livro['Editora'])
# Rocco


# 5 - Adição de uma nova chave e valor
ficha_livro['Ano de publicação'] = 2000
print(ficha_livro)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone", 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000}


# 6 - Criação de um dicionário independente baseado no primeiro, seguido da alteração dos valores abaixo
ficha_livro2 = ficha_livro.copy()
ficha_livro2['Título'] = 'Harry Potter e o Prisioneiro de Azkaban'
ficha_livro2['Título original'] = 'Harry Potter and the Prisoner of Azkaban'
ficha_livro2['Páginas']= '288 páginas'
ficha_livro2['Ano de publicação'] = 2007
print(ficha_livro2)
#{'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban', 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007}


# 7 - Para ambas as listas, inclusão da informação de que se trata da 1ª ediição dos livros.
edition ={
    'Edição': '1ª ed.',
}
ficha_livro.update(edition)
ficha_livro2.update(edition)
print(ficha_livro)
print(ficha_livro2)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone", 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}
# {'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban', 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007, 'Edição': '1ª ed.'}


# 8 - Considerando-se somente o primeiro dicionário:
# 8.1 - Retorno de uma lista apenas com as chaves do dicionário
print(ficha_livro.keys())
# dict_keys(['Título', 'Título original', 'Autor(a)', 'Editora', 'Páginas', 'Ano de publicação', 'Edição'])


# 8.2 - Retorno de uma lista apenas com os valores do dicionário
print(ficha_livro.values())
# dict_values(['Harry Potter e a Pedra Filosofal', "Harry Potter and the Philosopher's Stone", 'Rowling, J.K.', 'Rocco', '264 páginas', 2000, '1ª ed.'])


# 8.3. - Retorno de uma lista com os pares chave-valor do dicionário
print(ficha_livro.items())
#dict_items([('Título', 'Harry Potter e a Pedra Filosofal'), ('Título original', "Harry Potter and the Philosopher's Stone"), ('Autor(a)', 'Rowling, J.K.'), ('Editora', 'Rocco'), ('Páginas', '264 páginas'), ('Ano de publicação', 2000), ('Edição', '1ª ed.')])