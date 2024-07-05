'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> > Acessando valores e fazendo manipulações em listas
'''

# 1. Imprimir na tela uma lista de números que vá de 0 a 20
numeros = list(range(21))
print(numeros) 

'''
Saída:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


# 2. Remover da lista o número 0
numeros.remove(0) 
print(numeros) 

'''
Saída:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


# 3. Remover da lista o elemento que tem o índice de número 5
numeros.pop(5)  
print(numeros)

'''
Saída:
[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


# 4. Inserir novamente o número 6 na lista
numeros.insert(5, 6)
print(numeros) 

'''
Saída:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


# 5. Informar o primeiro e último elemento da lista
numeros[0]   # Saída: 1
numeros[-1]  # Saída: 20


# 6. Retornar o maior valor e o menor valor da lista
print(max(numeros))  # Saída: 1
print(min(numeros))  # Saída: 20


# 7. Apresentar a soma de todos os elementos da lista
print(sum(numeros))  # Saída: 210


# 8. Retornar qual o número de elementos que a lista possui
print(len(numeros))  # Saída: 20 


# 9. Criar duas sublistas, ao separar os números pares dos ímpares
numeros_pares = numeros[1::2]
print(numeros_pares)

numeros_impares = numeros[::2]
print(numeros_impares)

'''
Saída:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
'''


# 10. Imprimir a lista original de números na ordem decrescente
print(numeros[::-1])

'''
Saída:
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''


# 11. Transformar os números de 1 a 10 da lista original em algarismos romanos. Demais números devem permanecer inalterados.
numeros_mixados = numeros.copy()
numeros_mixados[:10] = ['I','II','III','IV','V','VI','VII','VIII','IX','X']
print(numeros_mixados)

'''
Saída:
['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

 
# 12. Retornando à lista original, inserir o número subsequente no final da lista
numeros.append(21)
print(numeros)

'''
Saída: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
'''

  
# 13. Agora inserir os próximos 4 números subsequentes ao fim da lista
numeros.extend([22, 23, 24, 25])
print(numeros)

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
'''


# 14. Emabralhar os números da lista usando o método random.shuffle()
import random
random.shuffle(numeros)
print(numeros) 

'''
Saída:
[9, 15, 6, 23, 4, 2, 24, 22, 19, 14, 16, 7, 18, 12, 17, 21, 1, 3, 11, 8, 13, 20, 25, 5, 10]
'''


# 15. Reordenar a lista usando o método sort()
numeros.sort()
print(numeros) 

'''
Saída:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
'''


# 16. Criar um algoritmo que responda se um número informado pelo usuário está presente na lista.
numero_verificado = int(input('Qual o número que deseja testar? '))
if(numero_verificado in numeros):
    print(f'Sim, o número {numero_verificado} está nesta lista')
else:
    print(f'Não, o número {numero_verificado} não está nesta lista')

'''
Saída:
> Qual o número que deseja testar? 16
  Sim, o número 16 está nesta lista

> Qual o número que deseja testar? 32
  Não, o número 32 não está nesta lista
'''


# 17. Dadas as três listas abaixo:
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [11,12,13,14,15]


# 17.1. Criar uma lista englobando as 3 listas acima
listaGeral = []  
listaGeral.append(lista1)
listaGeral.append(lista2)
listaGeral.append(lista3)
print(listaGeral)  

'''
Saída:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
'''

&nbsp;  

# 17.2. Agora indexar apenas a última lista
print(listaGeral[2])  

'''
Saída:
[11, 12, 13, 14, 15]
'''


&nbsp;  

# 17.3. Por fim, indexar o primeiro elemento desta última lista
print(listaGeral[2][0])  

'''
Saída:
11
'''