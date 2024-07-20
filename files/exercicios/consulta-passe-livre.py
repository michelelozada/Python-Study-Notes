'''
> Repositório: Python - Notas de estudo
> GitHub: @michelelozada
> Exercício criado para praticar conceitos aprendidos

Escreva um algoritmo que consulte se um usuário tem direito à gratuidade para uso do transporte coletivo, que é válido
apenas para: estudantes menores de 18 anos, crianças menores de 6 anos, idosos a partir de 65 anos e profissionais públicos
em serviço.
'''


print('Tem direito à gratuidade no transporte coletivo? Consulte abaixo para saber')
idade = int(input('Por favor, informe a idade do usuário: '))

if idade < 6:
    print('> Criança até 6 anos, portanto com direito ao passe livre no transporte coletivo.')
elif idade < 18:
    estudante = input('Usuário é estudante? (s/n) ').lower()
    if estudante == 's':
        print('O usuário é menor de 18 anos e é estudante, portanto tem direito ao passe livre.')
    else:
        print(f'Usuário possui {idade} anos e não é estudante, portanto deve pagar a tarifa integral.')
elif idade >= 65:
    print(f'Usuário com {idade} anos, portanto tem direito ao passe livre.')
else:
    profissional_publico = input('O usuário é policial, bombeiro, carteiro ou guarda municipal? (s/n) ').lower()
    if profissional_publico == 's':
        print('Estando uniformizado e em serviço, este usuário tem direito ao passe livre.')
    else:
        print(f'Usuário com {idade} anos e sem prerrogativas especiais, portanto deve pagar a tarifa integral.')