'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício criado para praticar conceitos aprendidos

O Shopping XPTO utiliza a seguinte tabela de preços para o estacionamento de veículos dos clientes:

+----------------------+------------+
| Tempo de permanência | Preço (R$| |
+----------------------+------------+
| 30 minutos           |       8,00 |
| Entre 30 a 60 min    |      16,00 |
| Entre 2 a 3 horas    |   gratuito |
| Acima de 3 horas (*) |   R$ 10,00 |
+----------------------+------------+
* Diferentemente dos outros casos, após o período de gratuidade, será cobrado R$ 10,00 por cada 15 minutos em que o carro permanecer estacionado.

Escreva um algoritmo que receba o tempo de permanência do veículo e imprima um ticket sobre quanto o cliente precisará
pagar (ou não) na saída.
'''


# Definição das variáveis com os preços
valor_a = 8.00   # ref. permanência até 1/2 hora
valor_b = 16.00  # ref. permanência entre 30 a 60 min
valor_c = 0.00   # ref. permanencia entre 2 a 3 horas
valor_d = 10.00  # ref. permanencia acima de 3 horas


# Função para solicitar o tempo de permanência do veículo
def solicitar_tempo():
    while True:
        try:
            print('Abaixo você poderá informar a(s) hora(s) e os minutos em que o veículo permaneceu estacionado.')
            horas = int(input('> Primeiro, por favor, informe por quantas horas: '))
            minutos = int(input('> Agora, informe por quantos minutos: '))
            if horas < 0 or minutos < 0:
                print('Entrada inválida: É necessário inserir um valor positivo.\n')
                continue
            # Convertendo horas para minutos e somando-as com a variável minutos
            tempo_total = horas * 60 + minutos
            return tempo_total
        except ValueError:
            print('Entrada inválida: É necessário inserir um valor numérico.\n')


# Formatação do valor com duas casas decimais
def formatar_valor(valor):
    return '{:.2f}'.format(valor)


# Função para calcular valor a pagar
def calcular_valor(tempo):
    if tempo <= 30:
        valor = formatar_valor(valor_a)
    elif 30 < tempo <= 60:
        valor = formatar_valor(valor_b)
    elif 60 < tempo <= 180:
        valor = formatar_valor(valor_c)
    else:
        quartos_de_hora = (tempo//15) - 12
        valor = formatar_valor(valor_d * quartos_de_hora)

    return valor


# Função para gerar o ticket com tempo e valor a ser pago
def gerar_ticket(tempo):
    valor = calcular_valor(tempo)
    valor_formatado = valor.replace('.', ',')

    horas = tempo // 60
    minutos = tempo % 60

    if horas > 0:
        tempo_formatado = f'{horas:02} horas e {minutos:02} minutos'
    else:
        tempo_formatado = f'{minutos:02} minutos'

    print('\n - Estacionamento do Shopping XPTO - Ticket de Saída - ')
    print(f'Tempo de permanência na vaga: {tempo_formatado}')
    print(f'Valor a ser pago: R$ {valor_formatado}')


# Solicita e valida o tempo de permanência
tempo = solicitar_tempo()

# Imprime na tela o ticket
gerar_ticket(tempo)