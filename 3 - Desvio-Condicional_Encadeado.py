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