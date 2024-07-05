'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Acessando valores e fazendo manipulações em tuplas
'''


# 1. Declaração inicial de uma tupla
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


# 2. Verificar qual o tipo da estrutura de dados acima
print(type(livro)) 

'''
Saída: <class 'tuple'>
'''


# 3. Imprimir o conteúdo da tupla
print(livro)

'''
Saída: ('O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.')
'''


# 4. Informar o número de elementos que a tupla contém (utilize o método `len()`)
print(len(livro))

'''
Saída: 8
'''


# 5. Indicar qual o número do índice que autor J.R.R. Tolkien ocupa na tupla  (utilize o método `index()`)
print(livro.index("J.R.R. Tolkien"))  

'''
Saída: 2
'''


# 6. Associar cada elemento da tupla a uma etiqueta e imprimir três delas (para isso, 'desempacote' a tupla)  
titulo, tituloOriginal, autor, genero, editora, edicao, ano, paginas = livro

print(titulo)  # Saída: O Hobbit
print(genero)  # Saída: Ficção
print(editora) # Saída: HarperCollins


# 7. Verificar se as editoras 'Oxford' ou 'HarperCollins' são elementos desta tupla
print("Oxford" in livro)  # Saída: False
print("HarperCollins" in livro)  # Saída: True


# 8. Informar quais são o primeiro e o último elementos da tupla  
print(livro[0])   # Saída: O Hobbit
print(livro[-1])  # Saída: 336 p.


# 9. Imprimir apenas os valores referentes à editora, edição e ano (utilize a técnica de slicing) 
print(livro[4:7])  

'''
Saída: ('HarperCollins', '5a.edição', 2019)
'''


# 10. Considerando a nova estrutura abaixo, fazer a concatenação das duas tuplas  
infoExtra = (
    'Brochura',
    'Português',
    'Reinaldo José Lopes'
)

livro_values = livro + infoExtra
print(livro_values)

'''
Saída: 
(
  'O Hobbit', 
  'The Hobbit', 
  'J.R.R. Tolkien', 
  'Ficção', 
  'HarperCollins', 
  '5a.edição', 
  2019, 
  '336 p.', 
  'Brochura', 
  'Português', 
  'Reinaldo José Lopes'
)
'''


# 11. Imprimir elementos desta nova tupla, dispostos linha a linha:
for value in livro_values:
    print(value)

'''
Saída: 
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


# 12. Considerando a nova tupla abaixo, criar um dicionário com as chaves e valores correspondentes (utilize o método `zip()`)  

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
livro_dicionario = dict(zip(livro_keys, livro_values))
print(livro_dicionario)

'''
Saída: 
{
  'Título:': 'O Hobbit', 
  'Título original:': 'The Hobbit', 
  'Autor:': 'J.R.R. Tolkien', 
  'Gênero:': 'Ficção',
  'Editora:': 'HarperCollins', 
  'Edição:': '5a.edição', 
  'Ano de edição:': 2019, 
  'Número de páginas:': '336 p.',
  'Acabamento:': 'Brochura',
  'Idioma:': 'Português',
  'Tradutor:': 'Reinaldo José Lopes'
}
'''