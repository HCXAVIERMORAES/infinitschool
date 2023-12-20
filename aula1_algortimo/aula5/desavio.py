'''Crie um programa que receba três notas, calcule a média e mostre se o aluno foi aprovado ou
reprovado. (Base de cálculo: media=(nota1+nota2+nota3)/3'''
print('Aprovação ou Reprovação do Aluno')
nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
nota3 = float(input('Digite a 3ª nota do aluno: '))

media = (nota1+nota2+nota3)/3

if media <= 6:
    #aprov = False
    print(f'aluno reprovado. Sua média foi de {media:.2f}')
else:
    print(f'Aluno aprovado. Sua média foi de {media:.2f}')
 