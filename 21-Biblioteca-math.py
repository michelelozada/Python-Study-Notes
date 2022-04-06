# A - Importando a biblioteca math
import math


# B - Retorno do maior e do menor inteiro de um número real:
n = float(input('Informe um número real: '))
print(f'> O maior inteiro do número {n} é',math.ceil(n))
print('> Já o menor inteiro deste número é',math.floor(n))
'''
Informe um número real: 3.5
> O maior inteiro do número 3.5 é 4
> Já o menor inteiro deste número é 3
'''


# C - Retornando o máximo divisor comum (MDC) entre dois números
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print(f'> O máximo divisor comum (MDC) entre os números {n1} e {n2} é {math.gcd(n1,n2)}.')
'''
Informe o primeiro número: 18
Informe o segundo número: 60
> O máximo divisor comum (MDC) entre os números 18 e 60 é 6.
'''


# D - Retorno da raiz quadrada de um número
n = float(input('Forneça um número para retorno da sua raiz quadrada: '))
raiz = math.sqrt(n)
print (f'> Resultado: A raiz quadrada de {n} é {raiz:.3f}')
'''
Forneça um número para retorno da sua raiz quadrada: 16
> Resultado: A raiz quadrada de 16.0 é 4.000
'''


# E - Cálculo da potência de um número
n = int(input('Informe a base: '))
p = int(input('Qual o valor do expoente? '))
print(f'> O número {n} elevado à {p}ª potência é {(math.pow(n,p))}')
'''
Informe a base: 3
Qual o valor do expoente? 2
> O número 3 elevado à 2ª potência é 9.0
'''


# F - Retorno do fatorial de um número
num = int(input('Forneça um número para que seja retornado seu fatorial: '))
print(f'> Resultado: {num}! = {math.factorial(num)}')
'''
Forneça um número para que seja retornado seu fatorial: 5
> Resultado: 5! = 120
'''


# G - Informando o valor da constante pi
print('> Número Pi (π) é um número irracional cujo valor é',math.pi)
> Número Pi (π) é um número irracional cujo valor é 3.141592653589793