> **Strings**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
```py

citacao = 'devemos julgar um homem mais pelas suas perguntas que pelas respostas.'  
autor = 'voltaire'  
nome = 'françois marie-arouet'  
oficio = 'ESCRITOR E FILÓSOFO FRANCÊS DO SÉCULO 18'  
```

&nbsp;  

### 1 - Informando o conteúdo de um índice
```py

print(citacao[8])  # output: j
```

&nbsp;  

### 2 - Informando o conteúdo de um intervalo
```py

print(citacao[15:24])  # um homem
```

&nbsp;  

### 3.1 - Iterando a string autor, de forma semelhante ao loop foreach de outras linguagens de programação
```py

for i in autor:
    print(i)
		
'''
v
o
l
t
a
i
r
e
'''
```

&nbsp;  

### 3.2 - Iterando novamente a string autor, mas agora através de indexação
```py

letra = 1
for i in range(0,len(autor)):
    print(str(letra) + 'ª letra -> ' + autor[i])
    letra += 1
		
'''
1ª letra -> v
2ª letra -> o
3ª letra -> l
4ª letra -> t
5ª letra -> a
6ª letra -> i
7ª letra -> r
8ª letra -> e
'''
```

&nbsp;  

### 4 - Fazendo as verificações a respeito do tipo de caracteres  que as strings autor e ofício contêm:
```py

print(autor.islower()) # True -> essa string possui somente caracteres minúsculos
print(oficio.isupper()) # True -> essa string possui somente caracteres maiúsculos
```

&nbsp;  

### 5 - Informando qual o número de ocorrências da letra 's' na string frase e em que posição ela aparece pela primeira vez
```py

print(citacao.count('s')) # 10 -> ocorre 10 vezes nesta string
print(citacao.index('s')) # 6 -> ocorre pela primeira vez no índice de nº 6
```

&nbsp;  

### 6 - Tornando maiúscula apenas a primeira letra da string frase
```py

citacao_nova = citacao.capitalize()
print(citacao_nova)

# Devemos julgar um homem mais pelas suas perguntas que pelas respostas.
```

&nbsp;  

### 7 - Tornando maiúsculas todas as letras da string autor
```py

autor_novo = autor.upper()
print(autor_novo) # VOLTAIRE
```

&nbsp;  

### 8 - Tornando maiúsculas todas as primeiras letras das palavras da string nome
```py

nome_novo = nome.title()
print(nome_novo) # François Marie-Arouet
```

&nbsp;  

### 9 - Tornando minúsculas todas as letras da string oficio
```py

oficio_novo = oficio.lower()
print(oficio_novo) # escritor e filósofo francês do século 18
```

&nbsp;  

### 10 - Substituindo as palavras escritor, filósofo e 18 da string oficio por ensaísta, pensador e XVIII:
```py

oficio_novo2 = oficio_novo.replace('escritor','ensaísta').replace('filósofo','pensador').replace('18','XVIII')
print(oficio_novo2)

# ensaísta e pensador francês do século XVIII
```

&nbsp;  

### 11 - Imprimindo a versão da citação
```py

print('\"'+citacao_nova+'\"\n'+autor_novo+' (pseudônimo de',nome_novo+'),',oficio_novo2)

'''
"Devemos julgar um homem mais pelas suas perguntas que pelas respostas."
VOLTAIRE (pseudônimo de François Marie-Arouet), ensaísta e pensador francês do século XVIII
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>