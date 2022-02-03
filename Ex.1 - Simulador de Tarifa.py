'''
Para este exercício, tentei escrever um algoritmo que simulasse quais os gastos com água junto à uma companhia fornecedora,
levando em conta o tipo de consumidor e seu consumo. Eu me baseei nos dados de uma tabela real que encontrei na internet com
as seguintes tarifas em vigor em certa época junto à CASAN (Companhia Catarinense de Água e Saneamento).

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

    op = int(input('Selecione uma das opções acima: '))
    if (op == 1) or (op == 2) or (op == 3) or (op == 4):

      print('\n(B) Definindo o consumo de água:')
      consumo = float(input('Informe seu consumo estimado no mês (em m³): '))
      while True:
        if(op == 1):
          categoria = 'residencial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Independentemente do não-consumo de água, o valor da tarifa fixa para a categoria {categoria} é de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              total = consumo * 1.96 + fixo
            elif(consumo >= 11 and consumo <=25):
              total = consumo * 9.11  + fixo
            elif(consumo >= 26 and consumo <=50):
              total = consumo * 12.18 + fixo
            else:
              total = consumo * 15.32 + fixo

        elif(op == 2):
          categoria = 'residencial social'
          fixo = 5.50
          if (consumo == 0):
            print(f'\n> Independentemente do não-consumo de água, o valor da tarifa fixa para a categoria {categoria} é de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              total = consumo * 0.37 + fixo
            elif(consumo >= 11 and consumo <=25):
              total = consumo * 2.61  + fixo
            elif(consumo >= 26 and consumo <=50):
              total = consumo * 12.18 + fixo
            else:
              total = consumo * 15.32 + fixo

        elif(op == 3):
          categoria = 'comercial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Independentemente do não-consumo de água, o valor da tarifa fixa para a categoria {categoria} é de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              total = consumo * 4.34 + fixo
            elif(consumo >= 11 and consumo <=50):
              total = consumo * 12.18  + fixo
            else:
              total = consumo * 15.32 + fixo

        elif(op == 4):
          categoria = 'industrial'
          fixo = 29.49
          if (consumo == 0):
            print(f'\n> Independentemente do não-consumo de água, o valor da tarifa fixa para a categoria {categoria} é de R$ {fixo:.2f}.')
            break
          else:
            if(consumo >= 1 and consumo <=10):
              total = consumo * 4.34 + fixo
            else:
              total = consumo * 12.18 + fixo
        print('\n(C) Resultado da simulação:')
        print(f'Para consumo de {consumo:.2f} m³ de água (referente à categoria {categoria}), o valor estimado a pagar será de R$ {total:.2f}.')
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
Selecione uma das opções acima: 1

(B) Definindo o consumo de água:
Informe seu consumo estimado no mês (em m³): 27

(C) Resultado da simulação:
Para consumo de 27.00 m³ de água (referente à categoria residencial), o valor estimado a pagar será de R$ 358.35.
'''