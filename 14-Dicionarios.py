ficha_livro = {
    'Título': 'Harry Potter e a Pedra Filosofal',
    'Título original': 'Harry Potter and the Philosopher\'s Stone',
    'Autor(a)': 'Rowling, J.K.',
    'Editora': 'Rocco',
    'Páginas': '264 páginas'
}


# Retorno do tipo da estrutura de dados acima
print(type(ficha_livro))
# <class 'dict'>


# Impressão do dicionário
print(ficha_livro)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
# 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas'}


# Acessar o valor do índice correspondente à editora do livro
print(ficha_livro['Editora'])
# Rocco


# Adição de uma nova chave e valor
ficha_livro['Ano de publicação'] = 2000
print(ficha_livro)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone", 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000}

# Criação um novo dicionário independente baseado no primeiro, seguido de alteração de valores.
ficha_livro2 = ficha_livro.copy()
ficha_livro2['Título'] = 'Harry Potter e o Prisioneiro de Azkaban'
ficha_livro2['Título original'] = 'Harry Potter and the Prisoner of Azkaban'
ficha_livro2['Páginas']= '288 páginas'
ficha_livro2['Ano de publicação'] = 2007
print(ficha_livro2)
#{'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban', 'Autor(a)': 'Rowling, J.K.', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007}