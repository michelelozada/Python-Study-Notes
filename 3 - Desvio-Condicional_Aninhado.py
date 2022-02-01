'''
Escreva um algoritmo para servir de pré-atendimento para encomenda de clientes em uma panificadora.
Um menu deve oferecer as opções disponíveis para encomenda e qual a quantidade que o cliente deseja encomendar.
A saída deve apresentar o valor total a pagar de tal encomenda.
'''


print('Panificadora Bela Vista - Auto-atendimento')
print('--------------------------------------------')
print('\nConfira abaixo nossas opções para hoje:')
print('1 - Broa de de aveia: R$ 7.50')
print('2 - Broa de centeio: R$ 7.00')
print('3 - Broa de fubá: R$ 6.50')
print('4 - Broa de milho: R$ 8.00')
print('5 - Broa de trigo integral: R$ 8.50')

op = int(input('\nDigite o número da opção escolhida: ' ))
encomenda = int(input('Quantas broas deste sabor deseja encomendar? '))

if(op==1):
  total = encomenda*7.50
  print(f'\n> Você encomendou {encomenda} broa(s) de aveia, sendo que o valor de seu pedido ficou em R$ {total:.2f}')
else:
  if(op==2):
    total = encomenda*7.00
    print(f'\n> Você encomendou {encomenda} broa(s) de centeio, sendo que o valor de seu pedido ficou em R$ {total:.2f}')
  else:
    if(op==3):
      total = encomenda*6.50
      print(f'\n> Você encomendou {encomenda} broa(s) de fubá, sendo que o valor de seu pedido ficou em R$ {total:.2f}')
    else:
      if(op==4):
        total = encomenda*8.00
        print(f'\n> Você encomendou {encomenda} broa(s) de milho, sendo que o valor de seu pedido ficou em R$ {total:.2f}')
      else:
        if(op==5):
          total = encomenda*8.50
          print(f'\n> Você encomendou {encomenda} broa(s) de trigo integral, sendo que o valor de seu pedido ficou em R$ {total:.2f} |')
        else:
          print('> Esta opção é inválida.')

  '''
A saída gerada: 

Panificadora Bela Vista - Auto-atendimento
--------------------------------------------

Confira abaixo nossas opções para hoje:
1 - Broa de de aveia: R$ 7.50
2 - Broa de centeio: R$ 7.00
3 - Broa de fubá: R$ 6.50
4 - Broa de milho: R$ 8.00
5 - Broa de trigo integral: R$ 8.50

Digite o número da opção escolhida: 3
Quantas broas deste sabor deseja encomendar? 4

> Você encomendou 4 broa(s) de fubá, sendo que o valor de seu pedido ficou em R$ 26.00
  '''