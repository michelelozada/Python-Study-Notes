> **Manipulação de arquivos em Python **  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp; 

## Manipulação de arquivos em Python *(mini-revisão)*
```
- Refere-se ao processo de interação e gerenciamento de arquivos armazenados no sistema de arquivos do 
computador, através da  linguagem de programação Python 

- Dentre outras funcionalidades, inclui a leitura de dados de arquivos e a escrita de novos dados nos 
arquivos

- Leitura de arquivo: abrir um arquivo existente para ler seu conteúdo

- Escrita em arquivos: criar ou sobrescrever um arquivo com novos dados
```

&nbsp; 

## Funções do Python para manipulação de arquivos 

### Observação inicial 
Para os exemplos abaixo, será criado antes um arquivo chamado arquivo.txt, a ser salvo na mesma pasta em que se salvará um arquivo .py com os códigos abaixo. 

&nbsp; 

↳ Abaixo, o arquivo .txt está sendo atribuído a uma variável chamda file

```py

file = 'arquivo.txt'
```

&nbsp; 

### • Função open()
Utilizada para *abrir um arquivo no modo desejado*. Retorna um objeto de arquivo que permite a leitura e escrita de dados para o arquivo especificado. 

&nbsp; 

A forma básica de uso é `open(nome_do_arquivo, 'modo')`, onde nome_do_arquivo é o caminho para o arquivo e modo especifica se o arquivo será aberto para leitura (`'r'`), escrita (`'w'`) ou para adicionar novos dados ao final do arquivo (`'a'`).

```py

# abrindo um arquivo apenas para leitura
arquivo_leitura = open(file, 'r')

# abrindo um arquivo para escrita
arquivo_escrita_1 = open(file, 'w')

# abrindo um arquivo para escrita, ao fim do arquivo
arquivo_escrita_2 = open(file, 'a')
```

&nbsp; 

### • Função read()
Utilizada para *ler o conteúdo de um arquivo aberto para leitura* (`'r'`). Pode ler todo o conteúdo do arquivo de uma vez ou, se especificado, uma quantidade específica de caracteres. 

```py

# abrindo um arquivo para leitura
arquivo_leitura = open(file, 'r')

# lendo o conteúdo do arquivo e atribuindo-o a uma variável
leitura = arquivo_leitura.read()

# imprimindo o conteúdo da variável na tela
print(leitura)
```

&nbsp; 

### • Função close()
Utilizada para fechar o arquivo que foi aberto previamente com a função `open()`. Depois de trabalhar com um arquivo, é sempre importante fechá-lo para liberar os recursos do sistema operacional associados a ele. 

```py

# abrindo um arquivo para leitura
arquivo_leitura = open(file, 'r')

# lendo o conteúdo do arquivo e atribuindo a uma variável
leitura = arquivo_leitura.read()

# imprimindo o conteúdo da variável na tela
print(leitura)

# fechando o arquivo 
arquivo_leitura.close()
```

&nbsp;

### • Função write()
Utilizada para escrever dados em arquivos abertos no modo de escrita (`'w'` ou `'a'`). Aceita uma string como argumento e escreve essa string no arquivo aberto.

```py

# abrindo arquivo para escrita 
arquivo_escrita = open(file, 'w')

# escrevendo no arquivo, sobrescrevendo mensagem anterior
arquivo_escrita.write("Este é o novo texto") 

# fechando o arquivo 
arquivo_escrita.close()
```

&nbsp; 

## Trabalhando com o with
No contexto de manipulação de arquivos em Python, o `with` é frequentemente usado em conjunto com a função `open()` para garantir que o arquivo seja automaticamente fechado após as operações de leitura ou escrita - e isso mesmo que ocorram exceções durante a execução das operações no arquivo. 

&nbsp; 

↳ Repare que com o uso do `with` não há a necessiade de usar a função `close()`, tornando o código mais conciso

```py

with open('arquivo.txt', 'r') as arquivo:
  conteudo = arquivo.read()
  print(conteudo)
```    

&nbsp; 

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>