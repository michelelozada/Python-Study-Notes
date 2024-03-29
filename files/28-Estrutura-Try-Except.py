'''
 *  Estrutura Try Except
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada


1 - Escreva um algoritmo que leia um número. Este número informado pelo usuário deve necessariamente estar compreendido
no intervalo de 1 a 50 (ambos inclusos). Além disso, você deve usar um tratamento de exceção para evitar que o programa
seja abortado, caso o usuário digite um valor não-numérico.
'''

while True:
    try:
        n = int(input("Digite um número: "))
        if (n>= 1 and n<=50):
            print(f'> Resposta aceita: você informou um número dentro do intevalo.\n')
            break
        else:
            print('> Houve um erro: você informou um número fora do intervalo entre 1 e 50. Por favor, tente novamente.\n')
            continue
    except ValueError:
        print('> Houve um erro: o valor digitado não é um número. Por gentileza, comece novamente.\n')
        continue

'''
Outputs possíveis:
Digite um número: -55
> Houve um erro: você informou um número fora do intervalo entre 1 e 50. Por favor, tente novamente.

Digite um número: dez
> Houve um erro: o valor digitado não é um número. Por gentileza, comece novamente.

Digite um número: 25
> Resposta aceita: você informou um número dentro do intevalo.

'''



'''
 2 - Considerando os divisores abaixo, trate os erros que podem acontecer a fim de evitar que programa seja abortado
durante o procesamento das divisões:
'''
cont = 1
dividendo = 2
divisores = ['DIV',0,1,1.5]

for d in divisores:
    try:
        quociente = dividendo / d
        print(f'{cont}º resultado: O resultado da divisão de {dividendo} com {d} é {quociente:.2f}')
        cont += 1

    except TypeError:
        print(f'{cont}º resultado: O valor {d} é inválido para esta operação (motivo: não é possível realizar divisão com '
              f'valores não-numéricos).')
        cont += 1

    except ZeroDivisionError:
        print(f'{cont}º resultado: O valor 0 é inválido para esta operação (motivo: não é possível dividir um '
              f'número por zero).')
        cont += 1

'''
Output: 
1º resultado: O valor DIV é inválido para esta operação (motivo: não é possível realizar divisão com valores não-numéricos).
2º resultado: O valor 0 é inválido para esta operação (motivo: não é possível dividir um número por zero).
3º resultado: O resultado da divisão de 2 com 1 é 2.00
4º resultado: O resultado da divisão de 2 com 1.5 é 1.33
'''