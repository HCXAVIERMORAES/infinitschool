#Apostila aula 3, revisão condicionais
#Faça um Programa que peça 4 números e imprima o maior deles.
print('Digite 4 numeros.')
N1 = float(input('Digite 1ª numero: '))
N2 = float(input('Digite 2ª numero: '))
N3 = float(input('Digite 3ª numero: '))
N4 = float(input('Digite 4ª numero: '))
if N1 > N2 and N1 > N3 and N1 > N4 :
  print(f'O miaor número digitado foi: {N1}')
elif N2 > N1 and N2 > N3 and N2 > N4 :
  print(f'O miaor número digitado foi: {N2}')
elif N3 > N1 and N3 > N2 and N3 > N4 :
  print(f'O miaor número digitado foi: {N3}')
#elif N4 > N1 and N4 > N2 and N4 > N3 :
 # print(f'O miaor número digitado foi: {N4}')
else :
  print(f'O miaor número digitado foi: {N4}')
