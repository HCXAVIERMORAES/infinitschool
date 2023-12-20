'''Faça um programa que leia o sexo de uma pessoa,identificado pelos valores 'M' ou 'F'.
Caso esteja errado, peça para digitar novamente e dê 3 tentativas.'''
qtd = int(3)
sexo = 'MF'
sexo = input('Digite seu sexo [M/F]: ')
if sexo == 'M':
    print(' Seu sexo é Masculino')
elif sexo == 'F':
    print(' Seu sexo é Femino')
else:
    for c in range(0,qtd) :
      sexo  = input(f'Você digitou {sexo}, digite novamente [M/F]: ')
      qtd -= 1
      if sexo == 'M':
        print(' Seu sexo é Masculino')
        qtd = 0
      elif sexo == 'F':
        print(' Seu sexo é Femino')
        qtd = 0
      else :
        if sexo == 'M' or sexo == 'F' :
         qtd = 0
      print(f'Voce tem {qtd} de chances ainda')
print('Fim')
