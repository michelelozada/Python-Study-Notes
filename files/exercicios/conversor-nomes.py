'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício de um trabalho da faculdade de ADS - 2021

Crie um programa que solicite que o usuário digite um nome. O programa deve:
 - imprimir na tela o nome informado, apenas com letras maiúsculas
 - vogais devem ser substituídas pelos seguintes símbolos:

+-------+---------+
| Letra | Símbolo |
+-------+---------+
| A     | @       |
| E     | &       |
| I     | !       |
| O     | #       |
| U     | *       |
+-------+---------+
'''


print('- CONVERSOR DE PALAVRAS - ')
nome_original = input('\n>> Por favor, digite seu nome: \n')
nome_modificado = nome_original.upper() \
                               .replace('A',"@") \
                               .replace('E','&') \
                               .replace('I','!') \
                               .replace('O',"#") \
                               .replace('U','*')
print(f'\n>> Seu nome com as vogais convertidas:\n{nome_modificado}')

'''
- CONVERSOR DE PALAVRAS - 

>> Por favor, digite seu nome: 
Michele

>> Seu nome com as vogais convertidas:
M!CH&L&
'''