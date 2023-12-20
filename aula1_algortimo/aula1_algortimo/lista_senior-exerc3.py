'''3) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"1-Telefonou para a vítima?" "2-Esteve no local do crime?" "3-Mora perto da vítima?"
"4-Devia para a vítima?" "5-Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
contaSim = int(0)
contaNao = int(0)
print('Responda com sim ou não')
resp1 = str(input('1- você Telefonou para a vítima? S-sim N-não '))
if resp1 == 's' or resp1 =='S'  or resp1 == 'Sim' or resp1 == 'sim' :
  contaSim = contaSim + 1
#elif resp1 == 'n' or resp1 =='N'  or resp1 == 'Nao' or resp1 == 'nao' :
else:
  contaNao = contaNao + 1
resp2 = str(input('2- você Esteve no local do crime? S-sim N-não '))
if resp1 == 's' or resp1 =='S'  or resp1 == 'Sim' or resp1 == 'sim' :
  contaSim = contaSim + 1
#elif resp1 == 'n' or resp1 =='N'  or resp1 == 'Nao' or resp1 == 'nao' :
else:
  contaNao = contaNao + 1
resp3 = str(input('3- você Mora perto da vítima? S-sim N-não '))
if resp1 == 's' or resp1 =='S'  or resp1 == 'Sim' or resp1 == 'sim' :
 contaSim = contaSim + 1
#elif resp1 == 'n' or resp1 =='N'  or resp1 == 'Nao' or resp1 == 'nao' :
else:
 contaNao = contaNao + 1
resp4 = str(input('4- Devia para a vítima? S-sim N-não '))
if resp1 == 's' or resp1 =='S'  or resp1 == 'Sim' or resp1 == 'sim' :
 contaSim = contaSim + 1
#elif resp1 == 'n' or resp1 =='N'  or resp1 == 'Nao' or resp1 == 'nao' :
else:
  contaNao = contaNao + 1
resp5 = str(input('5- Já trabalhou com a vítima? S-sim N-não '))
if resp1 == 's' or resp1 =='S'  or resp1 == 'Sim' or resp1 == 'sim' :
  contaSim = contaSim + 1
#elif resp1 == 'n' or resp1 =='N'  or resp1 == 'Nao' or resp1 == 'nao' :
else:
  contaNao = contaNao + 1

print('resposta com sim: ', contaSim)
print('resposta com Não: ', contaNao)
