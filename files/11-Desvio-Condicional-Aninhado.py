'''
 *  Desvio condicional aninhado
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada


Escreva um algoritmo para servir de pré-atendimento para encomendas de clientes em uma panificadora.
Um menu deve oferecer as opções disponíveis para encomenda e qual a quantidade que o cliente deseja encomendar.
A saída deve apresentar o valor total a pagar e o produto encomendado.
'''

print('Panificadora Bela Vista - Auto-atendimento')
print('--------------------------------------------')
print('\nConfira abaixo nossas opções para hoje:')
print('1 - Broa de de aveia: R$ 7.50')
print('2 - Broa de centeio: R$ 7.00')
print('3 - Broa de fubá: R$ 6.50')
print('4 - Broa de milho: R$ 8.00')
print('5 - Broa de trigo integral: R$ 8.50')

op = int(input('\nDigite o número da opção escolhida: '))
encomenda = int(input('Quantas broas deste sabor deseja encomendar? '))

if (op == 1):
  produto = 'broa(s) de aveia'
  preco = 7.50
else:
  if (op == 2):
    produto = 'broa(s) de centeio'
    preco = 7.00
  else:
    if (op == 3):
      preco = 6.50
      produto = 'broa(s) de fubá'
    else:
      if (op == 4):
        produto = 'broa(s) de milho'
        preco = 8.00
      else:
        produto = 'broa(s) de trigo integral'
        preco = 8.50
print(
  f'\n> Você encomendou {encomenda} {produto}, sendo que o valor de seu pedido ficou em R$ {encomenda * preco:.2f}.')

'''
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