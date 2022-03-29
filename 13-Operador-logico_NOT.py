'''
Escrever um algoritmo que faça a consulta se um usuário tem direito a gratuidade para uso do transporte coletivo (válido
para esudantes dmenore de 18 anos, crinaãs menores de 6 anos, idosos e profissionais públicos em serviço. Para tanto, só
poderão ser utilizados operadores lógicos do tipo NOT.
'''

print('- Tem direito à gratuidade no transporte coletivo? Consulte abaixo para saber - ')
idade = int(input('\nPor favor, informe a idade do usuário: '))
if not(idade < 6):
    if not(idade >= 65):
        estudante = input('O usuário é estudante e tem menos de 18 anos? (s/n) ')
        if (not (estudante == 'n')) and (not(idade > 18)):
            print(f'> O usuário é menor de 18 anos e é estudante, portanto, tem direito ao passe livre no transporte'
                  f'coletivo (solicite o Passe Estudantil na Prefeitura).')
        elif (not(estudante == 's')) and (not(idade > 18)):
            print(f'> Usuário com {idade} anos de idade e não é estudante, portanto, deve pagar a tarifa integral para '
                  f'uso do transporte coletivo.')
        else:
            profissional = input('O usuário é policial, bombeiro, carteiro ou guarda municipal? (s/n) ')
            if not(profissional == 's'):
                print( f'> Usuário com {idade} anos de idade e sem prerrogativas especiais, portanto, deve pagar a tarifa'
                       f' integral para uso do transporte coletivo.')
            else:
                print('> Quando estiver em serviço, este usuário tem direito à isenção no uso do transporte coletivo (para '
                      'embarcar, é necesário apresentar sua ID profissional e estar uniformizado).')
    else:
        print(f'> Usuário com {idade} anos de idade, portanto, com direito ao passe livre no transporte coletivo (solicite '
              f'o Passe Sênior na Prefeitura).')
else:
    print(f'> O usuário é uma criança com {idade} anos de idade, portanto, tem direito ao passe livre no transporte coletivo '
          f'(não há necessidade de cartão).')

'''
Outputs possíveis:

Por favor, informe a idade do usuário: 4
> O usuário é uma criança com 4 anos de idade, portanto, tem direito ao passe livre no transporte coletivo (não há necessidade de cartão).

Por favor, informe a idade do usuário: 10
O usuário é estudante? (s/n) s
> O usuário é menor de 18 anos e é estudante, portanto, tem direito ao passe livre no transporte coletivo (solicite o Passe Estudantil na Prefeitura).

Por favor, informe a idade do usuário: 17
O usuário é estudante e tem menos de 18 anos? (s/n) n
> Usuário com 17 anos de idade e não é estudante, portanto, deve pagar a tarifa integral para uso do transporte coletivo.

Por favor, informe a idade do usuário: 25
O usuário é estudante e tem menos de 18 anos? (s/n) n
O usuário é policial, bombeiro, carteiro ou guarda municipal? (s/n) s
> Quando estiver em serviço, este usuário tem direito à isenção no uso do transporte coletivo (para embarcar, é necesário apresentar sua ID profissional e estar uniformizado).

Por favor, informe a idade do usuário: 25
O usuário é estudante e tem menos de 18 anos? (s/n) n
O usuário é policial, bombeiro, carteiro ou guarda municipal? (s/n) n
> Usuário com 25 anos de idade e sem prerrogativas especiais, portanto, deve pagar a tarifa integral para uso do transporte coletivo.

Por favor, informe a idade do usuário: 65
> Usuário com 65 anos de idade, portanto, com direito ao passe livre no transporte coletivo (solicite o Passe Sênior na Prefeitura).
'''