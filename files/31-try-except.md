> **Estrutura Try Except**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão

### Bloco `try... except... finally`
- Utilizado para tratar as exceções/erros que podem ocorrer durate a execução de um bloco de código  
- Evita que um programa termine abruptamente em virtude de um erro que não foi previsto
- Fornece feedback ao usuário, de modo que este pode corrigir a entrada

&nbsp;  

#### Estrutura básica
```py

try:
	# Bloco de código que pode causar um erro

except:
	# Bloco de código com o tratamento da exceção acima 
	
finally:
  # Bloco de código que será executado sempre, indepentemente de erros. É opcional!
```

&nbsp;  

### ValueError		
- É uma exceção em Python, lançada quando uma função recebe um '**argumento de tipo correto, mas com um valor inapropriado**'  
- Ocorre quando a função recebe um valor específico que não pode ser processado adequadmente devido ao valor fornecido

```py

try:
  numero = int(input("Por favor, Digite um número: "))
  print(numero)
# digitando algo que não possa ser convertido para um inteiro 
except ValueError:
  print("Erro! Eu te avisei que era para digitar um número.")
```

&nbsp;  

### Exercício:
Escreva um algoritmo que leia um número. Este número informado pelo usuário deve necessariamente estar compreendido
no intervalo de 1 a 50 (ambos inclusos). Além disso, você deve usar um tratamento de exceção para evitar que o programa
seja abortado, caso o usuário digite um valor não-numérico.  

```py 

while True:
	try:
	  n = int(input("Digite um número: "))
		if (n>= 1 and n<=50):
		  print(f'> Resposta aceita: você informou um número dentro do intevalo.\n')
			break
		else:
			print('> Houve um erro: você informou um número fora do intervalo entre 1 e 50. Por favor, tente novamente.\n')
			continue
	except ValueError:
		print('> Houve um erro: o valor digitado não é um número. Por gentileza, comece novamente.\n')
		continue


'''
Outputs possíveis:
Digite um número: -55
> Houve um erro: você informou um número fora do intervalo entre 1 e 50. Por favor, tente novamente.

Digite um número: dez
> Houve um erro: o valor digitado não é um número. Por gentileza, comece novamente.

Digite um número: 25
> Resposta aceita: você informou um número dentro do intevalo.

'''
```

&nbsp;  

### Exercício:
Considerando os divisores abaixo, trate os erros que podem acontecer a fim de evitar que programa seja abortado
durante o procesamento das divisões:  

```py 
cont = 1
dividendo = 2
divisores = ['DIV',0,1,1.5]

for d in divisores:
	try:
		quociente = dividendo / d
		print(f'{cont}º resultado: O resultado da divisão de {dividendo} com {d} é {quociente:.2f}')
		cont += 1

	except TypeError:
		print(f'{cont}º resultado: O valor {d} é inválido para esta operação (motivo: não é possível realizar divisão com '
					f'valores não-numéricos).')
		cont += 1

	except ZeroDivisionError:
		print(f'{cont}º resultado: O valor 0 é inválido para esta operação (motivo: não é possível dividir um '
					f'número por zero).')
		cont += 1

'''
Output: 
1º resultado: O valor DIV é inválido para esta operação (motivo: não é possível realizar divisão com valores não-numéricos).
2º resultado: O valor 0 é inválido para esta operação (motivo: não é possível dividir um número por zero).
3º resultado: O resultado da divisão de 2 com 1 é 2.00
4º resultado: O resultado da divisão de 2 com 1.5 é 1.33
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>