## Exercícios de nivelamento em Python - Bootcamp Data Analytics (WoMakersCode - 2024)

### Parte 1: Conceitos Básicos de Python 

&nbsp; 

1. Escreva um programa que solicite dois números e realize as operações de soma, subtração, multiplicação e divisão.  
```py

def solicitar_numeros():
  numero1 = int(input('Por favor, digite o 1º número: '))
  numero2 = int(input('Agora, digite o 2º número: '))
  return numero1, numero2

def somar_numeros(numero1, numero2):
  return numero1 + numero2

def subtrair_numeros(numero1, numero2):
  return numero1 - numero2

def multiplicar_numeros(numero1, numero2):
  return numero1 * numero2

def dividor_numeros(numero1, numero2):
  if numero2 != 0:
    return numero1 / numero2
  else:
      return "Divisão por zero não é possível"

def calcular_numeros(numero1, numero2):
  operacoes = {
    'Soma': somar_numeros(numero1, numero2),
    'Subtração': subtrair_numeros(numero1, numero2),
    'Multiplicação': multiplicar_numeros(numero1, numero2),
    'Divisão': dividor_numeros(numero1, numero2)
  }
  return operacoes

def imprimir_resultados(resultados):
  print('\nResultados das operações')
  for operacao, resultado in resultados.items():
    print(f' . {operacao}: {resultado}')


# Chamada da função que solicita os números
numero1, numero2 = solicitar_numeros()

# Chamada de função que recebe um dicionario com resultado das operações
resultados = calcular_numeros(numero1, numero2)

# Chamada de função que imprime o tipo e resultado das operações
imprimir_resultados(resultados)
```

&nbsp; 

2. Solicite ao usuário que informe o seu ano de nascimento. Em seguida, o programa deve calcular e imprimir a idade atual do usuário

```py

# importando a biblioteca datetime
import datetime

ano_nascimento = int(input('Por favor, informe o seu ano de nascimento: '))
# datetime.date.today() retorna a data atual | .year extrai o ano da data atual
ano_corrente = datetime.date.today().year

idade = ano_corrente - ano_nascimento
print(f'> Resposta: O(a) usuário(a) possui/fará {idade} anos em {ano_corrente}.')
```

&nbsp; 


3. Escreva um programa que peça a quantidade de quilômetros e a transforme em metros, centímetros e milímetros.  

```py

def conversao_km_para_metros(quilometros):
  return quilometros * 1000

def conversao_metros_para_centimetros(metros_obtidos):
  return metros_obtidos * 100

def conversao_centimetros_para_milimetros(centimetros_obtidos):
  return centimetros_obtidos * 10

def gerar_resultados(quilometros):
  """ Gera e imprime os resultados das conversões """
  metros_obtidos = conversao_km_para_metros(quilometros)
  centimetros_obtidos = conversao_metros_para_centimetros(metros_obtidos)
  milimetros_obtidos = conversao_centimetros_para_milimetros(centimetros_obtidos)
  print(f'\nEstas são as equivalências para {quilometros:.2f} quilômetro(s):')
  print(f'  . {metros_obtidos:,.2f} metros')
  print(f'  . {centimetros_obtidos:,.2f} centímetros')
  print(f'  . {milimetros_obtidos:,.2f} milímetros')

try:
  quilometros = float(input('Por favor, informe uma quantidade em quilômetros: '))
  if quilometros > 0:
    gerar_resultados(quilometros)
  else:
    print('Por favor, recomece e informe um valor positivo e maior que zero.')
except ValueError:
  print('Por favor, recomece e informe um valor válido.')
```

&nbsp; 

4. Escreva um programa que receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. O programa deve calcular e imprimir o consumo médio em km/l.  

```py

def solicitar_dados():
  while True:
    try:
      volume_consumo = float(input('Por favor, informe qual a quantidade de combustível consumida (em litros): '))
      distancia_percorrida = float(input('Agora, informe qual a distância percorrida (em km): '))
      if volume_consumo <= 0 or distancia_percorrida <= 0:
        print('Erro: informar apenas valores positivos')
      else:
        return volume_consumo, distancia_percorrida
    except ValueError:
      print('Erro: informar apenas valores numéricos')

def calcular_consumo_medio(volume_consumo, distancia_percorrida):
  consumo_medio = distancia_percorrida / volume_consumo
  return consumo_medio

# Recebe valores digitados pelo usuário com a chamada da função
volume_consumo, distancia_percorrida = solicitar_dados()

# Calcula o consumo médio com a chamada da função
consumo_medio = calcular_consumo_medio(volume_consumo, distancia_percorrida)

# Exibição do resultado
print(f'\n> O consumo médio do veículo foi {consumo_medio:.2f} km/l.')
```

&nbsp; 


5. Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus, levando em consideração os seguintes dados de velocidade média do:  
+--------+----------+
| avião  | 600 km/h |
| carro  | 100 km/h |
| ônibus | 80 km/h  |
+--------+----------+

```py

# Velocidades médias
velocidade_onibus = 80
velocidade_carro = 100
velocidade_aviao = 600

def solicitar_distancia():
  while True:
    try:
      distancia = float(input("Por favor, informe qual a distância percorrida (em km): "))
      if distancia <= 0:
        print('Por favor, entre com digite valor positivo/maior que zero.\n')
        continue
      else:
        return distancia
    except ValueError:
      input('> Por favor, entre com valores numéricos.')

def inserir_minutos(tempo_em_horas):
  horas = int(tempo_em_horas)
  minutos = int((tempo_em_horas - horas) * 60)
  return horas, minutos

def calculo_onibus(distancia):
  tempo_em_horas = distancia / velocidade_onibus
  return inserir_minutos(tempo_em_horas)

def calculo_carro(distancia):
  tempo_em_horas = distancia / velocidade_carro
  return inserir_minutos(tempo_em_horas)

def calculo_aviao(distancia):
  tempo_em_horas = distancia / velocidade_aviao
  return inserir_minutos(tempo_em_horas)

def exibir_comparativo(distancia):
  hora_onibus, minuto_onibus = calculo_onibus(distancia)
  hora_carro, minuto_carro = calculo_carro(distancia)
  hora_aviao, minuto_aviao = calculo_aviao(distancia)

  print(f'\nComparativo de tempo para uma viagem de {distancia:.2f} km, caso seja feita de:')
  print(f'. Ônibus - {hora_onibus:02}:{minuto_onibus:02}')
  print(f'. Carro - {hora_carro:02}:{minuto_carro:02}')
  print(f'. Avião - {hora_aviao:02}:{minuto_aviao:02}')

distancia = solicitar_distancia()
exibir_comparativo(distancia)
```

&nbsp; 

6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: 
IMC = peso / (altura x altura).  

```py

```

&nbsp; 

7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.   

```py

```

&nbsp; 

8. Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.  

```py

```

&nbsp; 

9. Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.   
Exemplos de variáveis: nome, idade, lugar, profissão ....   
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.   
Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade.  
```py

```