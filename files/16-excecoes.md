> **Gerenciamento de exceções**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Gerenciamento de exceções em Python *(mini-revisão)*
```
- As instruções try, except e finally são utilizadas para lidar com exceções (erros durante a execução de um programa),  
permitindo sua captura e tratamento de forma controlada.

- Esse tratamento evita, portanto que um programa termine abruptamente em virtude de uma exceção que não foi prevista, 
fornecendo também um feedback ao usuário, de modo que este possa corrigir sua ação com outra entrada adequada
```

&nbsp;  

#### ↳ Sintaxe básica
```py

try:
	# Bloco de código que pode vir a gerar uma exceção

except:
	# Se tiver havido um erro, esse bloco de código irá lidar com tratamento da exceção
	
finally:
# Essa instrução é opcional. Se existir, o bloco de código aqui será executado sempre, indepentemente de ter havido um exceção ou não
```

&nbsp;  

## ValueError		

É uma exceção em Python, lançada quando uma função ou operação recebe um **argumento que tem o tipo correto, mas o valor inapropriado**.

&nbsp;  

↳ Considerando o exemplo abaixo em que é solicitada uma entrada do usuário: se esta for diferente de um número (como `int` ou `float`), um `ValueError` será lançado, pois a entrada não poderá ser processada adequadamente.

```py

try:
  numero = int(input("Por favor, digite aqui um número: "))
  print(numero)
# Para o caso da entrada de valor que não possa ser convertido para um inteiro 
except ValueError:
  print("Eu te avisei que era para digitar um número!")
```

&nbsp;  

↳ Exercício: Escreva um algoritmo que leia um número. Este número informado pelo usuário deve necessariamente estar compreendido no intervalo de 1 a 50 (ambos inclusos). Além disso, você deve usar um tratamento de exceção para evitar que o programa seja abortado, caso o usuário digite um valor não-numérico.  


```py 

while True:
  try:
    numero = int(input("Por favor, digite um número de 1 a 50: "))
    if(1 <= numero <= 50):
      print("Resposta aceita!")
      break
    else:
      print("Este número está fora do intervalo proposto.\n")
  except ValueError:
    print("Por gentileza, digite apenas números.\n")
```

&nbsp;  

↳ Exercício: Considerando os divisores abaixo, trate os erros que podem acontecer a fim de evitar que programa seja abortado
durante o procesamento das divisões:  

```py 

dividendo = 2
divisores = ['DIV', 0, 1, 1.5]

for divisor in divisores:
    try:
        quociente = dividendo / divisor
        print(f"O resultado da divisão de {dividendo} por {divisor} é {quociente:.2f}")
        print("")

    except TypeError as e:
        print(f'O valor {divisor} é inválido para esta operação')
        print("Motivo: Não é possível realizar divisão com valores não-numéricos")
        print("")

    except ZeroDivisionError as e:
        print(f'O valor {divisor} é inválido para esta operação')
        print("Motivo: Não é possível dividir um número por zero/n")
'''
Saída: 

O valor DIV é inválido para esta operação
Motivo: Não é possível realizar divisão com valores não-numéricos

O valor 0 é inválido para esta operação
Motivo: Não é possível dividir um número por zero/n
O resultado da divisão de 2 por 1 é 2.00

O resultado da divisão de 2 por 1.5 é 1.33
'''
```

&nbsp;

## Usando o `as error` dentro de uma cláusula bloco except

Este recurso permite acessar informações adicionais sobre o erro. Útil para quando é necessário não apenas identificar o tipo de exceção que ocorreu, mas também acessar informações adicionais sobre a exceção. 

```py

try:
  resultado = 10 / 0
# Captura da exceção ZeroDivisionError e atribuição à variável 'error'  
except ZeroDivisionError as error:
  print(f'Ocorreu um erro: {error}')
    
# Saída: Ocorreu um erro: division by zero    
```    

&nbsp;

## Customizando exceções com raise

A palavra chave `raise` é usada para gerar exceções em Python.
Ela permite sinalizar que um erro ocorreu e precisa ser tratado.
Pode ser usada para lançar exceções personalizadas.


```py

def efetuar_divisao(x, y):
  if y == 0:
    raise ValueError("Não é possível dividir por zero.")
  return x / y

try:
  resultado = efetuar_divisao(20, 0)
except ValueError as e:
  print(f"Erro: {e}")
    
# Erro: Não é possível dividir por zero.
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>