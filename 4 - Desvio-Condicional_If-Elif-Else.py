'''
O Central Shopping utiliza a seguinte tabela de preços para o estacionamento de veículos dos clientes:

Tempo de permanência  | Preço
Até 15 minutos          Grátis
Até 60 minutos          R$ 14,00
Acima de 60 minutos     R$ 28,00

Escreva um algoritmo que receba o tempo de permanência do veículo e apresente quanto o cliente precisará pagar na saída.
'''

tempo = int(input('Quanto tempo o carro do cliente permaeneceu na vaga (em minutos)? '))

print('\nEstacionamento Central Shopping - Ticket de Saída')
if(tempo<=15):
    print('> Tempo de permanência na vaga: {} minutos\n> Valor a ser pago: R$ 0,00 (tarifa grátis)'.format(tempo))
elif(tempo>15 and tempo<=60):
    print('> Tempo de permanência na vaga: {} minutos\n> Valor a ser pago: R$ 14,00'.format(tempo))
else:
    print('> Tempo de permanência na vaga: {} minutos\n> Valor a ser pago: R$ 28,00'.format(tempo))