'''
 *  Exercício: Média de notas
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada


As notas de um aluno estão armazenadas numa lista. Calcule a média destas notas.
'''

aluno='Enzo Marques'
Lista_notas=[6.5,7.5,8,9,7.5,9.5]
soma=0

for nota in Lista_notas:
    soma = soma + nota
media = soma/len(Lista_notas)
print(f'A média das notas obtidas pelo aluno {aluno} é: {media:.1f}')

# Saída => A média das notas obtidas pelo aluno Enzo Marques é: 8.0
