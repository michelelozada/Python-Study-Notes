> **Funções personalizadas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  

## Funções personalizadas em Python *(mini-revisão)*
```
- São criadas pelo usuário para a realização de uma ação específica, podendo ser chamadas em diferentes
partes do programa

- Dessa forma, cada vez que uma função é chamada no programa principal, certos blocos de código são executados, 
desempenhando alguma tarefa

- São declaradas através da palavra-chave def, seguida pelo nome da função

- Funções podem aceitar:
  . parâmetros, que são variáveis usadas na declaração da função
	. argumentos, que são valores reais passados para a função quando ela é chamada 

- O bloco de código indentado é o que define o comportamento da função 

- A instrução return é utilizada dentro de funções para retornar um valor específico quando a 
função é chamada. É opcional, caso a função não precise retornar um valor específico (sendo que se nada for especificado, é retornado None por default)
```

&nbsp

↳ Sintaxe básica para a declaração e a chamada de uma função

```py

# Declaração da função
def nome_da_funcao(parametro):
  # Corpo da função
  return valor_de_retorno 
  
# Chamada da função
nome_da_funcao(argumento)  
```

&nbsp

↳ Criando e chamando uma função

```py

def multiplicacao(a, b):
  calculo = a * b
  return calculo

resultado = multiplicacao(4, 5)  
print(resultado)  

# Retorna: 20
```

&nbsp;  

↳ Exercício: Criar funções para cálculo de notas de alunos, sendo que:  
&nbsp;&nbsp; ◦ A atividade prática deve ter peso de 40%.  
&nbsp;&nbsp; ◦ O exame final deve ter peso de 60%.  
&nbsp;&nbsp; ◦ Deve ser informado se o aluno foi aprovado ou não na disciplina (a média da escola é 7).  

```py 

def solicitarNotas():
    nota_obtida_pratica = float(input('Por favor, informe a nota '
                                      'obtida na atividade prática: '))
    nota_obtida_exame = float(input('Por favor, informe a nota obtida no'
                                    ' exame final: '))
    return nota_obtida_pratica, nota_obtida_exame

def calcularNotas(nota_obtida_pratica, nota_obtida_exame,
                  pesoPratica = 0.4, pesoExame = 0.6):
   nota_efetiva_pratica = nota_obtida_pratica * pesoPratica
   nota_efetiva_exame = nota_obtida_exame * pesoExame
   return nota_efetiva_pratica, nota_efetiva_exame

def exibirResultado():
    nota_final = nota_efetiva_pratica + nota_efetiva_exame
    print('\nDesempenho do aluno:')
    print(f'1ª avaliação: {nota_efetiva_pratica}')
    print(f'2ª avaliação: {nota_efetiva_exame}')
    print(f'Nota final obtida: {nota_final}')
    if(nota_final <= 7.0):
        print('Status: Aluno(a) ficou para recuperação')
    else:
        print('Status: Aluno(a) foi aprovado(a)')


nota_obtida_pratica, nota_obtida_exame = solicitarNotas()
nota_efetiva_pratica, nota_efetiva_exame = calcularNotas(nota_obtida_pratica,
                                                         nota_obtida_exame)
exibirResultado()

'''
Saída:

Por favor, informe a nota obtida na atividade prática: 7.5
Por favor, informe a nota obtida no exame final: 6.5

Desempenho do aluno:
1ª avaliação: 3.0
2ª avaliação: 3.9
Nota final obtida: 6.9
Status: Aluno(a) ficou para recuperação
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>