'''
Para este exercício, procurei os preços de uma loja atacadista de produtos do ramo de lembrancinhas/souvenirs, que
trabalhasse com o chamado desconto progressivo. Uma das promoções encontradas foi a seguinte:

------------------------------------------
  ITEM - COD. 3021
  Preço unitário: R$ 1,25

  Tabela de preços - Atacado*:
  Quantidade (un.)  Desconto
  de 60 a 99            -
  de 100 a 249         4%
  de 250 a 499        12%
  de 500 a 749        20%
  de 750 a 999        28%
  acima de 1000       32%

  * Pedido mínimo de 60 unidades
------------------------------------------
O algoritmo abaixo é para registro do vendedor da encomenda feita pelo cliente.

'''

while True:
    item = "Souvenir Código 3021"
    print('ENCOMENDA DE PRODUTO: ' + item)
    try:
        quantidade = int(input('  Qual a quantidade encomendada (em unidades)? '))
        # definição dos intervalos
        if (quantidade < 60):
            print(f'\n> Aviso: Vendas somente acima de 60 unidades. Por favor, comece novamente.\n')
            continue;
        elif (quantidade >= 60 and quantidade <= 99):
            percentual = 0
        elif (quantidade >= 100 and quantidade <= 249):
            percentual = 4
        elif (quantidade >= 250 and quantidade <= 499):
            percentual = 12
        elif (quantidade >= 500 and quantidade <= 749):
            percentual = 20
        elif (quantidade >= 750 and quantidade <= 999):
            percentual = 28
        elif (quantidade >= 1000):
            percentual = 32
        # atribuição e cálculo dos valores
        preco = 1.25
        abatimento = quantidade * preco * (percentual / 100)
        total = quantidade * preco - abatimento
        print(
            f'\nREGISTRO DE ENCOMENDA \n  Item escolhido: {item} \n  Quantidade encomendada: {quantidade} unidades \n  Valor do pedido: R$ {quantidade * preco:.2f} \n  Desconto promocional: R$ {abatimento:.2f}\n  Total a pagar: R$ {total:.2f}\n')
        break
        # tratamento de exceções
    except ValueError:
        print('\n> Aviso: O valor digitado precisa ser um número. Por gentileza, tente novamente.\n')
        continue

'''
        ENCOMENDA DE PRODUTO: Souvenir Código 3021
          Qual a quantidade encomendada (em unidades)? 233

        REGISTRO DE ENCOMENDA 
          Item escolhido: Souvenir Código 3021 
          Quantidade encomendada: 233 unidades 
          Valor do pedido: R$ 291.25 
          Desconto promocional: R$ 11.65
          Total a pagar: R$ 279.60
'''