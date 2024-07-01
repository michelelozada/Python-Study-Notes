'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício de um trabalho da faculdade de ADS - 2021

Crie um programa que permita a pré-incrição de alunos para um curso de Python em uma escola.

Requisitos deste programa:
  - Solicitar ao usuário a entrada de nome, e-mail e telefone
  - Gerar um voucher para cada inscrição realizada
  - Exibir um menu de opções para o usuário, com as seguintes características:
    - Opção 0 para encerrar o programa
    - Opção 1 para inscrição
      (ao selecionar essa opção, o usuário deverá ser capaz de entrar com os dados da inscrição. O código da inscrição
      deve ser preenchido automaticamente pelo sistema e o usuário não deve ter a opção de alterar esse código)
    - Opção 2 para visualização de inscrições cadastradas
      (ao selecionar essa opção, o programa deverá imprimir na tela, para cada inscrição, todos os dados cadastrados.
      Caso nenhuma inscrição tenha sido cadastrada ao selecionar essa opção, o programa deverá exibir a mensagem “Não
      há nenhuma inscrição cadastrada”).
    - Caso o usuário digite uma opção inválida, o programa deve fornecer este feedback.
'''


import random

# Inicializando a semente do gerador de números aleatórios
random.seed(100)

def realizar_inscricao(nome, email, telefone):
  numero_inscricao = random.randint(100, 400)
  # Dicionário usado para armazenar detalhes de inscrições individuais
  inscricao = {
    'Número da inscrição': numero_inscricao,
    'Nome': nome,
    'E-mail': email,
    'Telefone': telefone,
    'Curso': 'Python'
  }
  return inscricao

def exibir_inscricoes(lista):
  for inscricao in lista:
    for chave, valor in inscricao.items():
      print(f"{chave}: {valor}")

def exibir_menu():
  print('\nAULAS GRATUITAS DE PYTHON')
  print('\n>> Menu de opções:')
  print('1 - Realizar inscrição e gerar voucher')
  print('2 - Consultar inscrição(ões) cadastrada(s)')
  print('3 - Encerrar o programa\n')


# Início do programa principal

# Lista a ser usada para armazenar todos os dicionários de inscrições
lista_inscricoes = []

while True:
  exibir_menu()
  try:
    opcao = int(input(">> Deseja acessar qual número de opção? "))
    if(opcao == 1):
      print('\n>> Realizar sua inscrição:')
      nome = input("Qual é o seu nome? ")
      email = input("Qual é seu email? ")
      telefone = input('Qual é seu telefone? ')
      # incricao é um dicionário com dados de cada aluno
      inscricao = realizar_inscricao(nome, email, telefone)
      # a cada novo cadastrado, um dicionário inscricao é acionado à lista abaixo
      lista_inscricoes.append(inscricao)
      print(f"\nFeedback: A sua inscrição de {nome} foi realizada com sucesso!")
    elif(opcao == 2):
      print('\n>> Consultar inscrição(ões) cadastrada(s):')
      # Verificando se a lista contém algum elemento
      if lista_inscricoes:
        exibir_inscricoes(lista_inscricoes)
      else:
        print(">> Não há nenhuma inscrição cadastrada.")
    elif (opcao == 3):
      print('\n>> Encerrar o programa:')
      print('Você escolheu encerrar o programa.')
      break
    else:
      print("\n>> Essa opção não existe no menu. Por gentileza, tente novamente.\n")
  except ValueError:
    print("\n>> Esta opção não é válida. Por gentileza, tente novamente.\n")