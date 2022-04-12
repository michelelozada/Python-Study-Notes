# 1 - Operador +
nome = 'Denzel' + ' ' + 'Washington'
profissao = 'ator e produtor norte-americano'
print(nome)  # Denzel Washington
print(nome + ', ' + profissao) # Denzel Washington, ator e produtor norte-americano


# 2 - Operador +=
s1 = 'hidro'
s2 = 'elétrica'
s1 += s2
print(s1) # hidroelétrica


# 3 - Operador *
frase = ('Vamos sentir saudades. Volte logo' + '!' * 3)
print(frase) # Vamos sentir saudades. Volte logo!!!


# 4 - Método str()
print('No ' + str(6) + 'º dia do evento, apenas ' + str(25) + '% dos convidados participaram dos ' + str(10) + ' seminários.')
# No 6º dia do evento, apenas 25% dos convidados participaram dos 10 seminários.


# 5- Método format()
name = 'Luísa Dias'
age = 18
grade = 9.5
print('Aluno(a): {}. Idade: {}. Nota: {}'.format(name,age,grade))
# Aluno(a): Luísa Dias. Idade: 18. Nota: 9.5

print(f'Aluno(a): {name}. Idade: {age}. Nota: {grade}') # Disponível a partir da versão 3.6 do Python!
# Aluno(a): Luísa Dias. Idade: 18. Nota: 9.5


# 3.2 - Método join()
bandasAnos80 = ['The Cure', 'The Smiths', 'New Order', 'Joy Division']
s = ' - '.join(bandasAnos80)
print(s)
