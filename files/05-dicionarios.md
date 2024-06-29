> **Dicionários**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Dicionários em Python *(mini-revisão)*
```
- Classe associada: dict

- É uma coleção de pares de chave-valor *mutável*, i.e., após a criação do dicionário, os pares 
chave-valor podem ser modificados, adicionados ou removidos  

- Na versões mais recentes do Python, os dicionários são ordenados, baseados na ordem de inserção 
dos valores 

- Os elementos de um dicionário são acessados por meio de suas chaves e podem ser iterados

- Exemplo da sintaxe básica: {'nome': 'James', 'sobrenome': 'Bond'}, {'a': 10, 'b': 20}
```

&nbsp;  

## Métodos da Classe `dict` *(referência rápida)* 

Método | Função
---    | :--
clear() | Remove todos os itens do dicionário
copy() | Retorna uma cópia superficial do dicionário
get() | Retorna o valor de chave especificada ou o valor padrão se a chave não for encontrada
items() | Retorna uma nova lista dos pares chave-valor no dicionário
keys() | Retorna uma nova lista das chaves do dicionário
pop() |  Remove e retorna o valor para a chave especificada. Se a chave não estiver no dicionário, retorna o valor padrão
popitem() | Remove e retorna um par chave-valor do dicionário. Se o dicionário estiver vazio, lança um KeyError
setdefault() | Retorna o valor para a chave especificada; se a chave não estiver no dicionário, adiciona a chave com o valor padrão
update() | Atualiza o dicionário com os pares chave-valor de outro dicionário, sobrescrevendo as chaves existentes
values() | Retorna uma nova lista dos valores do dicionário

&nbsp;

## Exemplos de aplicações dos métodos para manipular dicionários

### Método items()
```py

aluno = {
    'nome': 'Enzo',
    'idade': 18,
    'cidade': 'Curitiba'
}

for chave, valor in aluno.items():
	print(f"Chave: {chave}, Valor: {valor}")
	
# Retorna: 
Chave: nome, Valor: Enzo
Chave: idade, Valor: 18
Chave: cidade, Valor: Curitiba
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>