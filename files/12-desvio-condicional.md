> **Desvio condicional**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Desvio Condicional em Python *(mini-revisão)*
```

- É uma estrutura de decisão, utilizada para realizar testes condicionais e controlar o fluxo do 
programa com base em condições.

- Ou seja, dependendo de se uma condição é avaliada como verdadeira ou como falsa, o programa é 
capaz de tomar decisões e executar (ou não) diferentes blocos de código 

- Em Python, o desvio condicional é implementado, através das seguintes palavras-chave: 
  . if, que verifica se uma condição é verdadeira
	. elif (equivalente ao "else if"), que permite testar outras condições
	. else, que define um bloco de código para tratar dos casos não cobertos pelas condições anteriores

- O desvio condicional pode ser classificado como simples ou composto 

- Também pode ser aninhado ou encadeado (simulando aqui a estrutura switch case de outras linguagens)  

- Em Python, o indentamento apropriado do código é crucial para garantir que os blocos if, elif e else 
sejam executadas corretamente. 
```

&nbsp; 

## Desvio Condicional Simples
Envolve apenas uma condição ser verificada, sendo que executa um bloco de código se essa condição for avaliada como verdadeira.

&nbsp; 

↳ Exemplo da sua estrutura básica:

```py

idade = 20

if idade >= 18:
  print("OK, você é maior de idade!")
```

&nbsp; 

## Desvio Condicional Composto
Deriva do desvio condicional simples, sendo que passa a envolver mais uma ou mais condições e, por conta disso, passa a ter caminhos de execução diferentes, dependendo das condições serem avaliadas como verdadeiras ou falsas. 

&nbsp; 

Isso é expresso através da cláusulas `elif`para o caso de verificações adicionais após a primeira e `else` para capturar qualquer outra condição que não seja coberta pelas anteriores.

&nbsp; 

↳ Exemplo da sua estrutura básica:

```py
if condição:
  # bloco de código que será executado se esta condição for verdadeira
elif condição:
  # bloco de código que será executado se esta condição for verdadeira
else:
  # bloco de código a ser executado se nenhuma das condições acima forem verdadeiras
```

```py

idade = 20

# Condição principal
if idade >= 18:
  print("Você é maior de idade.")
# Condição adicional		
elif idade < 18:
  print("Você é menor de idade.")
# Se nenhuma das condições acima forem verdades	
else:
  print("Idade desconhecida.")
```		

&nbsp; 
		
## Desvio condicional aninhado (aka _nested if_)
Estrutura na qual uma ou mais instruções podem estar associadas a uma outra condição, ou seja, são criadas "combinações de condições" para a execução (ou não) de determinados blocos de código. Dessa forma, é ideal para lidar com múltiplas condições em uma estrutura hierárquica.

&nbsp; 

↳ Exemplo da sua estrutura básica:

```py

idade = 20
tem_carteira_de_motorista = True

# if externo que verifica uma condição geral 
if idade >= 18:
  print("Você tem idade suficiente para dirigir.")
  # if interno que verifica uma condição mais específica
  if tem_carteira_de_motorista:
    print("E você também possui uma carteira de motorista.")
  else:
    print("Mas você não possui uma carteira de motorista.")
else:
  print("Você é menor de idade e não pode dirigir.")
```

&nbsp; 

## Desvio condicional encadeado 
Estrutura na qual instruções independentes são encadeadas uma após a outra, sendo possível testar múltiplas condições em uma sequência linear.

&nbsp; 

Ao se utilizar esta estrutura, é implementado um comportamento similar à estrutura **switch case**, que é encontrada de forma nativa em algumas outras linguagens de programação, mas não no Python.

&nbsp; 

Esta estrutura é ideal para a implementação de um percurso para o usuário - seja através de um menu de opções ou apresentação de alternativas - que o direcionam dentro do programa (ou podem determinar seu encerramento).

&nbsp; 

↳ Exemplo da sua estrutura básica:

```py

opcao = 2

if opcao == 1:
  # Código caso opção 1
elif opcao == 2:
  # Código caso opção 2
elif opcao == 3:
  # Código caso opção 3
elif opcao == 4:
  # Código caso opção 4
elif opcao == 5:
  # Código caso opção 5
# 	
else:
  # Código para casos não cobertos 
```		

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>