#[LP-PT-A01]Escreva um algoritmo do tipo Pseudocódigo que pergunte ao usuário 5 números #inteiros  entre 0 e 10 e imprima cada um deles que seja par.
'''
print('Digite 5 numeros inteiros entre 0 e 10')
n1 = int(input('Digite o 1ª número: '))
if n1 % 2 == 0 :
  print(f'O número {n1} é par')
n2 = int(input('Digite o 2ª número: '))
if n2 % 2 == 0 :
  print(f'O número {n2} é par')
n3 = int(input('Digite o 3ª número: '))
if n3 % 2 == 0 :
  print(f'O número {n3} é par')
n4 = int(input('Digite o 4ª número: '))
if n4 % 2 == 0 :
  print(f'O número {n4} é par')
n5 = int(input('Digite o 5ª número: '))
if n5 % 2 == 0 :
  print(f'O número {n5} é par')

print('fim programa')'''
#solução 2
print('Digite 5 numeros inteiros entre 0 e 10')
for num in range(1,6):
  n = int(input(f"Digite {num}ª número : "))
  if n > 0 and n < 10 :
    if n % 2 == 0 :
       print(f'O número {n} é par')
  else :
    print('Número invalido.')
    #continue
print('Fim do programa')
'''
if n % 2 == 0 :
  print(f'O número {n1} é par')
'''
