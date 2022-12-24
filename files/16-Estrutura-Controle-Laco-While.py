'''
 *  Estrutura de controle - Laço While
 *  Repositório: Python - Notas de estudo
 *  GitHub: @michelelozada


Escreva um algoritmo para simular um formulário que impeça que o usuário avance para a próxima pergunta, caso algum
campo seja deixado em branco. Obs: O campo idade também não deve permitir a entrada de outro valor que não seja numérico
ou igual a zero.
'''

nome = ''
idade = ''
profissao = ''
#campo nome
while not nome:
    nome = input('Digite seu nome: ')
    if(not nome):
        print('(Erro: Você não pode deixar este campo vazio)')
#campo profissão
while not profissao:
    profissao = input('Digite sua profissão: ')
    if(not profissao):
        print('(Erro: Você não pode deixar este campo vazio)')
#campo idade
while not idade:
    try:
        idade = int(input('Digite sua idade: '))
        if idade:
            break
        else:
            print('(Erro: Você não pode preencher este campo com valor igual a zero)')
    except ValueError:
        print('(Erro: Você não utilizou um valor numérico aqui)')
        continue
print('Status: Formulário preenchido com sucesso.')


"""
Digite seu nome: 
(Erro: Você não pode deixar este campo vazio)
Digite seu nome: Paula Reis
Digite sua profissão: 
(Erro: Você não pode deixar este campo vazio)
Digite sua profissão: Programadora
Digite sua idade: 
(Erro: Você não utilizou um valor numérico aqui)
Digite sua idade: asdfg
(Erro: Você não utilizou um valor numérico aqui)
Digite sua idade: 0
(Erro: Você não pode preencher este campo com valor igual a zero)
Digite sua idade: 25
Status: Formulário preenchido com sucesso.
"""