'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> > Acessando valores e fazendo manipulações em strings
'''


# 1. Declarando variáveis e atribuindo strings a elas
citacao = 'devemos julgar um homem mais pelas suas perguntas do que pelas respostas.'
autor = 'voltaire'
nome = 'françois marie-arouet'
oficio = 'ESCRITOR E FILÓSOFO FRANCÊS DO SÉCULO 18'


# 2. Informar qual caractere corresponde ao índice 5 da string armazenada em autor
print(autor[5])
    
'''
Saída: 
i
'''


# 3. Informar o que vai no intervalo abaixo defindo na string armazenada em nome
print(nome[0:14])  # Utilizada a operação de fatiamento aqui
    
'''
Saída: 
françois marie
'''


# 4. Iterar a string em autor, de forma semelhante ao loop foreach de outras linguagens de programação
for letra in autor:
  print(letra)
  
'''
Saída:
v
o
l
t
a
i
r
e
'''

# 5. Iterar novamente a string em autor, mas agora através de indexação
for letra in range(0, len(autor)):
  print(autor[letra])
  
'''
Saída:
v
o
l
t
a
i
r
e
'''


# 6. Verificar qual o case da string armazenada em autor
print(autor.isupper())
print(autor.islower())
    
'''
Saída:
# False
# True (composta portanto por caracteres minúsculos apenas)
'''


# 7. Informar qual o número de ocorrências da letra 's' na string em citação e em que posição ela aparece pela primeira vez
print(citacao.count('s'))
print(citacao.index('s'))
    
'''
Saída:
10 (10 ocorrencias da substring 's' nesta string)
6  (1ª ocorrência da substring 's' ocorre no índice 6)
'''


# 8. Tornar maiúscula apenas a primeira letra da string em citação
citacao_nova = citacao.capitalize()
print(citacao_nova)
    
'''
Saída: 
Devemos julgar um homem mais pelas suas perguntas que pelas respostas.
'''


# 9. Tornar maiúsculas todas as letras da string em autor
autor_novo = autor.upper()
print(autor_novo)
    
'''
Saída: 
VOLTAIRE
'''


# 10. Tornar maiúsculas todas as primeiras letras das palavras da string em nome
nome_novo = nome.title()
print(nome_novo)
    
'''
Saída: 
François Marie-Arouet
'''

# 11. Tornar minúsculas todas as letras da string oficio
oficio_novo = oficio.lower()
print(oficio_novo)
'''
Saída: 
escritor e filósofo francês do século 18
'''

# 12. Substituir termos na string em ofício por: ensaísta, pensador e XVIII
oficio_atualizado = oficio_novo.replace('escritor','ensaísta')\
                               .replace('filósofo', 'pensador')\
                               .replace('18', 'XVIII')
print(oficio_atualizado)
    
'''
Saída: 
ensaísta e pensador francês do século XVIII
'''

# 13. Imprimir a nova versão da citação com identificação do autor

print(f"\"{citacao_nova}\"")
print(f"{autor_novo} (pesudônimo de {nome_novo}, {oficio_atualizado})")
    
'''
Saída:
"Devemos julgar um homem mais pelas suas perguntas do que pelas respostas."
VOLTAIRE (pesudônimo de François Marie-Arouet, ensaísta e pensador francês do século XVIII)
'''