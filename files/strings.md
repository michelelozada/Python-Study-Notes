> **Strings**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Revisão sobre strings em Python
```
- Classe associada: str

- Representa uma sequência de caracteres/texto

- Objetos do tipo str são imutáveis 

- É representado no código através do uso de aspas simples ou duplas

- Caracteres individuais de uma string podem ser acessados através dos índices (o 1º caractere de uma string está no índice 0)

- A técnica do fatiamento (slicing) extrai partes específicas de uma string

- As operação de string são:
	. comparação (com operadores de comparação)
	. concatenação (com operador +)
	. formatação (com métodos como format ou f-string)
	. repetição (com operador *)
````

&nbsp;  

## Formatação através das f-strings

Forma de formatar strings em Python, disponível a partir do Python 3.6
Facilita a interpolação de variáveis e expressões diretamente nas strings 
Uma f-tring deve começar com o prefixo `f`, seguida por uma string que deve conter as expressões/variáveis entre chaves. 
```py

estado = "Paraná"
cidade = "Curitiba"
print(f"{cidade} é a capital do {estado}.")

# Saída: Curitiba é a capital do Paraná.
```

&nbsp;

### • Comparando strings
```py

print('bom' < 'dia') # True
print('bom' == 'dia') # False
print('bom' > 'dia') # False
print('dia' == 'dia') # True
```

&nbsp;

## Concatenação: operadores e métodos  

&nbsp;

### 1 - Operador +
```py

nome = 'Denzel' + ' ' + 'Washington'
profissao = 'ator e produtor norte-americano'

print(nome)  # Denzel Washington
print(nome + ', ' + profissao) # Denzel Washington, ator e produtor norte-americano
```

&nbsp; 

### 2 - Operador +=
```py

s1 = 'hidro'
s2 = 'elétrica'
s1 += s2

print(s1) # hidroelétrica
```

&nbsp; 

### 3 - Operador *
```py

frase = ('Vamos sentir saudades. Volte logo' + '!' * 3)

print(frase) # Vamos sentir saudades. Volte logo!!!
```

&nbsp; 

### 4 - Método str()
```py

print('No ' + str(6) + 'º dia do evento, apenas ' + str(25) + '% dos convidados participaram dos ' + str(10) + ' seminários.')
# No 6º dia do evento, apenas 25% dos convidados participaram dos 10 seminários.
```

&nbsp; 

### 5 - Método format()
```py

name = 'Luísa Dias'
age = 18
grade = 9.5
	
print('Aluno(a): {}. Idade: {}. Nota: {}'.format(name,age,grade))
# Aluno(a): Luísa Dias. Idade: 18. Nota: 9.5

print(f'Aluno(a): {name}. Idade: {age}. Nota: {grade}') # Disponível a partir da versão 3.6 do Python!
# Aluno(a): Luísa Dias. Idade: 18. Nota: 9.5
```

&nbsp; 

### 6 - Método join()
```py

bandasAnos80 = ['The Cure', 'The Smiths', 'New Order', 'Joy Division']
s = ' - '.join(bandasAnos80)

print(s)
```

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