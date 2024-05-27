> **Desvio condicional encadeado**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### Exercício:
O Central Shopping utiliza a seguinte tabela de preços para o estacionamento de veículos dos clientes:
```
+----------------------+----------+
| Tempo de permanência |  Preço   |
+----------------------+----------+
| Até 15 minutos       | Grátis   |
| Até 60 minutos       | R$ 14,00 |
| Acima de 60 minutos  | R$ 28,00 |
+----------------------+----------+
```
Escreva um algoritmo que receba o tempo de permanência do veículo e apresente quanto o cliente precisará pagar na saída.  

```py

tempo = int(input('Quanto tempo o carro do cliente permaeneceu na vaga (em minutos)? '))

print('\nEstacionamento Central Shopping - Ticket de Saída')
if(tempo<=15):
   valor = 'Tarifa gratuita'
elif(tempo>15 and tempo<=60):
    valor = 'R$ 14,00'
else:
  valor = 'R$ 28,00'
print(f'> Tempo de permanência na vaga: {tempo} minutos\n> Valor a ser pago: {valor}')

'''
Quanto tempo o carro do cliente permaeneceu na vaga (em minutos)? 35

Estacionamento Central Shopping - Ticket de Saída
> Tempo de permanência na vaga: 35 minutos
> Valor a ser pago: R$ 14,00
'''
```

&nbsp;

### Simulando a estrutura switch case 
- É uma forma de controle de fluxo 
- Ou seja, permite que seja selecionada uma alternativa dentre as apresentadas, com base no valor de uma expressão 
- A linguagem Python não possui uma estrutura switch case nativa. Porém, para simular este mesmo comportamento, é possível utilizar a estrutura condicional `if-elif-else`

```py
mes = 2

if mes == 1:
  mes_extenso = "Janeiro"
elif mes == 2:
  mes_extenso = "Fevereiro"
elif mes == 3:
  mes_extenso  = "Março"
else:
  mes_extenso = "Um mês não compreendido entre os primeiros do ano"

print(mes_extenso) 

# Retorna: Fevereiro
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>