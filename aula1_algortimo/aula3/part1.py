'''3) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"1-Telefonou para a vítima?" "2-Esteve no local do crime?" "3-Mora perto da vítima?"
"4-Devia para a vítima?" "5-Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
print('Responda com s ou n')
resp = 0
respNao = 0
perg1 = input("1-Telefonou para a vítima? ")
perg2 = input("2-Esteve no local do crime? ")
perg3 = input("3-Mora perto da vítima? ")
perg4 = input("4-Devia para a vítima? ")
perg5 = input("5-Já trabalhou com a vítima? ")

if perg1 =='s':
    resp += 1
#elif perg1 == 'n':
   # respNao +=1

if perg2 =='s':
    resp += 1

if perg3 =='s':
    resp += 1

if perg4 =='s':
    resp += 1

if perg5 =='s':
    resp += 1

print(resp)

if resp == 2:
    print('suspeito')
elif resp == 3 or resp == 4:
    print('cumplice')
elif  resp == 5:
    print('matador')
else:
    print('inocente')

#print('resposta com sim: ', contaSim)
#print('resposta com Não: ', contaNao)

'''
#verificar idade
print('Entrada de show para maior de 18 anos')
acompanhado = ''
idade = int(input('Digite sua idade: '))
acompanhado = input('Esta acompanhado?(s - n) ')
if idade >= 18 :
    print('Você entrou')
elif acompanhado =='s':
     print('Você entrou')
else:
    print("você não tem idade para entra")
'''
