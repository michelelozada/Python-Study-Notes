> **Biblioteca math**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### A - Importando a biblioteca math
```py

import math
```

&nbsp;  

### B - Retorno do maior e do menor inteiro de um número real:
```py

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

### C - Retornando o máximo divisor comum (MDC) entre dois números
```py

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

### D - Retorno da raiz quadrada de um número
```py

n = float(input('Forneça um número para retorno da sua raiz quadrada: '))
raiz = math.sqrt(n)
print (f'> Resultado: A raiz quadrada de {n} é {raiz:.3f}')


'''
Forneça um número para retorno da sua raiz quadrada: 16
> Resultado: A raiz quadrada de 16.0 é 4.000
'''
```

&nbsp;  

### E - Cálculo da potência de um número
```py

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

### F - Retorno do fatorial de um número
```py

num = int(input('Forneça um número para que seja retornado seu fatorial: '))
print(f'> Resultado: {num}! = {math.factorial(num)}')


'''
Forneça um número para que seja retornado seu fatorial: 5
> Resultado: 5! = 120
'''
```

&nbsp;  

### G - Informando o valor da constante pi
```py

print('> Número Pi (π) é um número irracional cujo valor é',math.pi)


# > Número Pi (π) é um número irracional cujo valor é 3.141592653589793
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>