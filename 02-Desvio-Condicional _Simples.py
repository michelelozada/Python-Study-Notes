"""
Peguei um destes testes bem-humorados da época daquele meme sobre ser cringe (= nascidas entre as décadas de 80 e 90) ou não.
Pensei nisso, pois precisava de um pretexto para elaborar um pequeno algoritmo para usar a estrutura condicional simples.
"""


print('Será que você é cringe? Faça o teste abaixo e descubra!\n')
cont = 0
q = input('1 - Você é fã de Harry Potter, Disney ou Friends? ')
if (q.lower() == 's'):
    cont += 1
q = input('2 - Você paga suas compras e/ou contas no boleto? ')
if (q.lower() == 's'):
    cont += 1
q = input("3 - Você usa emoji 'chorando de rir' ou 'rsrsrs' para rir na internet? ")
if (q.lower() == 's'):
    cont += 1
q = input("4 - Você teve de pesquisar o que significa cringe no Google? ")
if (q.lower() == 's'):
    cont += 1
q = input("5 - Você é da época das fitas, DVDs e CDs? ")
if (q.lower() == 's'):
    cont += 1

print('\n>> Resultado:',cont,'pontos')
if(cont == 2):
    print('   Apesar de uma ou outra característica em comum, você não é cringe!')
else:
    if(cont == 3 or cont == 4):
        print('   Está passando perto, mas - tecnicamente falando - você não é exatamente cringe!')
    else:
        if (cont == 5):
            print('   OK, agora é oficial: você é Millenial... e é cringe também!')
        else:
            print('   Olha: você nem precisava fazer este teste, pois se tem alguém que está longe de ser cringe, é você!')


"""
Será que você é cringe? Faça o teste abaixo e descubra!

1 - Você é fã de Harry Potter, Disney ou Friends? s
2 - Você paga suas compras e/ou contas no boleto? s
3 - Você usa emoji 'chorando de rir' ou 'rsrsrs' para rir na internet? n
4 - Você teve de pesquisar o que significa cringe no Google? n
5 - Você é da época das fitas, DVDs e CDs?? s

>> Resultado: 3 pontos
   Está passando perto, mas - tecnicamente falando - você não é exatamente cringe!
"""