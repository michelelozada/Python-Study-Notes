"""
Escreva um algoritmo que receba 4 notas de um aluno em determinada disciplina, calcule a média delas e informe se este
aluno foi aprovado ou se ficou para recuperação.
"""

count = 1
sum = 0
print(':: Cálculo das notas da disciplina de Informática Básica ::')

while (count < 5):
    n = float(input(f'Qual a nota da {count}ª avaliação? '))
    count += 1
    sum += n
media = sum/count
print(f'\n> A soma de todas as notas: {sum:.1f}')
print(f'> A média final obtida: {media:.1f}')

if (media >= 7.0):
    status='está aprovado'
else:
    status='ficou para recuperação'
print(f'\nSTATUS: Este aluno {status} na disciplina Informática Básica.')


"""
:: Cálculo das notas da disciplina de Informática Básica ::
Qual a nota da 1ª avaliação? 6.5
Qual a nota da 2ª avaliação? 7.5
Qual a nota da 3ª avaliação? 8.0
Qual a nota da 4ª avaliação? 6.0

> A soma de todas as notas: 28.0
> A média final obtida: 5.6

STATUS: Este aluno ficou para recuperação na disciplina Informática Básica.
"""