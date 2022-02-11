"""
Escreva um algoritmo para simular permissão de acesso a um sistema. Após três tentativas sem sucesso de inclusão de senha,
o programa deve ser encerrado.
"""

def mensagem():
    leitura_senha = input(f"Qual a sua senha? (tentativa {cont} de 3): ")

email = "ana@gmail.com"
senha = "ana123#"
leitura_email = " "
leitura_senha = " "

print('> Faça login abaixo para acessar nosso sistema:')
while True:
    leitura_email = input("Qual seu e-mail? ")
    if (leitura_email == email):
        break
    else:
        print('\n> Por favor, digite seu e-mail novamente, pois não confere com o cadastrado no sistema.')
        continue

cont = 1
mensagem()
#leitura_senha = input(f'Qual a sua senha? (Tentativa {cont} de 3) ')

while (cont <= 2):
    if (leitura_senha !=  senha):
        cont = cont + 1
        print(f'\n> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.')
        mensagem()
        #leitura_senha = input(f'Qual a sua senha? (Tentativa {cont} de 3) ')
        continue
    else:
        break
# feedback para o usuário
if (leitura_senha != senha):
    print(f'\n> Acesso negado após senha ter sido informada com erro por três vezes. Por favor, contate o administrador do sistema.')
else:
    print(f'\n> Login realizado com sucesso. Seja bem-vindo(a) ao sistema!')


"""
> Faça login abaixo para acessar nosso sistema:
Qual seu e-mail? ana@gmail.com.br

> Por favor, digite seu e-mail novamente, pois não confere com o cadastrado no sistema.
Qual seu e-mail? ana@gmail.com
Qual a sua senha? (tentativa 1 de 3): ana123

> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.
Qual a sua senha? (tentativa 2 de 3): ana12#

> Por favor, digite a senha novamente, pois não confere com a cadastrada no sistema.
Qual a sua senha? (tentativa 3 de 3): ana123*

> Acesso negado após senha ter sido informada com erro por três vezes. Por favor, contate o administrador do sistema.
"""