'''
 *  Dicionários
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada
 '''


# 1 - Declaração inicial
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


# 2 - Retorno do tipo da estrutura de dados acima
print(type(ficha_livro))  # <class 'dict'>


# 3 - Número de elementos que este dicionário contém:
print(len(ficha_livro),'elementos')  # 5 elementos


# 4 - Consulta do valor associado à chave 'editora':
print(ficha_livro.get('Editora'))  # Rocco
#ou
print(ficha_livro['Editora']) # Rocco


# 5 - Verificação de se as chaves 'Páginas' e 'Capítulos' constam ou não neste dicionário:
print('Páginas' in ficha_livro)  # True
print('Capítulos' in ficha_livro) # False


# 6 - Atualizando o valor de uma chave
ficha_livro['Autor(a)'] = 'J.K. Rowling'


# 7 - Adição de uma nova chave e respectivo valor
ficha_livro['Ano de publicação'] = 2000
print(ficha_livro)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000}


# 8 - Criação de um dicionário independente baseado no primeiro, seguido da alteração dos valores abaixo:
ficha_livro2 = ficha_livro.copy()
ficha_livro2['Título'] = 'Harry Potter e o Prisioneiro de Azkaban'
ficha_livro2['Título original'] = 'Harry Potter and the Prisoner of Azkaban'
ficha_livro2['Páginas']= '288 páginas'
ficha_livro2['Ano de publicação'] = 2007
print(ficha_livro2)
# {'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban',
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007}


# 9 - Para ambas as listas, inclusão da informação de que se trata da 1ª edição dos livros.
edition ={
    'Edição': '1ª ed.',
}
ficha_livro.update(edition)
ficha_livro2.update(edition)
print(ficha_livro)
print(ficha_livro2)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}
# {'Título': 'Harry Potter e o Prisioneiro de Azkaban', 'Título original': 'Harry Potter and the Prisoner of Azkaban',
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '288 páginas', 'Ano de publicação': 2007, 'Edição': '1ª ed.'}


# 10 - Considerando-se somente o primeiro dicionário:
# 10.1 - Retorno de uma lista com os pares chave-valor do dicionário
print(ficha_livro.items())
#dict_items([('Título', 'Harry Potter e a Pedra Filosofal'), ('Título original', "Harry Potter and the Philosopher's
# Stone"), ('Autor(a)', 'J.K. Rowling'), ('Editora', 'Rocco'), ('Páginas', '264 páginas'), ('Ano de publicação', 2000),
# ('Edição', '1ª ed.')])


# 10.2 - Retorno de uma lista apenas com as chaves do dicionário
chaves = ficha_livro.keys()
print(chaves)
# dict_keys(['Título', 'Título original', 'Autor(a)', 'Editora', 'Páginas', 'Ano de publicação', 'Edição'])


# 10.3 - Retorno de uma lista apenas com os valores do dicionário
valores = ficha_livro.values()
print(valores)
# dict_values(['Harry Potter e a Pedra Filosofal', "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 'Rocco',
# '264 páginas', 2000, '1ª ed.'])


# 10.4 - Criação de um novo dicionário a partir das duas listas acima:
novo_dicionario = dict(zip (chaves,valores))
print(novo_dicionario)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Páginas': '264 páginas', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}


# 10.5 - Remoção do dicionário do valor e chave associada referente ao número de páginas
novo_dicionario.pop('Páginas')
print(novo_dicionario)
# {'Título': 'Harry Potter e a Pedra Filosofal', 'Título original': "Harry Potter and the Philosopher's Stone",
# 'Autor(a)': 'J.K. Rowling', 'Editora': 'Rocco', 'Ano de publicação': 2000, 'Edição': '1ª ed.'}