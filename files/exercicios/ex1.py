'''
De um trabalho da faculdade de ADS - 2021 

+------------------------+--------------------+
|         Ensino         |    Faixa etária    |
+------------------------+--------------------+
| Educação Infantil      | 1 a 5 anos         |
| Ensino Fundamental I   | 6 a 10 anos        |
| Ensino Fundamental II  | 11 a 14 anos       |
| Ensino Médio           | a partir 15 anos   |
+------------------------+--------------------+

De acordo com a seguinte classificação acima, crie um programa em Python que solicite nome e idade de um aluno e retorne qual a sua classificação em relação à etapa de ensino esperada. Além disso, o usuário deve escolher se deseja encerrar o programa ou não.
'''


def solicita_nome_aluno():
  aluno = input("Qual o nome do(a) aluno(a)? ")
  while not aluno.strip():
    print('<> Feedback: O  campo nome do aluno não pode estar vazio.\n')
    aluno = input("Qual o nome do(a) aluno(a)? ")
  return aluno

while True:
  print("\nClassificador de Etapa de Ensino de Aluno")
  aluno = solicita_nome_aluno()
  try:
    idade = int(input(f"Qual a idade de {aluno}? "))
    while idade <= 0 or idade > 100:
      print('<> Feedback: Esta idade é inválida para esta consulta.\n')
      idade = int(input(f"Qual a idade de {aluno}? "))
    if idade <= 5:
      etapa = 'Educação Infantil'
    elif idade <= 10:
      etapa = 'Educação Fundamental I'
    elif idade <= 14:
      etapa = 'Educação Fundamental II'
    else:
      etapa ='Ensino Médio'
    print(f"<> Resultado da consulta: {aluno} tem {idade} ano(s) e está, portanto, enquadrado(a) na seguinte etapa de ensino: {etapa}.")
  except ValueError:
    print('<> Feedback: Valor inválido. Por gentileza, comece novamente.\n')
    continue

  sair = input("\n>> Deseja sair do programa? (Digite S para sair/ Outra letra para continuar) ").lower()
  if(sair == 's'):
    print("\n>> <> Feedback: Encerrando o programa... Programa encerrado.")
    break