> **Concatenação: operadores e métodos**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
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

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>