'''
 *  Exercício: Dois números
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada
'''


def mensagem():
    print('Desculpe, mas é necesário que seja um número inteiro\n\nNova tentativa.....')

def maior():
    if(n1>n2):
        status = 'maior'
        diferenca = n1 - n2
    else:
        status = 'menor'
        diferenca = n2 - n1
    print(f' - O primeiro número informado ({n1}) é {status} que o segundo número ({n2}) por uma diferença de {diferenca} unidade(s)')

def soma():
    soma= n1+n2
    print(' - A soma destes dois números:',soma)

def subtracao():
    subtracao= n1-n2
    print(' - A subtração:',subtracao)


def multiplicacao():
    multiplicacao = n1*n2
    print(' - A multiplicação dos dois:',multiplicacao)

def divisao():
    divisao = n1/n2
    print(' - A divisão entre eles:',divisao)

# Programa principal
while True:
    try:
        n1 = int(input('\n>> Me informe um número inteiro, por favor: '))
        if (int(n1) == n1):
            print('Ok, obrigada!')
    except ValueError:
        mensagem()
        continue

    print(f'\n>> Informações sobre o número {n1}:')
    if (n1 % 2 == 0):
        print(' - Trata-se de um número par.')
    else:
        print(' - Trata-se de um número ímpar.')
    print(' - O número que vem antes dele é o', n1 - 1, 'e o número que vem depois é o',n1 + 1)

    while True:
        try:
            n2 = int(input('\n>> Agora preciso que você me informe outro número inteiro: '))
            if (int(n2) == n2):
                print('Ok, registrado!')
                break
        except ValueError:
            mensagem()
            continue

    print(f'\n>> Informações sobre o número {n2}:')
    if (n2 % 2 == 0):
        print(' - Trata-se de um número par.')
    else:
        print(' - Trata-se de um número ímpar.')
    print(' - O número que vem antes dele é o', n2 - 1, 'e o número que vem depois é o',n2 + 1)


    print('\n>> Vamos descobrir qual a relação entre estes dois números?')
    maior()
    soma()
    subtracao()
    multiplicacao()
    divisao()
    print(' - Ambos são simultaneamante múltiplos do(s) número(s):',end='')
    if (n1 % 2 == 0) and (n2 % 2 == 0):
        print(' 2 ', end='')
    if (n1 % 3 == 0) and (n2 % 3 == 0):
        print(' 3 ', end='')
    if (n1 % 4 == 0) and (n2 % 4 == 0):
        print(' 4 ', end='')
    if (n1 % 5 == 0) and (n2 % 5 == 0):
        print(' 5 ', end='')
    if (n1 % 6 == 0) and (n2 % 6 == 0):
        print(' 6 ', end='')
    if (n1 % 7 == 0) and (n2 % 7 == 0):
        print(' 7 ', end='')
    if (n1 % 8 == 0) and (n2 % 8 == 0):
        print(' 8 ', end='')
    if (n1 % 9 == 0) and (n2 % 9 == 0):
        print(' 9 ', end='')
    if (n1 % 9 != 0) and (n2 % 9 != 0):
        print('não há múltiplos em comum')
    break

"""
>> Me informe um número inteiro, por favor: 270
Ok, obrigada!

>> Informações sobre o número 270:
 - Trata-se de um número par.
 - O número que vem antes dele é o 269 e o número que vem depois é o 271 

>> Agora preciso que você me informe outro número inteiro: 125
Ok, registrado!

>> Informações sobre o número 125:
 - Trata-se de um número ímpar.
 - O número que vem antes dele é o 124 e o número que vem depois é o 126

>> Vamos descobrir qual a relação entre estes dois números?
 - O primeiro número informado (270) é maior que o segundo número (125) por uma diferença de 145 unidade(s)
 - A soma destes dois números: 395
 - A subtração: 145
 - A multiplicação dos dois: 33750
 - A divisão entre eles: 2.16
 - Ambos são simultaneamante múltiplos do(s) número(s): 5 
"""