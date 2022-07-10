'''
 *  Exercício: Sistema de login
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada


Escreva um algoritmo para simular permissão de acesso a um sistema. Após três tentativas sem sucesso de inclusão de senha,
o programa deve ser encerrado.
'''


email = "ana@example.com"
senha = "ana123#"

print('> Faça login abaixo para acessar nosso sistema:')
#validação do email
while True:
    leitura_email = input("Qual seu e-mail? ")
    if (leitura_email == email):
        break
    else:
        print('\n> Por favor, digite seu e-mail novamente, pois não confere com o cadastrado no sistema.')
        continue
#validação da senha
leitura_senha = input(f"Qual a sua senha? (tentativa 1 de 3): ")
for tentativa in range (1,3):
    if (leitura_senha == senha):
       break
    else:
        print(f'\n> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.')
        tentativa += 1
        leitura_senha = input(f"Qual a sua senha? (tentativa {tentativa} de 3): ")
        continue
# feedback para o usuário
if (leitura_senha != senha):
    print(f'\n> Acesso negado após a senha ter sido informada com erro por três vezes. Por favor, contate o administrador do sistema.')
else:
    print(f'\n> Login realizado com sucesso. Seja bem-vindo(a) ao sistema!')


"""
> Faça login abaixo para acessar nosso sistema:
Qual seu e-mail? ana@example.com.br

> Por favor, digite seu e-mail novamente, pois não confere com o cadastrado no sistema.
Qual seu e-mail? ana@example.com
Qual a sua senha? (tentativa 1 de 3): ana123

> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.
Qual a sua senha? (tentativa 2 de 3): ana123*

> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.
Qual a sua senha? (tentativa 3 de 3): ana#123

> Acesso negado após a senha ter sido informada com erro por três vezes. Por favor, contate o administrador do sistema.

Process finished with exit code 0
"""