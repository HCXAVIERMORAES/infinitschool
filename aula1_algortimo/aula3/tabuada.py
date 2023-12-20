'''Crie um programa que leia dois valores e mostre uma tabela de multiplicação do primeiro valor pelo segundo valor a partir de 1.'''
print('Tabela de multiplicação')
print('Digite dois valores, o de inicio e o de fim')
inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor do fim: '))
resul = 0
soma = 1
for c in range(1,fim + 1,1):
  resul = inicio * soma
  print(f'Resultado: {inicio} X {soma} = {resul}')
  soma += 1
  if soma == fim + 1 :
    break
print('Fim do programa.')
