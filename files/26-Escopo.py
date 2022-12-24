'''
 *  Escopo
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada
 '''

# 1 - Escopo global vs. escopo local
x = 'global' # variável de escopo global
def minhaFuncao():
    x = 'local' # variável de escopo local
    print(x)

# Evocando a função
minhaFuncao()
# Print da variável x
print(x)

''' Output:
local
global
'''


# 2 - Utlização da global keyword
x = 'global'
def minhaFuncao():
    global x
    x = 'local'
    print(x)

minhaFuncao()
print(x)
''' Output:
local 
local
'''