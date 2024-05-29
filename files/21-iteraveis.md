> **Iteráveis**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Iteráveis  
São os objetos que podem ser percorridos sequencialmente (= iterados), permitindo o acesso a seus elementos um de cada vez. Dessa forma, iteração é a passagem pelo bloco de código dentro do loop.    

&nbsp;  

## Iteráveis em Python
São os seguintes:   

&nbsp;  

### Strings: 
```py

word = "Github"
for letter in word:
  print(letter)
	
Retorna: 
G
i
t
h
u
b
```

&nbsp;  

### Listas: 
```py

lista = [5, 10, 15, 20]
for item in lista:
  print(item)


Retorna: 
5
10
15
20	
```		

&nbsp;  

### Tuplas: 
```py

tupla = [5, 10, 15, 20]
for item in tupla:
  print(item)

Retorna: 
5
10
15
20	
```		

&nbsp;  

### Dicionários: 
```py

dicionario = {'jan': 1, 'fev': 2, 'mar': 3}
for chave in dicionario:
  print(chave, dicionario[chave])
	
Retorna:	
jan 1
fev 2
mar 3
```		

&nbsp;  

### Conjuntos: 
```py

conjunto = {1, 3, 6, 9}
for item in conjunto:
  print(item)  

Retorna: 
1
3
6
9
```		

&nbsp;  

### Range: 
```py

for numero in range(5):
  print(numero)

Retorna: 
0
1
2
3
4
```		
**Notas:**
- **`for`** = é a keyword que inicia o loop
- **variável de iteração (ou variável de loop)** =  é a variável que, a cada iteração do loop, asssume um valor sucessivo gerado pela função `range()`. No exemplo acima, é a partícula `numero`
- **`in`** = é a keyword que indica que a variável de iteração será iterada sobre o iterável
- **range()** = é a função que gera um iterável de números. No exemplo acima começa de 0 (implícito) e vai até o número informado 5 (exclusive).

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>