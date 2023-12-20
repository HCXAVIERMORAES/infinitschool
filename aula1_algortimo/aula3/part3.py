#repetição for
''''repetir = range(5) # vai de 0 a 99

for valor in repetir : #valor variavel criada para controle do laço
   # print('oi')
    print(valor)

repetir = 'helton'
letra = 'o'

for valor in repetir:
    print(valor)

for valor in range(6):
    print(valor)

#verificar leta na palavra
for valor in repetir:
    if valor == 'e':
        print(valor)
'''
'''
#print de 0 a 9
for valor in range(10):
    print(valor)
'''
#lista de exercicio
#1-Escreva um programa que use um laço "for" para imprimir os números de 1 a 5.
#for num in range(1,6):
    #print(num)
''''
#2-Crie um programa que utilize um laço "for" para imprimir os números pares de 0 a 10.
for par in range(2,10+2,2):
    print(par)

#3- Desenvolva um programa que itere sobre uma string e imprima cada caractere separadamente. 
palav = input('Digite uma palavra: ')
for letra in palav:
    print(letra)

#4- Desenvolva um programa que conte ate o numero 100 mostrando apenas os numeros pares
for par in range(2,100+2,2):
    print(par)

#5-Faça o mesmo a questao anterior mostrando apenas os numero impares
for impar in range(100):
    if impar % 2 != 0:
        imp = impar
        print(imp)
    #print(impar)

#6-Desenvolva um programa que itere sobre uma string e conte o número de vogais presentes nela.
vogais ='aeiou'
tem = 0
palavra = input('Digite uma palavra? ')
for vog in palavra :
    if vog in vogais :
        tem += 1
print(tem)

#7-Itere sobre seu nome e mostre apenas as vogais
vogais ='aeiou'
tem = 0
palavra = input('Digite seu nome: ')
for vog in palavra :
    if vog in vogais :
        tem += 1
        print(vog)

#8-Itere sobre seu nome e mostre apenas as consoantes
cons ='BCDFGJKLMNPQRSTVWXZbcdfghjlmnpqrstvwxz'
tem = 0
palavra = input('Digite seu nome: ')
for vog in palavra :
    if vog in cons :
        print(vog)
'''
#9- Elabore um programa que itere sobre uma string e imprima cada caractere, mas em maiúsculas. utilize o .upper()
palavra = input('Digite uma palavra: ')
for letra in palavra:
    print(letra.upper())