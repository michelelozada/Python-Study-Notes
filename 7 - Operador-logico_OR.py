'''
Escreva um algoritmo que simule uma calculadora que realize as 4 operações aritméticas básicas.
'''

print('- CALCULADORA BÁSICA -')
print('\nMenu com as operações matemáticas disponíves:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

op = input('\nQual operação você deseja realizar? ')
if (op == '1') or (op == '2') or (op == '3') or (op == '4'):
    n1 = int(input('\nMuito bem, digite o primero número: '))
    n2 = int(input('E agora o segundo número: '))

    if (op == '1'):
        nome = 'adição'
        result = n1 + n2
    elif (op == '2'):
        nome = 'subtração'
        result = n1 - n2
    elif (op == '3'):
        nome = 'multiplicação'
        result = n1 * n2
    elif (op == '4'):
        nome = 'divisão'
        if (n1 % n2 == 0):
            result = n1 // n2
        else:
            result = n1 / n2
    print(f'\n> O valor da operação de {nome} de {n1} com {n2} resultou em {result}.')

else:
    print('\n> Hey, esta opção nao existe no menu. Por favor, tente novamente...')

'''
- CALCULADORA BÁSICA -

Menu com as operações matemáticas disponíves:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão

Qual operação você deseja realizar? 3

Muito bem, digite o primero número: 6
E agora o segundo número: 8

> O valor da operação de multiplicação de 6 com 8 resultou em 48.
'''