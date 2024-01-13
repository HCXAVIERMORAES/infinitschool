'''revisão aulas'''
'''
#var = 18
var = int(input('Informe idade: '))
if var  >= 18 :
    print('pode entrar')
else: 
    print('Não pode entrar')
'''
#faça um programa que conte de 1 a 10 com while

inicio = 0
while(inicio <= 10):
    print(inicio) #1ª mostra e depois inicia a contagem
    inicio += 1
    #print(inicio) #nao mostra o 1ª numero
print('fim while')

#faça um programa que conte de 1 a 10 com for
for var in range(1,11):
    print(var)
print('fim for')