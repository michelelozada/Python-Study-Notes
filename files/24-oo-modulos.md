> **Python OO: Módulos**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp; 

## Módulos
São arquivos com a extensão `.py` que podem conter os atributos do módulo, ou seja, as funções, classes, variáveis e código executável. 
&nbsp; 

São essenciais para se trabalhar com a POO para encapsular e organizar código em partes estruturadas e reutilizáveis. 
&nbsp; 

Para utilização em outro arquivo Python, os módulos precisam ser importados através do comando `import`, sendo que o nome do módulo não contém a extensão .py. Feito iss, os atributos do módulo podem ser acessados.
&nbsp; 

### Exemplo: 

arquivo main.py
```py

import modulo_saudacao

mensagem = 'Olá, ' + modulo_saudacao.nome + '!'
modulo_saudacao.saudar_usuario(mensagem)

# Saída: Olá, Michele!
```

&nbsp; 

arquivo modulo_saudacao.py

```py

nome = 'Michele'

def saudar_usuario(mensagem):
  print(mensagem)
```` 

&nbsp; 

Segundo as boas práticas, é importante que apenas partes específicas de um módulo (aquelas que serão efetivamente usadas) sejam importadas.
&nbsp;  

### Exemplo: 

arquivo main.py

```py

from modulo_saudacao import nome, saudar_usuario

mensagem = 'Olá, ' + nome + '!'
saudar_usuario(mensagem)

# Saída: Olá, Michele!
```

&nbsp; 

arquivo modulo_saudacao.py

```py

nome = 'Michele'

def saudar_usuario(mensagem):
  print(mensagem)
```` 

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>