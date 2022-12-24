'''
 *  Biblioteca random
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada
 '''

# 1 - Dados os números abaixo, retorne uma lista com três números aleatórios da mesma:
import random
lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numeros_aleatorios1 = random.sample(lista1, 3)
print(numeros_aleatorios1)
# Exemplo de um dos outputs gerados: [40, 100, 10]


# 2 - Dentro do intervalo de 1 a 50 (ambos inclusos), retorne uma lista com 5 números aleatórios:
lista2 = random.sample(range(1,50),5)
print(lista2)
# Exemplo de um dos outputs gerados: [39, 9, 22, 41, 27]


'''
3 - Escreva um algoritmo que, mediante sorteio, defina qual o a escla de fins  de semana de folga para cada um dos 10 
colaboradores de uma empresa. 
'''
def print_msg():
    print(f'Semana #{cont} - Fim de semana de folga para ' + colaborador + '.')
cont = 0
colaboradores = ['Ana Carolina', 'Enzo', 'Carla', 'Marcos', 'Morgana', 'Paulo', 'Vanessa', 'Lucas', 'Rodrigo', 'Alana']
print(f'- ESCALA DE FOLGAS DE COLABORADORES- EMPRESA XPTO -')
while (cont <10):
    cont += 1
    colaborador = random.choice(colaboradores)
    print_msg()
    colaboradores.remove(colaborador)

''' Exemplo de um dos outputs gerados:
Semana #1 - Fim de semana de folga para Morgana.
Semana #2 - Fim de semana de folga para Lucas.
Semana #3 - Fim de semana de folga para Vanessa.
Semana #4 - Fim de semana de folga para Enzo.
Semana #5 - Fim de semana de folga para Rodrigo.
Semana #6 - Fim de semana de folga para Marcos.
Semana #7 - Fim de semana de folga para Carla.
Semana #8 - Fim de semana de folga para Paulo.
Semana #9 - Fim de semana de folga para Alana.
Semana #10 - Fim de semana de folga para Ana Carolina.
'''