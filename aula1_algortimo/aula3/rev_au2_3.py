'''Faça um programa que calcule se o elevador transportará as
pessoas. O limite máximo é de até 8 pessoas.'''
print('Limite maximo do elevador: 8 Pessoas')
andarMax = int(8)
andarInicial = int(1)
subSolo = int(-1)
Npess = int(0)
sair = 0
resp = input('Deseja usar o elevador? s / n {resp}')
if resp == 's' and Npess < 8:
  qtd = int(input('quantas pessoas vao entra? '))
  Npess += qtd
  if Npess <= 8 :
    print('Pode entrar')
    andar = int(input('Digite seu andar: '))
    if andar <= andarMax and andar > andarInicial:
      print('Subindo')
      sair = int(input('Quantas pessoas vão descer nesse andar? '))
      Npess -= sair
    else :
      print('Descendo')
      sair = int(input('Quantas pessoas vão descer nesse andar? '))
      Npess -= sair
  else :
    print('A quantidade máxima são 8 pessoas no elevador')
if resp == 's' and Npess == 8 :
  print('Lotação maxima atingida. Aquarde o proximo.')
