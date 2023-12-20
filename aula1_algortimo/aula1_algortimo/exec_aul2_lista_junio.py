'''1) Dada as seguintes variaveis crie um programa para exibir o tipo de cada uma:'''

x = 24
y = 'teste'
z = 456.3
a,b = True, 45 #duas variaveis popde ser sepadas por vigula em tipos diferentes

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

#2)Faça um programa que verifique se a expressão e verdadeira ou falsa: (35*3+(22+2)) > (9*9)

bloco1 = (35*3+(22+2))
bloco2 = (9*9)

print(bloco1 > bloco2)

#3) solicite ao usuario que informe 2 numero com o comando input e verifique qual e o maior numero deles
'''
print('Difite doi numeros diferentes entre se')
n1 = input('digite 1ª numero: ')
n1 = int(n1)
n2 = input('digite 2ª numero: ')
n2 = int(n2)

if(n1 > n2):
    print(f'O maior numero é {n1}')
elif n1 == n2:
      print(f'Os numeros sãp iguais')
else:
     print(f'O maior numero é {n2}')

'''

#3) Faça a mesma situação porem com 3 numeros
print('Digite 3 numeros')
n1 = input('digite 1ª numero: ')
n1 = int(n1)
n2 = input('digite 2ª numero: ')
n2 = int(n2)
n3 = input('digite 3ª numero: ')
n3 = int(n3)

if(n1 > n2 and n1 > n3):
    print(f'O maior numero é {n1}')
elif n2 > n1 and n2 > n3:
      print(f'O maior numero é {n2}')
elif n3 > n1 and n3 > n2 :
      print(f'O maior numero é {n3}')
else:
      print('valores iguais')
