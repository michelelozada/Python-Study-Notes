"""
Escreva um algoritmo que apresente o resultado da conversão de um valor, de real para libra esterlina.
O algoritmo deve receber o valor da cotação da libra e a quantidade em reais a ser convertida.
"""


print('-- Conversor de Real/BRL para Libra Esterlina/GBP --')

cotacaoLibra = float(input('\nQual o valor da cotação de hoje da Libra em relação ao Real? £ 1.00 = R$ '))
quantidadeReal = float(input('Qual a quantia em Real que você deseja converter para Libra Esterlina? R$ ' ))

print(f'\n> Resultado da conversão: Na cotação de hoje, você pode comprar £ {quantidadeReal/cotacaoLibra:.4f} (GBP) utilizando a quantia de R$ {quantidadeReal:.2f} (BRL).')


"""
-- Conversor de Real/BRL para Libra Esterlina/GBP --

Qual o valor da cotação de hoje da Libra em relação ao Real? £ 1.00 = R$ 7.1597
Qual a quantia em Real que você deseja converter para Libra Esterlina? R$ 500.00

> Resultado da conversão: Na cotação de hoje, você pode comprar £ 69.8353 (GBP) utilizando a quantia de R$ 500.00 (BRL).

"""