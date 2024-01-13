'''[PY-A02] - Faça um programa que solicite ao usuário que digite 10 valores para
preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.'''

print('\033[33m -=-' * 20)
print(' '*20,'PROVA DE PYTHON [PY-A02]')
print('\033[33m -=-\033[m' * 20)

print('Informe 10 números inteiros. ')
lista_par = []
lista_impar = []
soma_par = 0
soma_impar = 0

for c in range(1,11):
  num = int(input(f'Digite {c}ª número: '))
  if num % 2 == 0 :
    soma_par += num
    lista_par.append(num)
  else:
    soma_impar += num
    lista_impar.append(num)
print('A quantidades de números pares é: {} e sua soma é {}.'.format(len(lista_par),soma_par))
print('Lista dos números pares: ',lista_par)
print(f'A quantidades de números impares é: {len(lista_impar)} e sua soma é: {soma_impar}')
print('Tupla dos números impares: ',tuple(lista_impar))
