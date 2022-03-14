"""
Foi publicada uma lista com os diretores mais influentes de todos os tempos. Portanto, crie uum algoritmo que:

1- Liste os 10 diretores de cinema mais influentes de todos os tempos:
1. Steven Spielberg*
2. Stanley Kubrick
3. Bernardo Bertolucci
4. Jean-Luc Godard
5. Quentin Tarantino*
6. Martin Scorsese*
7. Alfred Hitchcock
8. Tim Burton*
9. Woody Allen*
10. Francis Ford Coppola*

2 - Que inclua também os próximos cinco nomes:
11. George Lucas*
12. Charles Chaplin
13. Ingmar Bergman
14. James Cameron*
15. Federico Fellini

3 - Por fim, a lista deve mostar apenas os cinco maiores diretores vivos (são os identificados acima com asteriscos)
"""
# 1
maiores_diretores=[
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

print('1) A lista dos 10 diretores mais influentes de Hollywood:')
print(maiores_diretores)
# 2
maiores_diretores.extend([
    'George Lucas',
    'Charles Chaplin',
    'Ingmar Bergman',
    'James Cameron',
    'Federico Fellini'
])
print('\n2) A lista dos 15 diretores mais influentes de Hollywood:')
print(maiores_diretores)

3#
if 'Stanley Kubrick' in maiores_diretores:
    maiores_diretores.remove('Stanley Kubrick')
if 'Bernardo Bertolucci' in maiores_diretores:
    maiores_diretores.remove('Bernardo Bertolucci')
if 'Jean-Luc Godard' in maiores_diretores:
    maiores_diretores.remove('Jean-Luc Godard')
if 'Alfred Hitchcock' in maiores_diretores:
    maiores_diretores.remove('Alfred Hitchcock')
if 'Charles Chaplin' in maiores_diretores:
    maiores_diretores.remove('Charles Chaplin')
if 'Ingmar Bergman' in maiores_diretores:
    maiores_diretores.remove('Ingmar Bergman')
if 'Federico Fellini' in maiores_diretores:
    maiores_diretores.remove('Federico Fellini')

print('\n3) A lista dos 5 diretores vivos mais influentes de Hollywood:')
print(maiores_diretores[0:5])

"""
Output:
1) Os 10 diretores mais influentes de todos os tempos:
['Steven Spielberg', 'Stanley Kubrick', 'Bernardo Bertolucci', 'Jean-Luc Godard', 'Quentin Tarantino', 'Martin Scorsese',
'Alfred Hitchcock', 'Tim Burton', 'Woody Allen', 'Francis Ford Coppola']

2) Os 15 diretores mais influentes de todos os tempos:
['Steven Spielberg', 'Stanley Kubrick', 'Bernardo Bertolucci', 'Jean-Luc Godard', 'Quentin Tarantino', 'Martin Scorsese', 
'Alfred Hitchcock', 'Tim Burton', 'Woody Allen', 'Francis Ford Coppola', 'George Lucas', 'Charles Chaplin', 'Ingmar Bergman', 
'James Cameron', 'Federico Fellini']

3) Os  5 diretores vivos mais influentes de todos os tempos:
['Steven Spielberg', 'Quentin Tarantino', 'Martin Scorsese', 'Tim Burton', 'Woody Allen']
"""