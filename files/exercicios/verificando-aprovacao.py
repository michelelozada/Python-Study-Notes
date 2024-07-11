'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício criado para praticar conceitos aprendidos

O edital de um exame de proficiência em inglês definiu que, para ser aprovado, um candidato precisa obter nota mínima
8,0 em cada uma das quatro provas a serem aplicadas. Sabendo disso, escreva um algoritmo que, depois de ler as notas
obtidas, informe se esse candidato foi aprovado no exame (ou não).  
'''


candidato = input('Por favor, informe o nome do aluno: ')

provas = [
    'Listening',
    'Speaking',
    'Reading and Use of English',
    'Writing'
]

print(f'Informe abaixo as notas obtidas pelo candidato {candidato}.')
notas = [float(input(f'- Prova de {prova}: ')) for prova in provas]

if all(nota >= 8.0 for nota in notas):
    escala = 'igual ou superior'
    prova = 'todas as provas'
    status = 'aprovado'

else:
    escala = 'inferior'
    prova = 'pelo menos uma das provas'
    status = 'reprovado'

print(f'\n>> Candidato {candidato} obteve nota {escala} a 8,0 em {prova} e está, portanto, {status} no exame de proficiência em inglês.')