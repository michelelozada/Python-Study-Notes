> **Módulo math**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão sobre o módulo math do Python
```
- O módulo math é uma ferramenta útil para lidar com operações e cálculos matemáticas em Python

- Já que faz parte da biblioteca padrão do Python, para utilizá-la, basta utilizar a instrução: import math

- Depois de importá-lo, já é possível acessar todas as funcionalidades deste módulo, prefixando-as sempre com 
math. Ex: math.ceil(), math.floor(), etc.

- Também é posível utilizar importar apenas partes específicas de um módulo. Por ex: from math import ceil. Com 
isso apenas esta função é importada, permitndo usar a função ceil(), sem a necessidade de prefixá-la com math.
```

&nbsp;  

### Funções importantes disponíveis na biblioteca math do Python.

#### • Funções Matemáticas Básicas

Função | Finalidade 
---    | ---
math.ceil(x) | Retorna o número arredondado para cima (para inteiro mais próximo)
math.floor(x) | Retorna o número arredondado para baixo (para  inteiro mais próximo)
math.pow(x, y) | Retorna x elevado à potência y
math.round(x, n) | Retorna o número x arrendondado para n dígitos decimais
math.sqrt(x) | Retorna a raiz quadrada de x
math.trunc(x.y) | Remove a parte decimal de x, retornando a parte inteira

&nbsp;  

#### • Outras Funções:

Função | Finalidade 
---    | ---
math.factorial(x) | Retorna o fatorial de x
math.isnan(x) | Retorna True se x for NaN (Not a Number)
math.modf(x) | Retorna a parte fracionária e a parte inteira de x

&nbsp;  

> Exemplo: Retorno do maior e do menor inteiro de um número real:
```py

import math

n = float(input('Informe um número real: '))
print(f'> O maior inteiro do número {n} é',math.ceil(n))
print('> Já o menor inteiro deste número é',math.floor(n))


'''
Informe um número real: 3.5
> O maior inteiro do número 3.5 é 4
> Já o menor inteiro deste número é 3
'''
```

&nbsp;  

> Exemplo: Retornando o máximo divisor comum (MDC) entre dois números
```py

import math

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print(f'> O máximo divisor comum (MDC) entre os números {n1} e {n2} é {math.gcd(n1,n2)}.')


'''
Informe o primeiro número: 18
Informe o segundo número: 60
> O máximo divisor comum (MDC) entre os números 18 e 60 é 6.
'''
```

&nbsp;  

> Exemplo: Retorno da raiz quadrada de um número
```py

import math

n = float(input('Forneça um número para retorno da sua raiz quadrada: '))
raiz = math.sqrt(n)
print (f'> Resultado: A raiz quadrada de {n} é {raiz:.3f}')


'''
Forneça um número para retorno da sua raiz quadrada: 16
> Resultado: A raiz quadrada de 16.0 é 4.000
'''
```

&nbsp;  

> Exemplo: Cálculo da potência de um número
```py

import math

n = int(input('Informe a base: '))
p = int(input('Qual o valor do expoente? '))
print(f'> O número {n} elevado à {p}ª potência é {(math.pow(n,p))}')


'''
Informe a base: 3
Qual o valor do expoente? 2
> O número 3 elevado à 2ª potência é 9.0
'''
```

&nbsp;  

> Exemplo: Retorno do fatorial de um número
```py

import math

num = int(input('Forneça um número para que seja retornado seu fatorial: '))
print(f'> Resultado: {num}! = {math.factorial(num)}')


'''
Forneça um número para que seja retornado seu fatorial: 5
> Resultado: 5! = 120
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>