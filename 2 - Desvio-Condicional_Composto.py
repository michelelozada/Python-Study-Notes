'''
O edital de um exame de proficiência em inglês definiu que, para ser aprovado, um candidato precisa obter a nota mínima
8.0 em cada uma das quatro provas a serem aplicadas. Sabendo disso, escreva um algoritmo que, depois de ler as notas obtidas,
informe se esse candidato foi aprovado no exame (ou não).
'''
print("Por favor, informe abaixo as notas obtidas pelo candidato.")
p1 = float(input('- Prova de Listening: Nota '))
p2 = float(input('- Prova de Speaking: Nota '))
p3 = float(input('- Prova de Reading and Use of English: Nota '))
p4 = float(input('- Prova de Writing: Nota '))

print('\nResultado final:')
if (p1>=8.0) and (p2>=8.0) and (p3>=8.0) and (p4>=8.0):
  print('O candidato obteve nota igual ou superior a 8.0 em todas as provas e, portanto, foi aprovado no exame de proficiência em inglês.')
else:
 print('O candidato obteve nota inferior a 8.0 em pelo menos uma das provas e, portanto, não foi aprovado no exame de proficiência em inglês.')
