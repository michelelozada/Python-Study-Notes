'''
 *  Conjuntos (sets)
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada
 '''


# 1. Declarando um set
conjunto = set()
conjunto = set([1,2,3,6,5])
print(conjunto) # Retorna: {1, 2, 3, 5, 6}
# ou
conjunto = {1,2,3,6,5}
print(conjunto) # {1, 2, 3, 5, 6}


# 2. Um set é uma coleção de elementos únicos, repare: 
conjunto2 = {1,2,2,2,1}
print(conjunto2) # {1, 2}


# 3. Num set a ordem dos elementos é irrelevante:
print({1,2,3} == {2,1,3}) # True
print ({3,3,2,2,1} == {1,2,3}) # True


# 4. Determinando o tamanho de um set:
setNomes = {'Ana','Bárbara','Luisa','Antônia','Érica','Márcia'}
print(len(setNomes)) #6


# 5. Verificando se um elemento consta em um set:
print('Ana' in setNomes) # True
print('Larissa' in setNomes) # False


# 6. Adicionando elementos a um set:
set1 = {'a','b','c'}
set1.add('d') # para adição de apenas um elemento
print(set1) # {'a', 'b', 'c', 'd'}

set1.update(['e','f','g']) # para adição de mais elementos
print(set1) # {'e', 'f', 'a', 'g', 'b', 'c','d'}


# 7. Excluindo elementos de um set
set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.remove('c') # definindo o elemento a ser excluido. Necessário que elemento pertença ao set para evitar erro.
print(set) # {'f', 'e', 'a', 'd', 'b'}
# ou
set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.discard('r') # fará o mesmo que remove(), mas sem gerar erro em caso de elemento fora do set
print(set) # {'a', 'c', 'f', 'e', 'd', 'b'}  -> repare que não houve alteração (nem exceção!)
#ou
set= {'a', 'b', 'c', 'd', 'e', 'f'}
excluido = set.pop() # sem definir o elemento a ser excluido
print(excluido) # a
print(set) # {'c', 'b', 'f', 'd', 'e'}
# ou
set= {'a', 'b', 'c', 'd', 'e', 'f'}
set.clear() # exclusão de todos os elementos
print(set) # set()


# 8. Convertendo uma lista em um conjunto/set
nomes = ['Huguinho','Luisinho','Zezinho']
listaNomes = set(nomes)
print(listaNomes) # {'Huguinho', 'Zezinho', 'Luisinho'}


# 9. Convertendo um conjunto em um lista
nomes = {'Margarida', 'Minnie','Mickey'}
lista = list(nomes)
print(lista) # ['Mickey', 'Minnie', 'Margarida']


# 10. Convertendo um conjunto em uma tupla
novoSet = {'Luciano','Paulo','Marcos','Antônio','Eduardo'}
tupla = tuple(novoSet)
print(tupla)  # ('Marcos', 'Antônio', 'Eduardo', 'Paulo', 'Luciano')