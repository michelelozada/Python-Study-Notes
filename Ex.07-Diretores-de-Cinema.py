"""
Foi publicada uma lista com os diretores mais influentes de todos os tempos em Hollywood:
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
11. George Lucas*
12. Charles Chaplin
13. Ingmar Bergman
14. James Cameron*
15. Federico Fellini
(*) Indica os diretores vivos.

Portanto:
A - Liste os 10 dos diretores de cinema mais influentes de todos os tempos. Imprima  essa lista na ordem decrescente.
B - Crie um algoritmo que responda se os cineastas Woody Allen e Fran Capra estão nesta lista.
C - Inclua neal os diretores subsequentes. Agora a lista deve er impressa na ordem crescente.
D - Por fim, a lista deve mostar somente os cinco maiores diretores vivos.
"""
# A
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
Lista dos 10 diretores mais influentes de Hollywood:
['Francis Ford Coppola', 'Woody Allen', 'Tim Burton', 'Alfred Hitchcock', 'Martin Scorsese', 'Quentin Tarantino', 
'Jean-Luc Godard', 'Bernardo Bertolucci', 'Stanley Kubrick', 'Steven Spielberg'].
"""
# B
sim = 'está na lista dos 10 maiores diretores de todos os tempos.'
nao = 'não está na lista dos 10 maiores diretores de todos os tempos.'
diretor = input('\nQual o nome do diretor? ')

if diretor in maiores_diretores:
    print('> %s %s'%(diretor,sim))
else:
    print('> %s %s' %(diretor,nao))

"""
Output:
Qual o nome do diretor? Woody Allen
> Woody Allen está na lista dos 10 maiores diretores de todos os tempos.

Qual o nome do diretor? Frank Capra
> Frank Capra não está na lista dos 10 maiores diretores de todos os tempos.
"""
#C

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
#3
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

print(f'\nLista dos 5 diretores vivos mais influentes de Hollywood:\n{maiores_diretores[0:5]}.')

"""
Output:
Lista dos 5 diretores vivos mais influentes de Hollywood:
['Steven Spielberg', 'Quentin Tarantino', 'Martin Scorsese', 'Tim Burton', 'Woody Allen']
"""