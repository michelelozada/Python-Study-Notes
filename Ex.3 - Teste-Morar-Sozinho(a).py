"""
O que segue abaixo é uma simulação que tentei criar destes testes aleatórios que encontramos pela internet afora.
No caso, trata-se de um teste para descobrir se o(a) usuário(a) está preparado(a) para morar sozinho(a).
Meu foco aqui era treinar a utilização de estruturas while True com os desvios incondicionais break e continue.
"""

def msg_erro():
  print('\n>> Ops, a resposta digitada foi inválida. Por favor, responda novamente para continuar o teste...\n')

def progresso():
  print('\n>> Seu resultado até aqui:',soma,'pontos')

while True:
  print('\nEntão quer dizer que você quer deixar a casa dos pais e ter o seu próprio cantinho, hein? ;)')
  print('Faça o teste abaixo e descubra se você já está apto a encarar os desafios de ter um lar para chamar de seu!')

  soma = 0

  print('\nA) Desafios do dia-a-dia:')
  while True:
    res = input('Pergunta 1 de 10 - Você consegue se virar bem na cozinha (para além do macarrão instantâneo)? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  while True:
    res = input('Pergunta 2 de 10 - Você saberia limpar sua casa e mantê-la organizada? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma +=  1
    progresso()
    break

  print('\nB) Família e amigos:')
  while True:
    res = input('Pergunta 3 de 10 - Você se considera apegado à sua família? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 0
    elif(res.lower() == 'n'):
      soma -= 1
    break

  while True:
    res = input('Pergunta 4 de 10 - Você tem muitos amigos? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  while True:
    res = input('Pergunta 5 de 10 - Você lida bem com a solidão? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    progresso()
    break

  print('\nC) Finanças:')
  while True:
    res = input('Pergunta 6 de 10 - Hoje você conseguiria se manter apenas com a sua renda atual (mesmo dividindo apartamento com alguém)? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  while True:
    res = input('Pergunta 7 de 10 - Você considera que administra bem o seu dinheiro? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  while True:
    res = input('Pergunta 8 de 10 - Você mantém uma reserva de emergência? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 0
    progresso()
    break

  print('\nD) Suas características pessoais:')

  while True:
    res = input('Pergunta 9 de 10 - Você lida bem com imprevistos? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  while True:
    res = input('Pergunta 10 de 10 - Você se considera uma pessoa responsável? (s/n) ')
    if(res.lower() != 's' and res.lower() != 'n'):
      msg_erro()
      continue
    elif(res.lower() == 's'):
      soma += 2
    elif(res.lower() == 'n'):
      soma += 1
    break

  print('\n>> Resultado final do teste: ',end='')
  if(soma <= 10):
    print(f'Você obteve {soma} pontos\n Bem, sua pontuação demonstra que possivelmente ainda não chegou a hora de você assumir uma casa ou apê só seu...')
  elif(soma > 10 and soma <= 16):
    print(f'{soma} pontos.\nSua pontuação demonstra que você tem muita vontade de morar sozinho, mas ainda precisa se preparar um pouquinho mais - talvez emocional ou financeiramente - para não ter problemas ao encarar este desafio.')
  else:
    print(f'{soma} pontos.\nParabéns, sua pontuação demonstra que você tem vários requisitos para logo assumir a sua casa!')

  restart = input('\n(Para encerrar o programa, digite S. Para refazer o teste, digite qualquer outra tecla) ')
  if(restart.lower() == 'S'):
    continue
  else:
    print('Programa encerrado...')
    break

"""
Então quer dizer que você quer deixar a casa dos pais e ter o seu próprio cantinho, hein? ;)
Faça o teste abaixo e descubra se você já está apto a encarar os desafios de ter um lar para chamar de seu!

A) Desafios do dia-a-dia:
Pergunta 1 de 10 - Você consegue se virar bem na cozinha (para além do macarrão instantâneo)? (s/n) s
Pergunta 2 de 10 - Você saberia limpar sua casa e mantê-la organizada? (s/n) s

>> Seu resultado até aqui: 4 pontos

B) Família e amigos:
Pergunta 3 de 10 - Você se considera apegado à sua família? (s/n) s
Pergunta 4 de 10 - Você tem muitos amigos? (s/n) s
Pergunta 5 de 10 - Você lida bem com a solidão? (s/n) n

>> Seu resultado até aqui: 7 pontos

C) Finanças:
Pergunta 6 de 10 - Hoje você conseguiria se manter apenas com a sua renda atual (mesmo dividindo apartamento com alguém)? (s/n) n
Pergunta 7 de 10 - Você considera que administra bem o seu dinheiro? (s/n) s
Pergunta 8 de 10 - Você mantém uma reserva de emergência? (s/n) n

>> Seu resultado até aqui: 10 pontos

D) Suas características pessoais:
Pergunta 9 de 10 - Você lida bem com imprevistos? (s/n) n
Pergunta 10 de 10 - Você se considera uma pessoa responsável? (s/n) s

>> Resultado final do teste: 13 pontos.
Sua pontuação demonstra que você tem muita vontade de morar sozinho, mas ainda precisa se preparar um pouquinho mais - talvez emocional ou financeiramente - para não ter problemas ao encarar este desafio.

(Para encerrar o programa, digite S. Para refazer o teste, digite qualquer outra tecla) n
Programa encerrado...
"""