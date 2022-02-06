'''
Para este exercício, tentei escrever um algoritmo que simulasse para um consumidor quais os gastos junto a uma companhia
fornecedora de água, levando em conta o seu perfil e consumo mensal estimado. Eu me baseei nos dados de uma tabela real
que encontrei na internet com as seguintes tarifas em vigor a certa época junto à CASAN (Companhia Catarinense de Água e
Saneamento).

Faixa consumo    Residencial   Resid. social  Comercial   Industrial
--------------------------------------------------------------------
1m³ a 10m³       R$  1,96      R$  0,37       R$  4,34    R$  4,34
11m³ a 25m³      R$  9,11      R$  2,61       R$ 12,18    R$ 12,18
26m³ a 50m³      R$ 12,18      R$ 12,18       R$ 12,18    R$ 12,18
Acima de 50m³    R$ 15,32      R$ 15,32       R$ 15,32    R$ 12,18
(*) Taxa fixa    R$ 29,49      R$  5,50       R$ 29,49    R$ 29,49
'''

while True:
  try:
    print('SIMULADOR DE TARIFA, DE ACORDO COM O CONSUMO DE ÁGUA\n')
    print('(A) Definindo sua categoria de consumo:')
    print('1 - Residencial')
    print('2 - Residencial Social')
    print('3 - Comercial')
    print('4 - Industrial')

    op = int(input('Em qual categoria seu imóvel se enquadra? Selecione uma das opções acima: '))
    if (op == 1) or (op == 2) or (op == 3) or (op == 4):
      print('\n(B) Definindo o consumo de água:')
      consumo = float(input('Informe seu consumo estimado no mês (em m³): '))
      while True:
        if(op == 1):
          categoria = 'residencial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Ainda que não haja consumo de água, o valor da tarifa fixa para a categoria {categoria} será de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              faixa = 1.96
            elif(consumo >= 11 and consumo <=25):
              faixa = 9.11
            elif(consumo >= 26 and consumo <=50):
              faixa = 12.18
            else:
              faixa = 15.32

        elif(op == 2):
          categoria = 'residencial social'
          fixo = 5.50
          if (consumo == 0):
            print(f'\n> InAinda que não haja consumo de água, o valor da tarifa fixa para a categoria {categoria} será de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              faixa = 0.37
            elif(consumo >= 11 and consumo <=25):
              faixa = 2.61
            elif(consumo >= 26 and consumo <=50):
              faixa = 12.18
            else:
              faixa = 15.32

        elif(op == 3):
          categoria = 'comercial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Ainda que não haja consumo de água, o valor da tarifa fixa para a categoria {categoria} será de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              faixa = 4.34
            elif(consumo >= 11 and consumo <=50):
              faixa = 12.18
            else:
              faixa = 15.32

        elif(op == 4):
          categoria = 'industrial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Ainda que não haja consumo de água, o valor da tarifa fixa para a categoria {categoria} será de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              faixa = 4.34
            else:
              faixa = 12.18
        print('\n(C) Resultado da simulação:')
        print(f'Para consumo de {consumo:.2f} m³ de água (referente à categoria {categoria}), o valor estimado a pagar será de R$ {consumo * faixa + fixo:.2f}.')
        break
      break
    else:
      print('\n> Esta opção é inexistente no menu. Por gentileza, tente novamente.\n')
      continue
  except ValueError:
    print('\n> O valor digitado precisa ser um número. Por gentileza, tente novamente.\n')
    continue

'''
SIMULADOR DE TARIFA, DE ACORDO COM O CONSUMO DE ÁGUA

(A) Definindo sua categoria de consumo:
1 - Residencial
2 - Residencial Social
3 - Comercial
4 - Industrial
Em qual categoria seu imóvel se enquadra? Selecione uma das opções acima: 1

(B) Definindo o consumo de água:
Informe seu consumo estimado no mês (em m³): 27

(C) Resultado da simulação:
Para consumo de 27.00 m³ de água (referente à categoria residencial), o valor estimado a pagar será de R$ 358.35.
'''
