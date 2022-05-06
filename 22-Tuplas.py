'''
 *  Tuplas
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada
 '''

# 1 - Declaração inicial
livro = (
    'O Hobbit',
    'The Hobbit',
    'J.R.R. Tolkien',
    'Ficção',
    'HarperCollins',
    '5a.edição',
     2019,
    '336 p.',
)


# 2 - Retorno do tipo da estrutura de dados acima
print(type(livro)) # <class 'tuple'>


# 3 - Impressão da tupla
print(livro)
# ('O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.')


# 4 - Número de elementos que esta tupla contém
print(len(livro),'elementos') # 8 elementos


# 5 - Verificação de se as editoras 'HarperCollins' ou 'Oxford' constam nesta tupla
print('HarperCollins' in livro) # True
print('Oxford' in livro) # False


# 6 - Selecionar primeiro e último elementos da tupla:
print('Primeiro elemento:',livro[0]) # Primeiro elemento: O Hobbit
print('Último elemento:',livro[-1]) # Último elemento: 336 p.


# 7 - Imprimir apenas os valores referentes à edição deste livro:
print(livro[4:7])  # ('HarperCollins', '5a.edição', 2019)


# 8 - Considerando a nova estrutura abaixo, fazer a a concatenação das duas tuplas
livro_extra_info = (
 'Brochura',
 'Português',
 'Reinaldo José Lopes'
)
livro_tuplanova = livro + livro_extra_info
print(livro_tuplanova)
# ('O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.', 'Brochura',
# 'Português', 'Reinaldo José Lopes')


# 9 - Impressão desta nova tupla, com elementos dispostos linha a linha:
for value in livro_tuplanova:
    print(value)
'''
O Hobbit
The Hobbit
J.R.R. Tolkien
Ficção
HarperCollins
5a.edição
2019
336 p.
Brochura
Português
Reinaldo José Lopes
'''


# 10 - Considerando a nova estrutura apresentada abaixo, criar um dicionário com as chaves e valores correspondentes
livro_keys = (
    'Título:',
    'Título original:',
    'Autor:',
    'Gênero:',
    'Editora:',
    'Edição:',
    'Ano de edição:',
    'Número de páginas:',
    'Acabamento:',
    'Idioma:',
    'Tradutor:'
)
dicionario = dict(zip(livro_keys,livro_tuplanova))
print(dicionario)
# {'Título:': 'O Hobbit', 'Título original:': 'The Hobbit', 'Autor:': 'J.R.R. Tolkien', 'Gênero:': 'Ficção',
# 'Editora:': 'HarperCollins', 'Edição:': '5a.edição', 'Ano de edição:': 2019, 'Número de páginas:': '336 p.',
# 'Acabamento:': 'Brochura', 'Idioma:': 'Português', 'Tradutor:': 'Reinaldo José Lopes'}