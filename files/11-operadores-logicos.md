> **Operadores lógicos**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Operadores Lógicos *(mini-revisão)*
```
- Usados para combinar e modificar valores booleanos para criar expressões lógicas mais complexas

- Normalmente são usados em instruções condicionais e em avaliações de expressões booleanas
```

&nbsp;  

### • E lógico (and)
*Retorna True somente se os operandos forem True*

&nbsp;  

↳ Representação da tabela verdade para o operador `and`:
```py

print(True and True) 
# Saída: True

print(True and False) 
# Saída: False

print(False and True) 
# Saída: False

print(False and False) 
# Saída: False
```

&nbsp;  

↳ Exemplos:
```py

print((3 < 2) and (2 == 2)) 
# Saída: False

print(1 + 1 == 2 and len("bola") == 4) 
# Saída: True

print(1 + 1 > 2 and 4 != 5) 
# Saída: False

print((True or False) and True) 
# Saída: True

print((True and False) and True) 
# Saída: False
```

&nbsp;  

### • OU lógico (or)
*Retorna True se pelo menos um dos operandos for True*

&nbsp;  

↳ Representação da tabela verdade para o operador `or`:
```py

print(True or True) 
# Saída: True

print(True or False) 
# Saída: True

print(False or True) 
# Saída: True

print(False or False) 
# Saída: False
```

&nbsp;  

↳ Exemplos:
```py

print((2 > 1) or (3 < 7))  
# Saída: True

print(1 + 1 == 2 or len("bola") == 4) 
# Saída: True

print(1 + 1 != 2 or len("bola") == 4)
# Saída: True

print((True or False) or True) 
# Saída: True

print((True and False) or True) 
# Saída: True
```

&nbsp;  

### • Negação lógica (not)
*Inverte o valor do operando, retornando False se o operando for True e True se o operando for False*

&nbsp;  

↳ Representação da tabela verdade para o operador `not`:
```py

print(not True) 
# Saída: False

print(not False) 
# Saída: True
```

&nbsp;  

↳ Exemplos:
```py

print(not (3 > 2)) 
# Saída: False

print(not (7 < 5)) 
# Saída: True

print(not (4 != 2) and (3 < 6)) 
# Saída: False

print(not True or False) 
# Saída: False

print(not True or True) 
# Saída: True

print(not False or True) 
# Saída: True

print(not True and False) 
# Saída: False
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>