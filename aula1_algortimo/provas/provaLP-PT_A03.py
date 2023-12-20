'''[LP-PY-A03]Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba:
- A média de idade de todo o grupo.
- Qual o nome da pessoa mais velha.
- Quantas pessoas têm menos de 20 anos.
- Quantas pessoas têm mais de 40 anos.
- Qual o sexo da pessoa mais nova.'''

print(' programa que lê o nome, idade e sexo de 5 pessoas')
maior = qtd = menor = soma = 0
mais_velho = mais_nova =''
contador_menor = contador_maior = int(0)
quarda_sexo =''
for c in range(1, 6):
  nome = input(f'Digite o {c}ª nome: ')
  idade = int(input('Digite a idade: '))
  sexo = input('Digite o sexo (F -Feminio / M -Masculino) ')
  soma += idade
  qtd += 1
  if qtd == 1 :
    maior = menor = idade
    mais_nova = mais_velho = nome
  else :
    if idade > maior:
      maior = idade
      mais_velho = nome
    if idade < menor :
      menor = idade
      mais_nova = nome
  if idade < 20 :
     contador_menor += 1
     quarda_sexo = sexo
     if quarda_sexo == 'f' or quarda_sexo == 'F':
      quarda_sexo = 'Feminio'
     else:
       quarda_sexo = 'Masculino'
  if idade > 40 :
    contador_maior += 1
  #sexo = input('Digite o sexo (F -Feminio / M -Masculino) ')
print(f'A media das idades é: {(soma/5):.2f}')
print(f'A pessoa mais velha se chama: {mais_velho} sua idade é {maior}')
print(f'A pessoa mais nova se chama: {mais_nova} sua idade é {menor} e seu sexo é {quarda_sexo}.')
print(f'existem {contador_menor} pessoas com menos de 20 anos.')
print(f'e existem {contador_maior} pessoas com mais de 40 anos.')
