#tuplas são como listas porem imutaveis
tupla = ('cpf','123.452.789-97')
print(type(tupla))
#print(tupla[1])
#desempacotamento
x,y = tupla
print('posição1: ',x)
print('posição 2: ',y)
# ou

tupla = ('cpf','123.452.789-97')
for x in tupla:
    print(x)

#Métodos de manipulação de tulas
frutas = ('maça','banana', 'laranja', 'abacaxi')
#metodo index():  retorna o index do 1ª elemento especificado
indece_laranja = frutas.index('laranja')
print('indece da laranja: ', indece_laranja)  #saida 2
#Metodo coun() Retorna o número de ocorrencia de elemento
qtd_bananas = frutas.count('banana')
print('quantidade de bananas: ',qtd_bananas) #saida = 1

