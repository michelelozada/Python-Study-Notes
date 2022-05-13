'''
 *  Operadores e expressões lógicas
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada
'''


# 1. Conectivo lógico 'AND'
# Tem seu valor lágico verdadeiro somente quando 2 preposições forem verdadeiras

# 1.1. Representação da tabela verdade para o operador AND:
print(True and True) # Retorna: True
print(True and False) # False
print(False and True) # False
print(False and False) # False


# 2. Conectivo lógico 'OR'
# Tem seu valor lágico verdadeiro quando ao menos uma das preposições for verdadeira

# 2.1. Representação da tabela verdade para o operador OR:
print(True or True) # Retorna: True
print(True or False) # True
print(False or True) # True
print(False or False) # False


# 3. Conectivo lógico 'NOT'
# Tem o efeito de inverter o valor lógico da proposição original

# 3.1. Representação da tabela verdade para o operador NOT:
print(not True) # False
print(not False) # True


# 4. Expressões lógicas diversas:
print((3 < 2) and (2 == 2)) # Retorna: False
print(1 + 1 == 2 and len("bola") == 4) # True
print(1 + 1 > 2 and 4 != 5) # False
print((True or False) and True) # True
print((True and False) and True) # False

print((2 > 1) or (3 < 7))  # Retorna: True
print(1 + 1 == 2 or len("bola") == 4) #True
print(1 + 1 != 2 or len("bola") == 4) # True
print((True or False) or True) # True
print((True and False) or True) # True

print(not (3 > 2)) # False
print(not (7 < 5)) # True
print(not (4 != 2) and (3 < 6)) # False
print(not True or False) # False
print(not True or True) # True
print(not False or True) # True
print(not True and False) # False