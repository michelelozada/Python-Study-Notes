> **Tuplas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão sobre tuplas em Python
```
- Classe associada: tuple

- Cada item dentro da tupla é chamado de elemento (ou mesmo de item) 

- É um estrutura de dados de sequência *imutável*, i.e., após a criação da tupla, elementos não podem 
ser modificados, adicionados ou removidos dali 

- Tuplas são ordenadas, i.e., sua ordem é baseada na sequência em que os elementos foram ali inseridos

- Elementos são acessados pela posição  (= seu índice) deles na tupla

- Exemplo da sintaxe básica: (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
```

&nbsp;  

### 1 - Declaração inicial
```py

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
```

&nbsp;


### 2 - Retorno do tipo da estrutura de dados acima
```py

print(type(livro)) # <class 'tuple'>
```

&nbsp;

### 3 - Impressão da tupla
```py

print(livro)
# ('O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.')
```

&nbsp;

### 4 - Número de elementos que esta tupla contém
```py

print(len(livro),'elementos') # 8 elementos
```

&nbsp;

### 5 - Indicar qual o número do índice que autor ocupa na tupla
```py

print(livro.index('J.R.R. Tolkien'))  # 2
```

&nbsp;


### 6 - Associe cada elemento da tupla a uma etiqueta e imprima três delas:
```py

titulo, tituloOriginal, autor, genero, editora, edicao, ano,paginas = livro # desempacotar uma tupla
print(titulo) # O Hobbit
print(genero) # Ficção
print(ano) # 2019
```

&nbsp;

### 7 - Verificação de se as editoras 'HarperCollins' ou 'Oxford' constam nesta tupla
```py

print('HarperCollins' in livro) # True
print('Oxford' in livro) # False
```

&nbsp;

### 8 - Selecionar primeiro e último elementos da tupla:
```py

print('Primeiro elemento:',livro[0]) # Primeiro elemento: O Hobbit
print('Último elemento:',livro[-1]) # Último elemento: 336 p.
```

&nbsp;

### 9 - Imprimir apenas os valores referentes à edição deste livro:
```py

print(livro[4:7])  # ('HarperCollins', '5a.edição', 2019)
```

&nbsp;

### 10 - Considerando a nova estrutura abaixo, fazer a a concatenação das duas tuplas
```py

livro_extra_info = (
 'Brochura',
 'Português',
 'Reinaldo José Lopes'
)
livro_tuplanova = livro + livro_extra_info
print(livro_tuplanova)

'''
('O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.', 'Brochura',
'Português', 'Reinaldo José Lopes')
'''
```

&nbsp;

### 11 - Converter esta nova tupla em uma lista
```py

print(list(livro_tuplanova))
# ['O Hobbit', 'The Hobbit', 'J.R.R. Tolkien', 'Ficção', 'HarperCollins', '5a.edição', 2019, '336 p.', 'Brochura', 'Português', 'Reinaldo José Lopes']
```

&nbsp;

### 12 - Impressão desta nova tupla, com elementos dispostos linha a linha:
```py

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
```

&nbsp;

### 13 - Considerando a nova estrutura apresentada abaixo, criar um dicionário com as chaves e valores correspondentes
```py

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

'''
{'Título:': 'O Hobbit', 'Título original:': 'The Hobbit', 'Autor:': 'J.R.R. Tolkien', 'Gênero:': 'Ficção',
'Editora:': 'HarperCollins', 'Edição:': '5a.edição', 'Ano de edição:': 2019, 'Número de páginas:': '336 p.',
'Acabamento:': 'Brochura', 'Idioma:': 'Português', 'Tradutor:': 'Reinaldo José Lopes'}
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>