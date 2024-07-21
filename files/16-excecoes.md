> **Gerenciamento de exceções**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Gerenciamento de exceções em Python *(mini-revisão)*
```
- As instruções try, except e finally são utilizadas para lidar com exceções (erros) em Python,  
permitindo sua captura e tratamento de forma controlada, ao longo da execução de um bloco de código

- Evita, portanto que um programa termine abruptamente em virtude de uma exceção que não foi prevista, 
fornecendo também um feedback ao usuário, de modo que este possa corrigir sua ação com outra entrada adequada
```

&nbsp;  

#### ↳ Sintaxe básica
```py

try:
	# Bloco de código que pode causar um erro

except:
	# Bloco de código com o tratamento da exceção acima 
	
finally:
  # Bloco de código que será executado sempre, indepentemente de erros. É opcional!
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
        print(f"Mais detalhes: {e}")
        print("")

    except ZeroDivisionError as e:
        print(f'O valor {divisor} é inválido para esta operação')
        print("Motivo: Não é possível dividir um número por zero/n")
        print(f"Mais detalhes: {e}")

'''
Saída: 

O valor DIV é inválido para esta operação
Motivo: Não é possível realizar divisão com valores não-numéricos
Mais detalhes: unsupported operand type(s) for /: 'int' and 'str'

O valor 0 é inválido para esta operação
Motivo: Não é possível dividir um número por zero/n
Mais detalhes: division by zero
O resultado da divisão de 2 por 1 é 2.00

O resultado da divisão de 2 por 1.5 é 1.33
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>