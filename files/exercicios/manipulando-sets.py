'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> > Acessando valores e fazendo manipulações em sets
'''

# 1. Declarando um set
nomes = {'Ana', 'Bárbara', 'Carlos', 'Paulo', 'Marcos', 'Rosana', 'Ana'}


# 2. Informar qual o número de elementos únicos no conjunto
print(len(nomes))  # Saída: 6


# 3. Verificar se os nomes Ana e Larissa constam no set
print(print('Ana' in nomes))     # Saída: True
print(print('Larissa' in nomes)) # Saída: False


# 4. Adicionar o nome Rogério ao set
nomes.add('Rogério')
print(nomes)

'''
Nesta saída:
{'Paulo', 'Rogério', 'Ana', 'Carlos', 'Rosana', 'Bárbara', 'Marcos'}
'''


# 5. Adicionar os nomes Luis e Giovana ao set
nomes.update(['Luis'], ['Giovana'])
print(nomes)

'''
Nesta saída:
{'Ana', 'Carlos', 'Rogério', 'Bárbara', 'Marcos', 'Luis', 'Rosana', 'Giovana', 'Paulo'}
'''


# 6. Excluir o nome Carlos do set
nomes.remove('Carlos')
print(nomes)

'''
Nesta saída:
{'Bárbara', 'Rogério', 'Luis', 'Marcos', 'Ana', 'Giovana', 'Paulo', 'Rosana'}
'''


# 7. Excluir o nome Sabrina do set, utilizando o método remove()
nomes.remove('Sabrina')
print(nomes)

'''
Saída:
Gerra erro, já que o nome Sabrina não está no set 
'''


# 8. Excluir o nome Sabrina do set, utilizando agora o método discard()
nomes.discard('Sabrina')
print(nomes)

'''
Saída:
{'Giovana', 'Ana', 'Marcos', 'Luis', 'Paulo', 'Rogério', 'Rosana', 'Bárbara'}

- Não houve alteração da lista, mas não gerou erro desta vez, mesmo o nome Sabrina não estando no set 
'''


# 9. Excluir todos os elementos do set
nomes.clear() 
print(nomes) 

'''
Saída:
set() 
'''