> **Estruturas de repetição**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Estruturas de Repetição em Python *(mini-revisão)*
 
```
- Existem duas estruturas principais de repetição em Python: o loop for e o loop while. 

- Estas duas estruturas de repetição são úteis em diferentes situações e a escolha entre elas dependerá 
do contexto específico do problema que está se tentando resolver

- Alguns conceitos importantes neste contexto são: 
  . Variável contadora, que é usada normalmente no loop while para controlar quantas vezes o bloco de 
	código dentro do loop é executado. Ela é inicializada com um dado valor e é incrementada a cada 
	iteração, até alcançar um limite pré-definido.
	. Variável acumuladora, que é usada para armazenar o resultado de operações realizadas ao longo das 
	iterações do loop for ou while
  . continue e break, que são palavras-chave utilizadas para, respectivamente, controlar e interromper 
	o fluxo de execução dentro de loops for e while	
```

&nbsp;  

## O Loop for
Usado para iterar sobre uma sequência (como uma lista, tupla, dicionário ou string) ou em um intervalo específico, executando o bloco de código associado a cada elemento desta sequência.

&nbsp;  

↳ Sintaxe básica do loop for:
```py

for item in sequencia:
  # item assume o valor de cada elemento na sequência, a cada iteração do loop.
```	

&nbsp;  

↳ Exercício: Calcule o quadrado de cada número da lista abaixo
```py

numeros = [1, 2, 3, 4, 5]

# O loop for vai iterar sobre cada número da lista numeros
for numero in numeros:
  quadrado = numero ** 2
  print(f"O quadrado de {numero} é {quadrado}")

'''
Saída:
  O quadrado de 1 é 1
  O quadrado de 2 é 4
  O quadrado de 3 é 9
  O quadrado de 4 é 16
  O quadrado de 5 é 25
'''
```

&nbsp;  

### •  Loop for em conjunto com a função `range()`

O `range()` é uma função incorporada em Python que gera uma sequência de números em uma progressão aritmética. É frequentemente utilizada em conjunto com o loop for para iterar sobre uma sequência de números específica. 

&nbsp; 

↳ No exemplo abaixo: range(5) gera uma sequência de números de 0 a 4 (não incluindo o número 5) sobre a qual o loop for vai iterar, imprimindo cada um desses números
```py

for i in range(5):
  print(i)
	
'''
Saída:
0
1
2
3
4
'''
```

&nbsp; 

↳ Exercício: Uma brincadeira antiga consistia em contar números em voz alta, substituindo os números múltiplos de 4 pela
palavra 'pi'. Escreva um programa que simule esta brincadeira, imprimindo os números e as ocorrência desta palavra, até o intervalo que o usuário tiver definido:

```py

limite = int(input('Até que número você deseja contar? '))

for numero in range(1, limite + 1):
  if numero % 4 == 0:
    print('pi')
  else:
    print(numero)
```

&nbsp;  

### •  Variável contadora
Também chamada de _variável de iteração_ ou _variável de loop_,  a variável contadora assume valores diferentes (= atualiza seu valor) a cada iteração de um loop. Para isso, conveciona-se usar o nome de variável `i`.

&nbsp;  

↳ Exemplo: 

```py

for i in range(5):
  print(i)
```

&nbsp;  

## Loop while: 
Executa um bloco de código repetidamente enquanto uma condição especificada for verdadeira. Portanto, até que o contador alcance um limite definido, o loop continua em vigor.

&nbsp;  

Recurso muito útil para quando se necessita garantir que um usuário permaneça em um determinado bloco até que certas entradas sejam válidas.

&nbsp;  

↳ Sintaxe básica do loop while:

```py

while condição:
  # O bloco de código aqui é repetido enquanto a condição for verdadeira
```

&nbsp; 

↳ Exercício: Conte de 1 até 5 usando um loop while. 
```py

# Inicializando a variável contadora
contador = 1

# Definindo o limite
limite = 5

# Loop while executa enquanto o contador é menor ou igual ao limite (que é 5)
while contador <= limite:
  print(contador)
  contador += 1  # Incrementa o contador a cada iteração do loop
	
'''
Saída:
1
2
3
4
5
'''
```

&nbsp; 

↳ Exercício: Escreva um algoritmo em que o usuário deve informar dois números, sendo que serão impressos na tela somente os números pares compreendidos no intervalo dos números fornecidos:

```py

numero_inicial = int(input('Digite o número inicial do intervalo: '))
numero_final = int(input('Digite o número final do intervalo: '))

numero_em_vigor = numero_inicial
while(numero_em_vigor <= numero_final):
  if(numero_em_vigor % 2 == 0):
    print(numero_em_vigor)
  numero_em_vigor += 1
```

&nbsp;

### • Variável acumuladora: 
É uma variável que é usada para armazenar valores acumulados de operações realizadas ao longo das iterações de um loop. Costuma ser utilizada em loops `for`, quando iterando sobre uma sequência de elementos.

&nbsp; 

↳ Exercício: Some todos os elementos da lista abaixo:
```py

numeros = [1, 2, 3, 4, 5]

# Variável acumuladora para armazenar a soma dos números
soma = 0

# Loop for para somar todos os números na lista
for numero in numeros:
  soma += numero

print("A soma dos números da lista é:", soma)

# Saída: A soma dos números da lista é: 15
```

&nbsp;

↳ Exercício: Escreva um algoritmo que receba 4 notas de um aluno, calcule a média delas e informe se este aluno foi aprovado (a média da escola é 7.0) ou se ficou para recuperação.

```py

provas = [1, 2, 3, 4]

notas = [float(input(f'Por favor informe a {prova}ª nota do aluno: ')) for prova in provas]

soma_notas = 0

for nota in notas:
    soma_notas += nota

media = soma_notas/len(provas)

if(media >= 7.0):
    print("Status: O aluno foi aprovado.")
else:
    print('Status: O aluno ficou para recuperação.')
```

&nbsp;

### • Instrução `continue`: 
Esta palavra-chave é usada para **interromper a iteração atual de um loop e avançar para a próxima iteração**. Ou seja, quando o Python encontra a instrução `continue` dentro de um loop, ele pula o restante do código dentro da iteração atual de um loop  e pula para a iteração seguinte.

&nbsp; 

↳ Sobre o exemplo abaixo: quando i for igual a 3, a instrução `continue` será acionada e o código dentro deste loop será interrompido para essa iteração específica. Repare na saída que o número 3 não será impresso e o loop continuará com a próxima iteração.
```py

for i in range(1, 6):
  if i == 3:
    continue
		print(i)
	
'''
Saída:
1
2
4
5
6
```	

&nbsp; 

### • Instrução `continue`: 
Esta palavra-chave é usada para **interromper a iteração atual de um loop e avançar para a próxima iteração**. Ou seja, quando o Python encontra a instrução `continue` dentro de um loop, ele pula o restante do código dentro da iteração atual de um loop e pula para a iteração seguinte.

&nbsp; 

↳ Sobre o exemplo abaixo: quando i for igual a 3, a instrução `continue` será acionada e o código dentro deste loop será interrompido "no meio" dessa iteração específica. Repare na saída que o número 3 não será impresso e o loop continuará com a próxima iteração.
```py

for i in range(1, 6):
  if i == 3:
    continue
		print(i)
	
'''
Saída:
1
2
4
5
6
```	

&nbsp; 

### • Instrução `break`: 
Esta palavra-chave é usada para **sair completamente de um loop, interrompendo sua execução**, mesmo que a condição de continuação do loop ainda seja verdadeira. 

&nbsp; 

↳ Sobre o exemplo abaixo: Quando i for igual a 4, a instrução `break` será acionada, e o loop será interrompido completamente. Repare na saída que só os números de 1 a 3 foram impressos.

```py

for i in range(1, 6):
  if i == 4:
    break
    print(i)
	 
'''
Saída:
1
2
3
'''
```	 

&nbsp; 

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>