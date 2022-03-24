# 1 - Imprima na tela uma lista de números que vá de 0 a 20.
numeros = list(range(21))
print(numeros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 2 - Remova da lista o número 0.
numeros.remove(0)
print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 3 - Identifique o primeiro e último elemento da lista.
primeiro = print('primeiro elemento:', numeros[0]) # primeiro elemento: 1
ultimo = print('último elemento:', numeros[-1]) # último elemento: 20


# 4 - Retorne o maior valor e o menor valor da lista:
primeiro = print('maior valor:', max(numeros)) # maior valor: 20
ultimo = print('menor valor:', min(numeros)) # menor valor: 1


# 5 - Apresente a soma de todos os elementos da lista:
print('O resultado da soma de todos os elementos desta lista é',sum(numeros))
# O resultado da soma de todos os elementos desta lista é 210


# 6 - Retorne qual o número de elementos que a lista possui.
numero_elementos = print('número de elementos desta lista:',len(numeros)) # número de elementos desta lista: 20


# 7 - Consegue criar duas sublistas ao separar os números pares dos ímpares?
pares = print(numeros[1::2]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
impares = print(numeros[::2]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# 8 - Imprima a lista original de números na order decrescente.
numeros_decrescentes = print(numeros[::-1]) # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# 9 - Transforme os números de 1 a 10 da lista original em algarismos romanos. Os demais números devem permanecer inalterados.
numeros [:10] = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
print(numeros)
# numeros = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# 10 - Retomando a lista original, insira o número subsequente esperado no final da lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros.append(21)
print(numeros)
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]


# 11 - Agora insira o intervalo dos 4 números subsequentes esperados no fim da lista.
numeros.extend([22,23,24,25])
print(numeros)
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


# 12 - Crie um algoritmo que responda se os números 16 e 32 estão presentes nesta lista.
teste = int(input('Qual número deseja verificar se está na lista? '))
if teste in numeros:
    print (f'O número {teste} está nesta lista.')
else:
    print(f'O número {teste} não está nesta lista.')
'''
> Qual número deseja verficar se está na lista? 16
    O número 16 está nesta lista.

> Qual número deseja verficar se está na lista? 32
    O número 32 não está nesta lista.
'''