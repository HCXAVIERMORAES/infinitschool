'''Faça um programa que receba dois números e mostre qual é o maior e qual é o menor.'''
print('comparação de 2 números')
n1  = int(input('Digite o 1ª numero: '))
n2  = int(input('Digite o 2ª numero: '))
maior = menor = n1
#igual = False
if n2 > maior:
    maior = n2
elif n1 == n2:
    #igual = True
    print('Numeros são iguais')
else:
    menor = n2

print(f'O número {maior} é o maior.')
print(f'O número {menor} é o menor.')
#solução prof.
n1 = int(input('Informe o 1ª número: '))
n1 = int(input('Informe o 2ª número: '))

if n1 > n2:
    print(f'O 1ª numero,{n1}, é maior')
elif n2 > n1:
    print(f'O 2ª numero, {n2} é maior')
else:
    print(f'Os números sao iguais, {n1}')
