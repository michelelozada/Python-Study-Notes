> **Iteráveis**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Iteráveis em Python *(mini-revisão)*
```
- Iteráveis são os objetos que podem ser percorridos (ou seja, iterados), permitindo o acesso a cada 
um de seus itens sequencialmente

- Os principais iteráveis em Python são:
  . Strings
	. Listas 
	. Dicionários
	. Tuplas
	. Sets (conjuntos)
	. Range (intervalos)
	
- Iteráveis e loops estão diretamente correlacionados, pois estes últimos são usados para percorrer os 
elementos de um iterável, normalmente executando uma ação específica para cada um destes itens
```

&nbsp;  

#### ↳ Iterando sobre uma string: 
```py

palavra = "Github"
for letra in palavra:
  print(letra)
	
'''
Saída:
G
i
t
h
u
b
'''
```

&nbsp;  

#### ↳ Iterando sobre uma lista: 
```py

lista = [5, 10, 15, 20]
for numero in lista:
  print(numero)

'''
Saída:
5
10
15
20	
'''
```	

&nbsp;  

#### ↳ Iterando sobre uma tupla: 
```py

tupla = [5, 10, 15, 20]
for numero in tupla:
  print(numero )

'''
Saída:
5
10
15
20	
'''
```		

&nbsp;  

#### ↳ Iterando sobre um dicionário: 
```py

dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave in dicionario:
  print(chave, dicionario[chave])
	
'''
Saída:
a 1
b 2
c 3
'''
```		

&nbsp;  

#### ↳ Iterando sobre um set (conjunto): 
```py

conjunto = {1, 3, 6, 9}
for numero in conjunto:
  print(numero)  

'''
Saída:
1
3
6
9
'''
```		

&nbsp;  

#### ↳ Iterando sobre um range (intervalo): 
```py

for numero in range(5):
  print(numero)

'''
Saída:
0
1
2
3
4
'''
```		

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>