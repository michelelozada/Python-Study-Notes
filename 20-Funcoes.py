'''
 *  Funções
 *  Repositório: Lógica de Programação e Algoritmos em Python
 *  GitHub: @michelelozada

Criar funções para cálculo de notas de um aluno, sendo que:
- A atividade prática deve ter peso de 40%.
- O exame final deve ter peso de 60%.
- Deve ser informado se o aluno foi aprovado ou não na disciplina (a média da escola é 7).
'''

#### As funções
def nota_efetiva_pratica(nota_obtida1, peso = 0.4):
    global nota_efetiva1
    nota_efetiva1 = nota_obtida1 * peso

def nota_efetiva_exame(nota_obtida2, peso = 0.6):
    global nota_efetiva2
    nota_efetiva2 = nota_obtida2 * peso

def imprime_resultado(notas_finais):
    sum = 0
    cont = 0
    for nota in notas_finais:
        sum = sum + nota
        cont = cont + 1
        print(str(cont)+'a. avaliação: Nota',nota)
    print(f'Nota final obtida: {sum:.1f}')
    if sum >= 7.0:
        print('>> Status: O aluno foi aprovado')
    else:
        print('>> Status: O aluno ficou para recuperação')


#### O programa principal

# Input das notas obtidas pelo aluno
nota_obtida1 = float(input('Entre com a nota obtida na atividade prática (representa 40% da nota final): '))
nota_obtida2 = float(input('Entre com a nota obtida no exame (representa 60% da nota final): '))

# Chamando funções para cálculo das notas efetivas, de acordo com seus pesos
nota_efetiva_pratica(nota_obtida1)
nota_efetiva_exame(nota_obtida2)

# Inclusão em lista das notas obtidas
notas_finais = [nota_efetiva1, nota_efetiva2]

# Impresão do informativo das notas
print('\nDesempenho do aluno:')
imprime_resultado(notas_finais)

'''
Output 

Entre com a nota obtida na atividade prática (representa 40% da nota final): 7.5
Entre com a nota obtida no exame (representa 60% da nota final): 6.5

Desempenho do aluno:
1a. avaliação: Nota 3.0
2a. avaliação: Nota 3.9
Nota final obtida: 6.9
>> Status: O aluno ficou para recuperação
'''