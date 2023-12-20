'''Crie um programa que leia dois valores e mostre um menu para calcular
1 - Somar
2 - Multiplicar
3 - Dividir
4 - Subtrair
5 - Sair do programa'''
print('Digite o numero do menu: 1-Somar, 2-Multpilica, 3-Dividir'
      + '4-Subttrair e 5- Sair')
opicao = 0
res = None
while opicao != 5:
  opicao = int(input('Digite o que deseja fazer!'))
  if opicao == 5:
    print("Você saiu, fim do programa..")
    break
  else:
    if opicao >= 6:
      print('Opisção invalida')
      print('Fim programa...')
      break
    else:
      n1 = float(input('Digite 1ª numero: '))
      n2 = float(input('Digite 2ª numero: '))
      if opicao == 1:
        res = n1 + n2
      elif opicao == 2:
        res = n1 * n2
      elif opicao == 3:
        res = n1 / n2
      elif opicao == 4:
        res = n1 - n2
    print(f'Resposta: {res}')
