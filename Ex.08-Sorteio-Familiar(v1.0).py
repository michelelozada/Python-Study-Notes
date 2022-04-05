# Escreva um algoritmo que permita a uma fa1 - oteria-Familiar(Bingo_family).pymília de 5 integrantes promover um sorteio entre entre eles.

# Importando a biblioteca random
import random
print('Loteria da Família Smith')
print('Vamos sortear quem vai ter o direito de escolher e ganhar um presente este mês?')

participantes = ['Papai','Mamãe','Sofia','Luísa','Enzo']
numeros_sorteio = [1,2,3,4,5]

# Definindo a escolha de um número aleatório dentro do intervalo de números do sorteio (será revelado apenas no final do programa)
numero_sorteado = random.choice(numeros_sorteio)

print('\nAtenção, pessoal, anotem seus números!')
for p in participantes:
    numero_atribuido = random.choice(numeros_sorteio)
    print(f'- {p}, seu número para este sorteio é: ',end="")
    print(numero_atribuido)
    # Armazenando qual o integrante que ganhou o sorteio, de acordo com o número a que lhe foi atribuído
    if numero_atribuido == numero_sorteado:
        vencedor = p
    numeros_sorteio.remove(numero_atribuido)

# Apresentando o ganhador do sorteio
resultado = input('\nDaí, Família Smith, preparados para o sorteio? Digitem s para descobrir quem ganhou o sorteio. ')
while True:
    if (resultado == 's'):
        print('\n>> Resultado: Foi sorteado o número', numero_sorteado,'e quem ganhou a loteria hoje foi você, '+vencedor+'. Parabéns!!!')
        print('(Demais integrantes não fiquem tristes, porque mês que vem tem mais sorteio, combinado? ;)')
        break
    else:
       continue

''' Primeiro output gerado:
Loteria da Família Smith
Vamos sortear quem vai ter o direito de escolher e ganhar um presente este mês?

Atenção, pessoal, anotem seus números!
- Papai, seu número para este sorteio é: 4
- Mamãe, seu número para este sorteio é: 5
- Sofia, seu número para este sorteio é: 1
- Luísa, seu número para este sorteio é: 2
- Enzo, seu número para este sorteio é: 3

Daí, Família Smith, preparados para o sorteio? Digitem s para descobrir quem ganhou o sorteio. s

>> Resultado: Foi sorteado o número 5 e quem ganhou a loteria hoje foi você, Mamãe. Parabéns!!!
(Demais integrantes não fiquem tristes, porque mês que vem tem mais sorteio, combinado? ;)
'''


''' Próximo output gerado:
Loteria da Família Smith
Vamos sortear quem vai ter o direito de escolher e ganhar um presente este mês?

Atenção, pessoal, anotem seus números!
- Papai, seu número para este sorteio é: 4
- Mamãe, seu número para este sorteio é: 2
- Sofia, seu número para este sorteio é: 3
- Luísa, seu número para este sorteio é: 5
- Enzo, seu número para este sorteio é: 1

Daí, Família Smith, preparados para o sorteio? Digitem s para descobrir quem ganhou o sorteio. s

>> Resultado: Foi sorteado o número 5 e quem ganhou a loteria hoje foi você, Luísa. Parabéns!!!
(Demais integrantes não fiquem tristes, porque mês que vem tem mais sorteio, combinado? ;)
'''