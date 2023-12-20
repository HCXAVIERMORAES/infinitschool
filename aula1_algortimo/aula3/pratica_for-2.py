'''Desenvolva um programa que leia o nome, idade e sexo de 3 pessoas.No final do programa, exiba:
-a média de idade de todo o grupo.
-Qual o nome da pessoa mais velha.
-quantas pessoas têm menos de 20 anos.'''
maior = qtd = menor = soma = 0
maisvelho = maisNova =''
contador = int(0)
for c in range(0, 3):
  nome = input('Digite um nome: ')
  idade = int(input('Digite a idade: '))
  soma += idade
  qtd += 1
  if qtd == 1 :
    maior = menor = idade
    maisNova = maisvelho = nome
  else :
    if idade > maior:
      maior = idade
      maisvelho = nome
    if idade < menor :
      menor = idade
      maisNova = nome
  if idade < 20 :
     contador += 1
  sexo = input('Digite o sexo (f -Feminio/M -Masculino) ')
print(f'A media das idades é: {(soma/3):.2f}')
print(f'A pessoa mais velha se chama: {maisvelho} sua idade é {maior}')
print(f'A pessoa mais nova se chama: {maisNova} sua idade é {menor}')
print(f'existem {contador} pessoas com menos de 20 anos.')
