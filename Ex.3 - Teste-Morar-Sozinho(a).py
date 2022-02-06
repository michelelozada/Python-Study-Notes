'''
O que segue abaixo é só uma simulação que criei destes testes aleatórios que encontramos pela internet.
No caso, trata-se de um teste para descobrir se o(a) usuário(A) está preparado(a) para morar sozinho(a).
Meu foco aqui era treinar a utilização de estruturas while True com os desvios incondicionais (break and continue).
'''

def msg_erro():
  print('\n>> Ops, a resposta digitada foi inválida. Por favor, responda novamente para continuar o teste...\n')

def progresso():
  print('\n>> Seu resultado até aqui:',soma, 'pontos')

print('Então quer dizer que você quer deixar a casa dos pais e ter o seu próprio cantinho, hein! ')
print('Faça o teste abaixo e descubra se você já está apto a encarar os desafios de ter um lar para chamar de seu! :)')

soma = 0

print('\nA) Desafios do dia-a-dia:')
while True:
  q1 = input('Pergunta 1 de 10 - Você consegue se virar bem na cozinha (para além do macarrão instantâneo)? (s/n) ')
  if(q1.lower() != 's' and q1.lower() != 'n'):
    msg_erro()
    continue
  elif(q1.lower() == 's'):
    soma += 2
  elif(q1.lower() == 'n'):
    soma += 1
  break

while True:
  q2 = input('Pergunta 2 de 10 - Você saberia limpar sua casa e mantê-la organizada? (s/n) ')
  if(q2.lower() != 's' and q2.lower() != 'n'):
    msg_erro()
    continue
  elif(q2.lower() == 's'):
    soma += 2
  elif(q2.lower() == 'n'):
    soma +=  1
  progresso()
  break

print('\nB) Família e amigos:')
while True:
  q3 = input('Pergunta 3 de 10 - Você se considera apegado à sua família? (s/n) ')
  if(q3.lower() != 's' and q3.lower() != 'n'):
    msg_erro()
    continue
  elif(q3.lower() == 's'):
    soma += 0
  elif(q3.lower() == 'n'):
    soma -= 1
  break

while True:
  q4 = input('Pergunta 4 de 10 - Você tem muitos amigos? (s/n) ')
  if(q4.lower() != 's' and q4.lower() != 'n'):
    msg_erro()
    continue
  elif(q4.lower() == 's'):
    soma += 2
  elif(q4.lower() == 'n'):
    soma += 1
  break

while True:
  q5 = input('Pergunta 5 de 10 - Você lida bem com a solidão? (s/n) ')
  if(q5.lower() != 's' and q5.lower() != 'n'):
    msg_erro()
    continue
  elif(q5.lower() == 's'):
    soma += 2
  elif(q5.lower() == 'n'):
    soma += 1
  progresso()
  break

print('\nC) Finanças:')
while True:
  q6 = input('Pergunta 6 de 10 - Hoje você conseguiria se manter apenas com a sua renda atual (mesmo dividindo apartamento com alguém)? (s/n) ')
  if(q6.lower() != 's' and q6.lower() != 'n'):
    msg_erro()
    continue
  elif(q6.lower() == 's'):
    soma += 2
  elif(q6.lower() == 'n'):
    soma += 1
  break

while True:
  q7 = input('Pergunta 7 de 10 - Você considera que administra bem o seu dinheiro? (s/n) ')
  if(q7.lower() != 's' and q7.lower() != 'n'):
    msg_erro()
    continue
  elif(q7.lower() == 's'):
    soma += 2
  elif(q7.lower() == 'n'):
    soma += 1
  break

while True:
  q8 = input('Pergunta 8 de 10 - Você mantém uma reserva de emergência? (s/n) ')
  if(q8.lower() != 's' and q8.lower() != 'n'):
    msg_erro()
    continue
  elif(q8.lower() == 's'):
    soma += 2
  elif(q8.lower() == 'n'):
    soma += 0
  progresso()
  break

print('\nD) Suas características pessoais:')

while True:
  q9 = input('Pergunta 9 de 10 - Você lida bem com imprevistos? (s/n) ')
  if(q9.lower() != 's' and q9.lower() != 'n'):
    msg_erro()
    continue
  elif(q9.lower() == 's'):
    soma += 2
  elif(q9.lower() == 'n'):
    soma += 1
  break

while True:
  q10 = input('Pergunta 10 de 10 - Você se considera uma pessoa responsável? (s/n) ')
  if(q10.lower() != 's' and q10.lower() != 'n'):
    msg_erro()
    continue
  elif(q10.lower() == 's'):
    soma += 2
  elif(q10.lower() == 'n'):
    soma += 1
  break

print('\n>> Resultado final do teste: ',end='')
if(soma <= 10):
  print(f'Você obteve {soma} pontos\n Bem, sua pontuação demonstra que possivelmente ainda não chegou a hora de você assumir uma casa ou apê só seu...')
elif(soma > 10 and soma <= 16):
  print(f'{soma} pontos.\nSua pontuação demonstra que você está com muita vontade de morar sozinho, mas possivelmente ainda precisa adquirir um pouco mais de autonomia (seja emocional ou financeira) para não ter problemas ao encarar este desafio.')
elif (soma >= 17):
  print(f'{soma} pontos.\nParabéns, sua pontuação demonstra que você tem vários requisitos para logo assumir a sua casa!')


  '''
Então quer dizer que você quer deixar a casa dos pais e ter o seu próprio cantinho, hein! 
Faça o teste abaixo e descubra se você já está apto a encarar os desafios de ter um lar para chamar de seu! :)

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
Pergunta 9 de 10 - Você lida bem com imprevistos? (s/n) s
Pergunta 10 de 10 - Você se considera uma pessoa responsável? (s/n) s

>> Resultado final do teste: 14 pontos.
Sua pontuação demonstra que você está com muita vontade de morar sozinho, mas possivelmente ainda precisa adquirir um pouco mais de autonomia (seja emocional ou financeira) para não ter problemas ao encarar este desafio.
  '''