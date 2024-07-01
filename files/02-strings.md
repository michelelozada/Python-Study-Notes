> **Strings**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Strings em Python *(mini-revisão)*
```
- Classe associada: str

- Representa uma sequência de caracteres/texto

- É representado no código através do uso de aspas simples ou duplas

- Objetos do tipo str são imutáveis, ou seja, não podem ser alterados após a sua criação. Portanto, qualquer operação que pareça estar alterando uma string, na verdade, está retornando uma nova string com estas alterações aplicadas 

- Uma string é uma sequência de caracteres, sendo que cada caractere possui um índice associado que começa em 0 e vai até o comprimento da string menos um

- Caracteres individuais de uma string podem ser acessados através dos seus índices correspondentes

- Já partes maiores de strings podem ser extraídas através da operação chamada slicing (ou fatiamento), que se refere basicamente a um intervalo de índices

- Outras operações com strings podem ser de:
  . comparação (realizadas com os operadores de comparação)
  . concatenação (realizadas com o operador +)
  . repetição (realizada com o operador *)
  
- Além da utilização do operador +, as strings podem tambpem ser concatenadas através dos métodos str() e join()

- Strings podem ser formatadas através do método format() ou da sintaxe f-string
````

&nbsp;  

## Métodos da classe `str` *(referência rápida)* 

#### • Para verificação de conteúdo de strings:

Método | Função
---    | :--
isalnum() | Retorna True se todos os caracteres da string forem letras ou dígitos
isalpha() | Retorna True se todos os caracteres da string forem letras e se string não está vazia
isdigit() | Retorna True se todos os caracteres da string forem dígitos
islower() | Retorna True se todos os caracteres da string estiverem em minúsculas
isspace() | Retorna True se todos os caracteres da string forem espaços em branco
isupper() | Retorna True se todos os caracteres da string estiverem em maiúsculas

&nbsp;  

#### • Para manipulação de conteúdo/formatação:
Método | Função
---    | :--
capitalize() | Retorna uma cópia da string com o 1º caractere apenas em maiúscula
format() | Formata uma string
join() | Junta os elementos de um iterável em uma string única, usando a string original como separador
lower() | Converte os caracteres de uma string para minúsculas
lstrip() | Remove espaços em branco do início de uma string 
replace(old, new) | Substitui a ocorrência da substring antiga por outra ali informada
rstrip() | Remove espaços em branco do final de uma string 
split() | Divide a string em uma lista de substrings usando o separador informado
strip() | Remove espaços em branco (ou outros caracteres especificados) do início e do fim da string 
title() | Retorna uma cópia da string com o 1º caractere de cada palavra da seuência em maiúscula
upper() | Retorna uma cópia da string em maiúsculas

&nbsp;  

#### • Para pesquisa de conteúdo:
Método | Função
---    | :--
count() | Retorna o número de ocorrências da substring informada 
endswith() | Retorna True se a string termina com o sufixo especificado
find() | Retorna o índice da 1ª ocorrência da substring informada ou -1 se não for encontrada
index() | Mesma função do método `find()`, mas retorna erro ValueError se a substring não for encontrada
startswith(prefix) | Retorna True se a string começa com o prefixo especificado

&nbsp;  

## Acessando caracteres em uma string

Em Python, caracteres individuais em uma string podem ser acessados através de números inteiros conhecidos como índices, lembrando que: 
&nbsp;&nbsp; . indexação de strings começa em 0
&nbsp;&nbsp; . há suporte para índices negativos, que contam a partir do final da string, como -1 e assim sucessivamente
&nbsp;&nbsp; . caracteres específicos podem ser acessados através de string[indice], sendo índice a posição do caractere desejado

```py
palavra = "Python"

print(palavra[0])  # Saída: 'P'
print(palavra[3])  # Saída: 'h'
print(palavra[-2]) # Saída: 'o'
```
  
&nbsp;

## Slicing (ou fatiamento) 

Através desta operação, é possível extrair partes maiores de uma string. O intervalo de índices deve ser definido usando a sintaxe `string[inicio:fim:passo]`, sendo: 
&nbsp;&nbsp; . inicio onde o fatiamento começa (inclusive) 
&nbsp;&nbsp; . fim onde o fatiamento termina (exclusive)
&nbsp;&nbsp; . passo é o intervalo entre os índices a ser considerado (opcional)
\* Se o inicio for omitido, Python assume 0. Se fim for omitido, Python assume o final da string.

&nbsp;

↳ Slicing básico
```py

palavra = "Python"
print(palavra[2:5])

# Extraiu: tho
```

&nbsp; 

↳ Slicing com índices negativos  
*Repare que no exemplo abaixo, extrai a partir do terceiro último até o final da string*  
```py

palavra = "Python"
print(palavra[-3:])

# Extraiu: hon
```

&nbsp; 

↳ Slicing com passo  
*Repare que no exemplo abaixo, capta o 1º caractere, pula o 2º, capta o 3º, e assim por diante*  
```py

palavra = "Python"
print(palavra[::2])

# Extraiu: Pto
```

&nbsp; 

↳ Slicing reverso  
*Inverte a string*
```py

palavra = "Python"
print(palavra[::-1])

# Extraiu: nohtyP
```

&nbsp; 

## Outras operações com strings 

#### • 1 - Operações de comparação  
*Realizadas com os operadores de comparação*  

```py

print('bom' < 'dia')  # Saída: True
print('bom' == 'dia') # Saída: False
print('bom' > 'dia')  # Saída: False
print('dia' == 'dia') # Saída: True
```

&nbsp;

#### • 2 - Operações de concatenação 
*Realizada com o operador `+`ou `+=`*

```py

nome = 'Denzel' + ' ' + 'Washington'
profissao = 'ator e produtor'

print(nome)  # Saída: Denzel Washington
print(nome + ', ' + profissao) 

# Saída: Denzel Washington, ator e produtor
```

```py

s1 = 'hidro'
s2 = 'elétrica'
s1 += s2
print(s1) 

# Saída: hidroelétrica
```

&nbsp;  

#### • 3 - Operações de repetição  
*Realizada com o operador `*`*

```py

frase = ('Vamos sentir saudades. Volte logo' + '!' * 3)

print(frase) 

# Saída: Vamos sentir saudades. Volte logo!!!
```

&nbsp;

## Concatenando strings 

#### • 1 - Através do método str() 

```py

print('No ' + str(6) + 'º dia do evento, apenas ' + str(25) + '% dos convidados participaram.) 

# Saída: No 6º dia do evento, apenas 25% dos convidados participaram.
```

&nbsp; 


#### • 2 - Através do método join()
```py

bandasAnos80 = ['The Cure', 'The Smiths', 'New Order', 'Joy Division']
s = ' - '.join(bandasAnos80)
print(s)

# Saída: The Cure - The Smiths - New Order - Joy Division
```

&nbsp;

## Formatando strings 

#### • 1 - Através do método format()
```py

name = 'Luísa Dias'
age = 18
grade = 9.5
	
print('Aluno(a): {}. Idade: {}. Nota: {}'.format(name,age,grade))

# Saída: Aluno(a): Luísa Dias. Idade: 18. Nota: 9.5
```

&nbsp; 

#### • 2 - Através da sintaxe f-string
Disponível a partir do Python 3.6, esta sintaxe facilita a interpolação de variáveis e expressões diretamente nas strings. Uma f-string deve começar com o prefixo `f` seguido por uma string que deve conter as expressões/variáveis sempre entre chaves. 
```py

estado = "Paraná"
cidade = "Curitiba"
print(f"{cidade} é a capital do {estado}.")

# Saída: Curitiba é a capital do Paraná.
```

&nbsp; 

## Exemplos de aplicações dos métodos para manipular strings em Python

#### • 1 - Método replace
*Substitui a ocorrência de uma substring por outra*

```py

frase_portugues = "Vamos dançar!"
frase_espanhol = frase_portugues.replace('dançar', 'a bailar')
print(frase_espanhol)

# Saída: Vamos a bailar!
```

↳ No exemplo abaixo o método replace() é encadeado para mudar letra a letra uma string
```py
palavra_portugues = "dançar"
palavra_espanhol = palavra_portugues.replace('d', 'b') \
                                    .replace('a', 'a') \
                                    .replace('n', 'i') \
                                    .replace('ç', 'l') \
                                    .replace('a','a') \
                                    .replace('r','r')
print(palavra_espanhol)

# Saída: bailar
```

&nbsp; 

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>