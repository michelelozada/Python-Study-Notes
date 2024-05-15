> **Comandos continue e break**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  

### Exercício:
Considere um sistema que forneça acesso somente se o login (LuisRamos) e a senha(Prisma84*) forem informados corretamente.
Caso não haja tal informação, o sistema deve reportar isso continuamente ao usuário.  

```py

while True:
	user1 = input('Por favor, informe o nome de usuário: ')
	if(user1 == 'LuisRamos'):
		print('> Nome de usuário confere...\n')
		while True:
			password = input('Por favor, informe sua senha cadastrada: ')
			if (password == 'Prisma84*'):
				print('> A senha confere! Seja bem-vindo ao sistema, Luis!')
				break # utilizado para quebrar o loop interno
			else:
				print('> Sua senha não confere. Por gentileza, tente novamente...\n')
				continue # utilizado para retornar ao loop interno
	else:
		print('> Nome de usuário não confere. Por gentileza, tente novamente...\n')
		continue # utilizado para retornar ao loop externo
	break # utilizado para quebrar o loop externo


''' 
Outputs possíveis:
 
Por favor, informe o nome de usuário: Luis
> Nome de usuário não confere. Por gentileza, tente novamente...

Por favor, informe o nome de usuário: LuisRamos
> Nome de usuário confere...

Por favor, informe sua senha cadastrada: Prisma82
> Sua senha não confere. Por gentileza, tente novamente...

Por favor, informe sua senha cadastrada: Prisma84
> Sua senha não confere. Por gentileza, tente novamente...

Por favor, informe sua senha cadastrada: Prisma84*
> A senha confere! Seja bem-vindo ao sistema, Luis!
'''
```

&nbsp; 

### Exercício:
Existia uma brincadeira que consistia em contar os números em voz alta, substituindo os números múltiplos de 4 pela 
palavra 'pi'. Escreva um programa que reproduza esta mesma brincadeira:  
```py 

for i in range (1,31):
	if i % 4 == 0:
		print('pi')
		i += 1
		continue
	print(i)

'''
1
2
3
pi
5
6
7
pi
9
10
11
pi
13
14
15
pi
17
18
19
pi
21
22
23
pi
25
26
27
pi
29
30
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>