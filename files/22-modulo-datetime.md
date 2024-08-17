> **Módulo datetime**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Módulo datetime do Python *(mini-revisão)*
```
- O módulo datetime é um módulo que contém classes e funções para manipulação de datas e horas em Python

- Suas principais classes são: 
  date (representa uma data sem informação da hora)
  time (representa uma hora sem informação da data)
  datetime (representa data e hora)
  timedelta (representa diferenças entre datas e horas)

- Já que faz parte da biblioteca padrão do Python, para utilizá-la, basta utilizar a instrução: import datetime

- Depois de importá-lo, já é possível acessar todas as funcionalidades deste módulo, prefixando-as sempre com 
datetime. 

- Também é posível utilizar importar apenas partes específicas de um módulo. Por ex: from datetime import time. Com 
isso apenas esta classe é importada, permitindo usar suas funções, sem a necessidade de prefixá-la com datetime.
```




&nbsp;  

#### Obtendo a data e hora atual 

↳ Criando um objeto datetime para o momento atual

```py 

from datetime import datetime

agora = datetime.now()
print("Agora:", agora)

'''
Agora: 2024-07-27 11:23:16.157642
'''
```

↳ Formatando a data e hora obtida acima 
```py 

data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)

'''
Data formatada: 27/07/2024 11:23:16
'''
```

&nbsp;  

#### Extraindo ano, mês e dia da data atual 

```py 

import datetime

# Extração da data atual
data_atual = datetime.date.today()
print(data_atual)

'''
2024-07-27
'''

# Extração do ano, mês e dia  (1ª forma)
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day
print(f'{dia}/{mes}/{ano}')

'''
27/7/2024
'''

# Extração do ano da data atual (2ª forma)
ano_atual = datetime.date.today().year
mes_atual = datetime.date.today().month
dia_atual = datetime.date.today().day
print(f'{dia_atual}/{mes_atual}/{ano_atual}')

'''
27/7/2024
'''

# Retorna um número de 0 (segunda) a 6 (domingo)
dia_semana = data_atual.weekday()
print(dia_semana)

'''
5 (obs: hoje é sábado! :)
'''

# Data no formato ISO 8601
data_isoformat = data_atual.isoformat()
print(data_isoformat)

'''
2024-07-27
'''
```

&nbsp;  

#### Adicionando dias a uma data atual

```py

from datetime import datetime, timedelta

atual_data = datetime.now()
print("Data atual:", atual_data)

'''
Data atual: 2024-07-27 11:32:47.112983
'''

# Adicionando 5 dias à data atual
futura_data = atual_data + timedelta(days=5)
print("Data futura:", futura_data)

'''
Data futura: 2024-08-01 11:32:47.112983
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>