'''
 *  Tipos de dados
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada
'''

# Retorne quais os tipos de dados das variáveis apresentadas abaixo:

a = 7
print(a, type(a))
# Retorna: 7 <class 'int'>


b = 10.5
print(b, type(b))
# 10.5 <class 'float'>


c = 3 + 4j
print(c, type(c))
# (3+4j) <class 'complex'>


d = 'Tipos de variáveis utilizadas em Python!'
print(d, type(d))
# Tipos de variáveis utilizadas em Python! <class 'str'>


e1 = True
e2 = False
print(e1, type(e1), ' - ', e2, type(e2))
# True <class 'bool'>  -  False <class 'bool'>


f = ['a', 2, 'c', 4, 5]
print(f, type(f))
# ['a', 2, 'c', 4, 5] <class 'list'>


g = ('Paraná', 'Santa Catarina','Rio Grande do Sul')
print(g, type(g))
# ('Paraná', 'Santa Catarina', 'Rio Grande do Sul') <class 'tuple'>


h = {'Nome': 'Davi', "Idade": 18, 'Profissão':'Programador'}
print(h, type(h))
# {'Nome': 'Davi', 'Idade': 18, 'Profissão': 'Programador'} <class 'dict'>