#6) Solicite ao usuario que informe uma palavra e verifique se  a letra ‘a’ esta presente nela se estiver print(‘tem a letra a’) se nao print(‘nao tem a letra a’)
#metodo 1 - verifica se   a substring esta presente na string. retorna -1 se não estiver
#ou o indice mais a esquerda onde a substring é encontrada
letra = 'a'
palavra = input('Digite uma palavra: ')
'''
if(palavra.find(letra) > -1):
  print('tem a letra a')
else:
   print('Não tem a letra a')
'''
#Metodo 2 -se uma substring esta presente em uma string, retorna true o false
retorno = letra in palavra
if  retorno == True :
  print('tem a letra a')
else:
   print('Não tem a letra a')

quant = palavra.count(letra)
print(f'A letra aparece a {quant} vezes')
