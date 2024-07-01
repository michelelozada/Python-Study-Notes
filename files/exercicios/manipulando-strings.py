'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Testando algumas manipulações de strings
> (através da indexação de strings, slicing e métodos de strings)
'''

# Declarando variáveis e atribuindo strings a elas
citacao = 'devemos julgar um homem mais pelas suas perguntas do que pelas respostas.'
autor = 'voltaire'
nome = 'françois marie-arouet'
oficio = 'ESCRITOR E FILÓSOFO FRANCÊS DO SÉCULO 18'


# Informar qual caractere corresponde ao índice 5 da string armazenada em autor
print(autor[5])
'''
i
'''


# Informar o que vai no intervalo abaixo defindo na string armazenada em nome
print(nome[0:14])  # Utilizada a operação de fatiamento aqui
'''
françois marie
'''


### Iterar a string em autor, de forma semelhante ao loop foreach de outras linguagens de programação
for letra in autor:
  print(letra)
'''
v
o
l
t
a
i
r
e
'''

# Iterar novamente a string em autor, mas agora através de indexação
for letra in range(0, len(autor)):
  print(autor[letra])
'''
v
o
l
t
a
i
r
e
'''


# Verificar qual o case da string armazenada em autor
print(autor.isupper())
print(autor.islower())
'''
# False
# True (composta portanto por caracteres minúsculos apenas)
'''


# Informar qual o número de ocorrências da letra 's' na string em citação e em que posição ela aparece pela primeira vez
print(citacao.count('s'))
print(citacao.index('s'))
'''
10 (10 ocorrencias da substring 's' nesta string)
6  (1ª ocorrência da substring 's' ocorre no índice 6)
'''


# Tornar maiúscula apenas a primeira letra da string em citação
citacao_nova = citacao.capitalize()
print(citacao_nova)
'''
Devemos julgar um homem mais pelas suas perguntas que pelas respostas.
'''


# Tornar maiúsculas todas as letras da string em autor
autor_novo = autor.upper()
print(autor_novo)
'''
VOLTAIRE
'''


# Tornar maiúsculas todas as primeiras letras das palavras da string em nome
nome_novo = nome.title()
print(nome_novo)
'''
François Marie-Arouet
'''

# Tornar minúsculas todas as letras da string oficio
oficio_novo = oficio.lower()
print(oficio_novo)
'''
escritor e filósofo francês do século 18
'''

# Substituir termos na string em ofício por: ensaísta, pensador e XVIII
oficio_atualizado = oficio_novo.replace('escritor','ensaísta')\
                               .replace('filósofo', 'pensador')\
                               .replace('18', 'XVIII')
print(oficio_atualizado)
'''
ensaísta e pensador francês do século XVIII
'''

# Imprimir a nova versão da citação com identificação do autor

print(f"\"{citacao_nova}\"")
print(f"{autor_novo} (pesudônimo de {nome_novo}, {oficio_atualizado})")
'''
"Devemos julgar um homem mais pelas suas perguntas do que pelas respostas."
VOLTAIRE (pesudônimo de François Marie-Arouet, ensaísta e pensador francês do século XVIII)
'''