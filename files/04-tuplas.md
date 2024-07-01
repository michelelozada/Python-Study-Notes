> **Tuplas**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;

&nbsp;  
## Tuplas em Python *(mini-revisão)*
```
- Classe associada: tuple

- Cada item dentro da tupla é chamado de elemento (ou mesmo de item) 

- É um estrutura de dados de sequência imutável, i.e., após a criação da tupla, elementos não podem 
ser modificados, adicionados ou removidos dali 

- Tuplas são ordenadas, i.e., sua ordem é baseada na sequência em que os elementos foram ali inseridos

- Elementos são acessados pela posição/por seu índice na tupla

- Exemplo da sintaxe básica: (1, 2, 3, 4), ('a', 'e', 'i', 'o', 'u')
```

&nbsp;

## Testando se uma tupla possui elementos ou se está vazia
*Em Python, uma tupla vazia é considerada um valor falso (False) num contexto booleano. Portanto, quando se usa uma tupla em uma condição if, é verificado se a tupla está vazia ou não, sendo que uma tupla com elementos é considerada True e uma tupla vazia é considerada False.* 

```py

numeros = (1, 2, 3)

if numeros:
  print("A tupla de números não está vazia.")
else:
  print("A tupla de números está vazia.")

# Saída: A tupla de número não está vazia.
```
```py

letras = ()
if letras:
  print("A tupla de letras não está vazia")
else:
  print("A tupla de letras está vazia")
  
# Saída: A tupla de letras está vazia
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>