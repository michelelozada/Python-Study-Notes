'''
 *  Operador lógico AND
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada


Escreva um algoritmo que receba três valores, representando os lados de um triângulo.
Lembre-se de que para formar um triângulo:
 - Nenhum lado pode ter medida igual a zero;
 - A medida de qualquer um dos lados não pode ser maior que a soma das medidas de outros dois.
Após verificar se os valores formam um triângulo, classifique-os.
'''

print('Digite abaixo as medidas do triângulo referentes ao:')
l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

# Duas verificações utilizando o operador AND para constatar se, de acordo com as medidas fornecidas, se trata realmente de um triângulo.
if (l1 > 0) and (l2 > 0) and (l3 > 0):
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        if (l1 != l2) and (l1 != l3):
            print('\n> Este é um triângulo escaleno, pois todos os seus lados apresentam medidas diferentes.')
        elif (l1 == l2) and (l1 == l3):
            print('\n> Este é um triângulo equilátero, pois todos os seus lados são congruentes.')
        else:
            print('\n> Este é um triângulo isósceles, pois dois de seus lados apresentam a mesma medida.')
    else:
        print('\n> Ops, estas medidas não formam um triângulo: ao menos um dos valores indicados é maior que os outros dois.')
else:
    print('\n> Ops, estas medidas não formam um triângulo, pois ao menos um dos valores indicados é igual a zero.')

'''
Digite abaixo as medidas do triângulo referentes ao:
Lado 1: 9
Lado 2: 4
Lado 3: 9

> Este é um triângulo isósceles, pois dois de seus lados apresentam a mesma medida.
'''