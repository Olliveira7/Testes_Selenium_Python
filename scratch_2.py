# -*- codeing: utf-8 -*-
#Entrar com nota da PR1 e nota da PR2 de 1 aluno. Imprimir: nome, nota da PR1, nota da PR2,
#média e uma das mensagens: AP , RP ou PF (a média é 7 para aprovação, menor que 3 para reprovação
#e as demais em prova final).

pr1=int(input(' Digite Nota da prova 1: '))
pr2 = int(input(' Digite Nota da prova 2: '))
media= (pr1 + pr2)/2
if media >= 7:
    print('Aprovado')
if media < 3:
    print('Reprovado')
if (media >= 3) and (media <=7):
    print('Prova Final')






