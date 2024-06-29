> **Range (intervalos)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Range/intervalos em Python *(mini-revisão)*
```
- Classe associada: range 

- É uma estrutura de dados de sequência de números inteiros, que são gerados quando o range é iterado 

- Os números deste invervalo são sempre inteiros, em progressão aritmética

- Os ranges/intervalos são imutáveis, i.e., tendo sido criados, não podem mais ser alterados

- Exemplo da sintaxe básica: range(1, 10, 2) 
```

&nbsp;

### A sintaxe básica para criar um objeto range:

```py

range(start, stop, step)
```
Sendo:  
&nbsp;&nbsp;**. start**: O valor inicial do intervalo (inclusive)  
&nbsp;&nbsp;**. stop**: O valor final do intervalo (exclusive)  
&nbsp;&nbsp;**. step**: O intervalo entre os números/passo (quando implícito, o padrão é 1)  

&nbsp;

### Exemplo

```py

r = range(1, 10, 2)

# Convertendo para lista para impressão de valores contidos no range
print(list(r))  

# Saída: [1, 3, 5, 7, 9]
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>