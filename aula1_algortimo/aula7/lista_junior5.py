'''5. crie uma lista de tuplas com o dicionario da questao dois exibindo a chave e o valor.'''

#dicio = {'nome':'Solange', 'sobrenome' : 'Maia', 'idade': '25', 'aniversario':'10/01/1999'}
dicio = dict([('nome','Solange'),('sobrenome','Maia'),('Idade','25'),('aniversario','11/01/1999')])

chave = list(dicio.keys())
valor = list(dicio.values())

lista = []
for x in range(len(dicio)):#tamanho do dicionario
    tupla = (chave[x],valor[x])
    lista.append(tupla)
    #print(x)
    #print(chave[x])
    #print(valor[x])
print(lista)

#forma 2
lista2 = [(x, y) for x ,y in dicio.items()]
print(lista2)

lista3 = dicio.items()
print(lista3)