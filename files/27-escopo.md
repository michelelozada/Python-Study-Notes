> **Escopo**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### 1 - Escopo global vs. escopo local
```py 

x = 'global' # variável de escopo global
def minhaFuncao():
    x = 'local' # variável de escopo local
    print(x)

# Evocando a função
minhaFuncao()
# Print da variável x
print(x)

''' Output:
local
global
'''
```

&nbsp;  

### 2 - Utlização da global keyword
```py 

x = 'global'
def minhaFuncao():
    global x
    x = 'local'
    print(x)

minhaFuncao()
print(x)

''' Output:
local 
local
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>