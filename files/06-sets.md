> **Set (conjunto de dados)**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
## Sets em Python *(mini-revisão)*
```
- Classe associada: set

- É uma estrutura de dados de sequência em que *apenas itens únicos são armazenados*

- Isso quer dizer que ao tentar adicionar um item que já presente no set, este será ignorado

- É uma sequência não ordenada, pois não mantém uma ordem específica dos elementos 

- É mutável, i.e, permite a adição, remoção ou modificação de elementos dentro da coleção

- Exemplo da sintaxe básica: {1, 2, 3, 6, 5}
```

&nbsp;

## Testando se um set possui elementos ou se está vazio
*Em Python, um set vazio é considerado um valor falso (False) num contexto booleano. Portanto, quando se usa um set em uma condição if, é verificado se o set está vazio ou não, sendo que um set com elementos é considerado True e um set vazio é considerado False. 

```py
set_numeros = {1, 2, 3, 4, 5}

if set_numeros:
  print("O set de números não está vazio.")
else:
  print("O set de números está vazio.")
```
```py
set_letras = {}

if set_letras:
  print("O set de letras não está vazio.")
else:
  print("O set de letras está vazio.")
```  

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>