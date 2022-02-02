"""
Escreva um algoritmo que apresente o resultado da conversão de um valor, de real para libra esterlina.
O algoritmo deve receber o valor da cotação da libra e a quantidade em reais a ser convertida.
"""

print('- Conversor de Real Brasileiro (BRL) para Libra Esterlina (GBP) -')

cotacaoReal = float(input('Qual o valor da cotação da Libra Esterlina em relação ao Real hoje? £ 1.00 = R$ '))
quantidadeReal = float(input('Qual o valor que você deseja converter para Libras Esterlinas? R$ ' ))

quantidadeLibras =  quantidadeReal/cotacaoReal

print(f'\n> Resultado da conversão de moedas: R$ {quantidadeReal:.2f} (BRL) = £ {quantidadeLibras:.4f} (GBP) ')


'''
- Conversor de Real Brasileiro (BRL) para Libra Esterlina (GBP) -
Qual o valor da cotação da Libra Esterlina em relação ao Real hoje? £ 1.00 = R$ 7.1292
Qual o valor que você deseja converter para Libras Esterlinas? R$ 100.00

> Resultado da conversão de moedas: R$ 100.00 (BRL) = £ 14.0268 (GBP) 
'''