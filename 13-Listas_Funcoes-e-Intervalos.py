# 1 - Imprima na tela uma lista de números de 0 a 20
numeros = list(range(21))
print(numeros) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 2 - Identifique o primeiro e último elementos da lista
primeiro = print(numeros[0]) # primeiro: 0
ultimo = print(numeros[-1]) # último: 20

# 3 - Retorne qual o número de elementos que a lsita possui
numero_elementos = print(len(numeros)) # número de elementos: 21

# 4 - Consegue criar duas listas ao separar os números pares dos ímpares?
pares = print(numeros[2::2]) # pares =  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
impares = print(numeros[1::2]) # impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 5 - Imprima a lista de números em ordem inversa
inversao = print(numeros[::-1]) # inversao = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 6 - Transforme os números de 1 a 10 em algarismos romanos. Os demais números devem permanecer inalterados.
numeros [1:11] = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
print(numeros)
# numeros = [0, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 7 - Utilizando a lista original de números, confira se estão presentes nela os números 16 e 32.
print(16 in numeros)  # True
print(32 in numeros)  # False

# 8 - Insira o número subsequente no final da lista:
numeros.append(21)
print(numeros)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

#9 - Insira mais 4 números subsequentes ao fim da lista:
numeros.extend([22,23,24,25])
print(numeros)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]