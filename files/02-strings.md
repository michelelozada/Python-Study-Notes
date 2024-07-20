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
  
- Além da utilização do operador +, as strings podem também ser concatenadas através dos métodos str() e join()

- A interpolação de strings pode ser feita através do operador %, do método format() ou das f-strings
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
zerofill() | Preenche uma string com zeros à esquerda até que ela atinja um comprimento especificado

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

nome = 'Denzel Washington'
profissao = 'ator e produtor'
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

print('se essa rua\n' * 2 + '  fosse minha')
print('eu mandava\n' * 2 + '  ladrilhar')
print('com pedrinhas\n' * 2 + '  de brilhantes')
print('para o meu\n' * 2 + '  amor passar.')

'''
Saída: 
se essa rua
se essa rua
  fosse minha
eu mandava
eu mandava
  ladrilhar
com pedrinhas
com pedrinhas
  de brilhantes
para o meu
para o meu
  amor passar.
'''
```

&nbsp;

## Concatenação de strings 
Refere-se à junção direta de duas ou mais strings para formar uma única string. Além da utilização do operador `+`, explicado acima, também é possível fazer isso das formas abaixo.

&nbsp;

#### • 1 - Através do método str() 

```py

dias = 6
participacao = 25


print('No ' + str(dias) + 'º dia do evento, apenas ' + str(participacao) + '% dos convidados participaram.')
```

&nbsp; 


#### • 2 - Através do método join()
```py

lista_bandas = [
    'The Cure', 'The Smiths', 'New Order', 'Joy Division'
]
bandas_anos80 = ' - '.join(lista_bandas)
print(bandas_anos80)

# Saída: The Cure - The Smiths - New Order - Joy Division
```

&nbsp;

## Interpolação de strings 
É uma forma de incorporar valores de variáveis em strings, podendo ser feita das maneiras abaixo.

&nbsp;

#### • 1 - Através do operador %
É o método mais antigo de formatar uma string, sendo necessário especificar também o tipo de dado que será inserido na string.

```py

nome = "Enzo"
meses = 4
peso = 6.400

frase = "%s é um lindo bebê de %i meses, que pesa %.1f quilos!" % (nome, meses, peso)
print(frase)

Saída: Enzo é um lindo bebê de 4 meses, que pesa 6.4 quilos!
```

&nbsp;

#### • 2 - Através do método format()
```py

nome = 'Luis'
idade = 35
score = 9.545

print('Cliente: {}. Idade: {} anos. Score: {:.2f}'.format(nome, idade, score))

# Saída: Cliente: Luis. Idade: 35 anos. Score: 9.54
```

&nbsp; 

#### • 3 - Através da sintaxe format-string (f-strings)
Disponível a partir do Python 3.6, esta sintaxe facilita a interpolação de variáveis e expressões diretamente nas strings. Uma f-string deve começar com o prefixo `f` seguido por uma string que deve conter as variáveis sempre entre chaves. 

```py

nome = 'Antônio'
idade = 55
score = 9.987

print(f'Cliente: {nome}. Idade: {idade} anos. Score: {score:.2f}')

# Saída: Cliente: Antônio. Idade: 55 anos. Score: 9.99
```

&nbsp; 

↳  Para casos em que é necessário preencher zeros à esquerda
```py

nome = 'James Bond'
codigo = 7

# código deve ocupar 3 espaços
print(f'{nome}, agente {codigo:03}') 

# Saída: James Bond, agente 007
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

#### • 2 - Método zerofill() 
*Preenche uma string com zeros à esquerda até que ela atinja um comprimento especificado*

```py

nome = 'James Bond'
codigo = 7

print('{}, agente {}'.format(nome, str(codigo).zfill(3)))

# Saída: James Bond, agente 007
```

&nbsp; 

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>