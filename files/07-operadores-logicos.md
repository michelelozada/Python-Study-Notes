> **Operadores e expressões lógicas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  

### 1. Conectivo lógico 'AND'
Tem seu valor lógico verdadeiro somente quando todas as preposições forem verdadeiras  

&nbsp;  

### Representação da tabela verdade para o operador AND:
```py

print(True and True) # Retorna: True
print(True and False) # False
print(False and True) # False
print(False and False) # False
```

&nbsp;  

### 2. Conectivo lógico 'OR'
Tem seu valor lógico verdadeiro quando ao menos uma das preposições for verdadeira  

&nbsp;  

### Representação da tabela verdade para o operador OR:
```py

print(True or True) # Retorna: True
print(True or False) # True
print(False or True) # True
print(False or False) # False
```

&nbsp;  

### 3. Conectivo lógico 'NOT'
Tem o efeito de negar o valor lógico da proposição original  

&nbsp;  

### Representação da tabela verdade para o operador NOT:
```py

print(not True) # False
print(not False) # True
```

&nbsp;  

### 4. Expressões lógicas diversas:
```py

print((3 < 2) and (2 == 2)) # Retorna: False
print(1 + 1 == 2 and len("bola") == 4) # True
print(1 + 1 > 2 and 4 != 5) # False
print((True or False) and True) # True
print((True and False) and True) # False

print((2 > 1) or (3 < 7))  # Retorna: True
print(1 + 1 == 2 or len("bola") == 4) #True
print(1 + 1 != 2 or len("bola") == 4) # True
print((True or False) or True) # True
print((True and False) or True) # True

print(not (3 > 2)) # False
print(not (7 < 5)) # True
print(not (4 != 2) and (3 < 6)) # False
print(not True or False) # False
print(not True or True) # True
print(not False or True) # True
print(not True and False) # False
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>