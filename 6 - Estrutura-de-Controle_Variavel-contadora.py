"""
Escreva um algoritmo em que o usuário deve informar dois números, sendo que serão impressos na tela somente os números
pares compreendidos neste intervalo dos números fornecidos:
"""

n1 = int(input('Diga um número para marcar o início do intervalo: '))
n2 = int(input('Diga o número para fechar o intervalo: '))

print('\nVou imprimir apenas os números pares compreendidos neste intevalo:')
x = n1
while (x <= n2):
    if(x % 2 == 0):
        print(x)
    x += 1

"""
Diga um número para marcar o início do intervalo: 50
Diga o número para fechar o intervalo: 85

Vou imprimir apenas os números pares compreendidos neste intevalo:
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
"""