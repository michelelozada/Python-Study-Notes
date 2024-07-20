'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício criado para praticar conceitos aprendidos

Escreva um algoritmo que defina, mediante sorteio, qual será a ordem em que cada um dos
colaboradores de uma empresa terá direito a uma sexta-feira de folga.
'''


import random

def imprimir_escala():
    print('\nEscala de folga às 6ªs-feiras')
    print('-' * 30)

    colaboradores = [
      'Ana', 'Enzo', 'Carla', 'Marcos',
      'Morgana', 'Paulo', 'Vanessa', 'Lucas'
    ]

    for i in range(1, len(colaboradores) + 1):
      colaborador = random.choice(colaboradores)
      print(f'{i}º | {colaborador}')
      colaboradores.remove(colaborador)


imprimir_escala()