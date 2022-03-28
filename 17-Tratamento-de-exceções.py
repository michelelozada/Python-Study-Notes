'''
Escreva um algoritmo que leia um número. Este número informado pelo usuário deve necessariamente estar compreendido
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
Output:
Digite um número: -55
> Houve um erro: você informou um número fora do intervalo entre 1 e 50. Por favor, tente novamente.

Digite um número: dez
> Houve um erro: o valor digitado não é um número. Por gentileza, comece novamente.

Digite um número: 25
> Resposta aceita: você informou um número dentro do intevalo.
'''
