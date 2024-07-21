> **Operadores de pertencimento**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp; 

## Operadores de pertencimento *(mini-revisão)*
```
- Usados para verificar se um elemento está presente ou ausente em estruturas de dados sequenciais 
em Python (como, listas, tuplas, strings, etc.), sendo que:

  . O operador in verifica se um elemento está presente em uma sequência. Retorna True se o valor 
  estiver presente na sequência

  . O operador not verifica se um elemento está ausente em uma sequência. Retorna True se o valor 
  não estiver presente na sequência
```

&nbsp; 

### Verificação da presença ou ausência de elementos em uma string

```py

cidade = "Curitiba"

print('e' in cidade) 
# Saída: False

print('x' not in cidade)
# Saída: True
```

&nbsp; 

### Verificação da presença ou ausência de elementos em uma lista 

```py

frutas = ['abacaxi','amora','uva']

print('laranja' in frutas)
# Saída: False

print('goiaba' not in frutas)
# Saída: True
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>