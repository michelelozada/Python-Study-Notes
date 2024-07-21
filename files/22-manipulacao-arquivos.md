> **Manipulação de arquivos em Python **  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp; 

## Manipulação de arquivos em Python *(mini-revisão)*
```
- Refere-se aos processo de interação e gerenciamento de arquivos armazenados no sistema de arquivos do 
computador, através da  linguagem de programação Python 

- Dentre várias funcionalidades, inclui a leitura de dados de arquivos e a escrita de novos dados nos 
arquivos

- A leitura de arquivo é abrir um arquivo existente para ler seu conteúdo

- A escrita em arquivos é criar ou sobrescrever um arquivo com novos dados
```

&nbsp; 

## Funções do Python para manipulação de arquivos 

### Observação inicial 
Para os exemplos abaixo, será criado antes um arquivo chamado arquivo.txt, a ser salvo na mesma pasta em que se salvará um arquivo o código abaixo, sendo que se atribui este arquivo à variável a seguir. 

```py

# aqui, o arquivo criado está sendo atribuído a uma variável 
file = 'arquivo.txt'
```

&nbsp; 

### open()
Função utilizada para abrir um arquivo no modo desejado. Retorna um objeto de arquivo que permite a leitura e escrita de dados para o arquivo especificado. 

&nbsp; 

A forma básica de uso é open(nome_do_arquivo, modo), onde nome_do_arquivo é o caminho para o arquivo e modo especifica se o arquivo será aberto para leitura ('r'), escrita ('w'), ou para adicionar novos dados ao final do arquivo ('a'), dentre outros modos.

```py

# abrindo um arquivo para leitura
arquivo_leitura = open(file, 'r')

# abrindo um arquivo para escrita
arquivo_leitura = open(file, 'w')

# abrindo um arquivo para adicionar novos dados no fim do arquivo
arquivo_leitura = open(file, 'a')
```

&nbsp; 

### read()
Função utilizada para ler o conteúdo de um arquivo aberto para leitura ('r'). Pode ler todo o conteúdo do arquivo de uma vez ou, se especificado, uma quantidade específica de caracteres. 

```py

# abrindo um arquivo para leitura
arquivo_leitura = open(file, 'r')

# lendo o conteúdo do arquivo e atribuindo-o a uma variável
leitura = arquivo_leitura.read()

# imprimindo o conteúdo da variável na tela
print(leitura)
```

&nbsp; 

### close()
Esta função é usada para fechar o arquivo que foi aberto previamente com a função `open()`. Depois de trabalhar com um arquivo, é sempre importante fechá-lo para liberar os recursos do sistema operacional associados a ele. 

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

### write()
Função utilizada para escrever dados no arquivo, uma vez que arquivo esteja aberto no modo de escrita ('w' ou 'a'). Aceita uma string como argumento e escreve essa string no arquivo aberto.

```py

# abrindo arquivo para escrita 
arquivo_escrita = open(file, 'w')

# escrevendo no arquivo, sobrescrevendo mensagem anterior
arquivo_escrita.write("Este é o novo texto") 

# fechando o arquivo 
arquivo_escrita.close()
```

&nbsp; 

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>