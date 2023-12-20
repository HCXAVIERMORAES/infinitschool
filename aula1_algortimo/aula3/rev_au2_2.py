#Faça um Programa que verifique se uma letra digitada é ‘M’ ou ‘F’.
#letra = 'M', 'F'
letra = input('Digite um letra: ')
if letra == 'M' or letra == 'F' :
  print(f'Você digitou a letra {letra}')
else:
  print(f'Voce não digitou nem M e nem F, e sim {letra}')
