'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício criado para praticar conceitos aprendidos

Crie um programa que simule a solicitação de um nome de usuário (AnaMaria) e senha (rh123) para acessar um sistema. Caso
estas entradas sejam digitadas incorretamente, isso deve ser reportado ao usuário; sendo que, após 3 entradas incorretas para
cada solicitação, o programa deve ser encerrado.
'''

MAX_TENTATIVAS = 3

def solicitar_senha():
  tentativas_restantes = MAX_TENTATIVAS
  while tentativas_restantes > 0:
    senha = input(f'\n(Tentativa {MAX_TENTATIVAS - tentativas_restantes + 1} de MAX_TENTATIVAS) Agora informe a sua senha: ')
    if senha == 'rh123':
      return senha
    else:
      print(f'> Feedback: A senha digitada está incorreta. Tentativas restanes: {tentativas_restantes}\n')
      tentativas_restantes -= 1
  print('> Feedback: Programa encerrado (motivo: três entradas de senha incorrrtas')


def solicitar_credenciais():
  tentativas_restantes = MAX_TENTATIVAS
  while tentativas_restantes > 0:
    usuario = input(f'(Tentativa {MAX_TENTATIVAS - tentativas_restantes + 1} de MAX_TENTATIVAS) Informe seu nome de usuário: ')
    if usuario == 'AnaMaria':
      senha = solicitar_senha()
      print('> Feedback: Acesso concedido. Seja bem-vindo(a) ao sistema!')
      return
    else:
      print(f'> Feedback: O nome de usuário {usuario} está incorreto. Tentativas restanes: {tentativas_restantes}\n')
      tentativas_restantes -= 1
  print('> Feedback: Programa encerrado (motivo: três entradas de nome de usuário incorretas)')

solicitar_credenciais()