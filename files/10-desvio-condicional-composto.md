> **Desvio condicional composto**  
> Repositório: Python - Notas de estudo     
> GitHub: @michelelozada
&nbsp;
     
&nbsp;  
### Exercício:
O edital de um exame de proficiência em inglês definiu que, para ser aprovado, um candidato precisa obter nota mínima
8.0 em cada uma das quatro provas a serem aplicadas. Sabendo disso, escreva um algoritmo que, depois de ler as notas
obtidas, informe se esse candidato foi aprovado no exame (ou não).  

```py

candidate = 'Enzo Marques'
print(f"Por favor, informe abaixo as notas obtidas pelo candidato {candidate}:\n")
p1 = float(input('- Prova de Listening: Nota '))
p2 = float(input('- Prova de Speaking: Nota '))
p3 = float(input('- Prova de Reading and Use of English: Nota '))
p4 = float(input('- Prova de Writing: Nota '))

print('\nResultado final:')
if (p1>=8.0) and (p2>=8.0) and (p3>=8.0) and (p4>=8.0):
  status = 'igual ou superior'
  outcome = 'conseguiu aprovação'
  exam = 'todas as provas'
else:
  status = 'inferior'
  outcome = 'foi reprovado'
  exam = 'pelo menos uma das provas'
print(f'O candidato {candidate} obteve nota {status} a 8.0 em {exam} e, portanto, {outcome} no exame de proficiência em inglês.')


'''
Por favor, informe abaixo as notas obtidas pelo candidato Enzo Marques:

- Prova de Listening: Nota 9.5
- Prova de Speaking: Nota 8.6
- Prova de Reading and Use of English: Nota 7.8
- Prova de Writing: Nota 9.1

Resultado final:
O candidato Enzo Marques obteve nota inferior a 8.0 em pelo menos uma das provas e, portanto, foi reprovado no exame de proficiência em inglês.
'''
```

&nbsp;

<div align="center">
<a href="https://github.com/michelelozada/Python-Study-Notes">[Voltar à tela inicial do repositório]</a>
</div>

