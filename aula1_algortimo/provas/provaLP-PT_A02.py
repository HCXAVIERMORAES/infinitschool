'''[LP-PY-A02]Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números.'''
'''
print('Digite 3 numeros')
n1 = float(input('Digite 1ª número: '))
n2 = float(input('Digite 2ª número: '))
n3 = float(input('Digite 3ª número: '))
#maior
maior = n1
if n2 > n1 and n2 > n3 :
  maior = n2
elif n3 > n1 and n3 > n2 :
  maior = n3

menor = n1
if n2 < n1 and n2 < n3 :
  menor = n2
elif n3 < n1 and n3 < n2 :
  menor = n3
else :
  if n1 == n2 or n2 == n1:
    print(f'Os número {n1} e {n2} são iguais')
  if n1 == n3 or n3 == n1:
    print(f'Os número {n1} e {n3} são iguais')
  if n2 == n3 or  n3 == n2:
    print(f'Os número {n2} e {n3} são iguais')

print(f'O numero {maior} foi o maior número digitado.')
print(f'O numero {menor} foi o menor número digitado.')
print('Fim do programa')
'''
# Solicitar três números ao usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Determinar o maior número
maior = n1
if n2 > maior:
  maior = n2
if n3 > maior:
  maior = n3

# Determinar o menor número
menor = n1
if n2 < menor:
  menor = n2
if n3 < menor:
  menor = n3

# Verificar se existem números iguais e mostrá-los
iguais = False
if n1 == n2 or n1 == n3 or n2 == n3:
  iguais = True

if n1 == n2 == n3:
  print(f"Os três números são iguais {n1}.")
else:
  if iguais:
    print("Existem números iguais:")
    if n1 == n2:
      print(f'O 1ª e o 2ª número, {n2} são iguais')
    if n1 == n3:
      print(f'O 1ª e o 3ª número, {n3} são iguais')
    if n2 == n3:
      print(f'O 2ª e o 3ª número, {n3} são iguais')
  else:
    print("Não existem números iguais.")
    # Exibir resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
