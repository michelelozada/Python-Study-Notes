> **Escopo**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Resumo sobre Desvio condicional em Python
```
- Escopo refere-se à região onde uma variável (ou uma função) é acessível.

- Existem dois tipos de escopo:
  . Um no qual as variáveis e funções podem ser acessadas de qualquer lugar do programa, incluindo de dentro das funções - tendo elas, portanto, escopo global.
	. Outro no qual as variáveis só podem ser acessadas dentro de funções - tendo elas, portanto, escopo local. 
	
- As funções têm acesso a variáveis definidas no escopo global, mas as variáveis definidas dentro de uma função não são acessíveis fora dela, a menos que sejam explicitamente passadas para fora da função (por meio de valores de retorno) ou usadas dentro de outras funções (por meio de argumentos)	
```	

&nbsp;  

>> No exemplo abaixo: Repare que a variável local não afeta a variável global

```py 

x = 10  # Variável global

def minhaFuncao():
  x = 20  # Variável local

minhaFuncao()
print(x)  

# Saida: 10
```

&nbsp;  

>> No exemplo abaixo: Repare que a palavra-chave `global` é usada para declarar que uma variável dentro de uma função está se referindo a uma variável no escopo global, em vez de ser criada uma nova variável local com o mesmo nome.

```py 

x = 10  # Variável global

def minhaFuncao():
  global x  # Declarando que queremos usar a variável global x
  x = 20    # Modificando a variável global x

minhaFuncao()
print(x)  

# Saída: 20
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>