"""
Foi publicada uma lista com os diretores mais influentes de todos os tempos em Hollywood:
1º. Steven Spielberg
2º. Stanley Kubrick*
3º. Bernardo Bertolucci*
4º. Jean-Luc Godard*
5º. Quentin Tarantino
6º. Martin Scorsese
7º. Alfred Hitchcock*
8º. Tim Burton
9º. Woody Allen
10º. Francis Ford Coppola
11º. George Lucas
12º. Charles Chaplin*
13º. Ingmar Bergman*
14º. James Cameron
15º. Federico Fellini*
(*) Indica os diretores já falecidos
"""


# A - Liste os 10 dos diretores de cinema mais influentes de todos os tempos. Imprima  essa lista na ordem decrescente.
maiores_diretores = [
    'Steven Spielberg',
    'Stanley Kubrick',
    'Bernardo Bertolucci',
    'Jean-Luc Godard',
    'Quentin Tarantino',
    'Martin Scorsese',
    'Alfred Hitchcock',
    'Tim Burton',
    'Woody Allen',
    'Francis Ford Coppola'
]
print(f'Lista dos 10 diretores mais influentes de Hollywood:\n{maiores_diretores[::-1]}.')

"""
Output:
Lista dos 10 diretores mais influentes de Hollywood: ['Francis Ford Coppola', 'Woody Allen', 'Tim Burton', 'Alfred Hitchcock', 
'Martin Scorsese', 'Quentin Tarantino', 'Jean-Luc Godard', 'Bernardo Bertolucci', 'Stanley Kubrick', 'Steven Spielberg'].
"""


# B - Inclua nela os 5 nomes subsequentes. Agora a lista deve ser impressa na ordem crescente.
maiores_diretores.extend([
    'George Lucas',
    'Charles Chaplin',
    'Ingmar Bergman',
    'James Cameron',
    'Federico Fellini'
])
print(f'\nLista dos 15 diretores mais influentes de Hollywood:\n{maiores_diretores}.')

"""
Output:
Lista dos 15 diretores mais influentes de Hollywood:
['Steven Spielberg', 'Stanley Kubrick', 'Bernardo Bertolucci', 'Jean-Luc Godard', 'Quentin Tarantino', 'Martin Scorsese', 
'Alfred Hitchcock', 'Tim Burton', 'Woody Allen', 'Francis Ford Coppola', 'George Lucas', 'Charles Chaplin', 'Ingmar Bergman', 
'James Cameron', 'Federico Fellini'].
"""


# C - Crie um algoritmo que responda se os cineastas Woody Allen e Fran Capra estão nesta lista.
# Se a resposta for positiva, deve informar qual o número do índice que o diretor ocupa na lista acima dos diretores.
consulta = [
    'Woody Allen',
    'Frank Capra'
]
sim = 'está'
nao = 'não está'
msg = 'na lista dos 10 maiores diretores mais influentes de todos os tempos.'

for diretor in consulta:
    if diretor in maiores_diretores:
        print('\n> %s %s %s' % (diretor, sim, msg), end=' ')
        print(f'Ele ocupa o índice de nº {maiores_diretores.index(diretor)} na lista.')
    else:
        print('> %s %s %s' % (diretor, nao, msg))

"""
Output:
> Woody Allen está na lista dos 10 maiores diretores mais influentes de todos os tempos. Ele ocupa o índice de nº 8 na lista.
> Frank Capra não está na lista dos 10 maiores diretores mais influentes de todos os tempos.
"""


# D - Apresente a lista agora com apenas os cinco maiores diretores vivos.
deceased_directors =[
    'Stanley Kubrick',
    'Bernardo Bertolucci',
    'Jean-Luc Godard',
    'Alfred Hitchcock',
    'Charles Chaplin',
    'Ingmar Bergman',
    'Federico Fellini'
]

for diretor in deceased_directors:
    if diretor in maiores_diretores:
        maiores_diretores.remove(diretor)
print(f'\nLista dos 5 diretores vivos mais influentes de Hollywood:\n{maiores_diretores[0:5]}.')

"""
Output:
Lista dos 5 diretores vivos mais influentes de Hollywood:
['Steven Spielberg', 'Quentin Tarantino', 'Martin Scorsese', 'Tim Burton', 'Woody Allen'].
"""