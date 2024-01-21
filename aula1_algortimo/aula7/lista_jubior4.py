'''4. crie uma variavel que retorne na tela todos os valores do dicionario da questão 2.'''
dicio = {'nome':'Solange', 'sobrenome' : 'Maia', 'idade': '25', 'aniversario':'10/01/1999'}
chave = dicio.keys()
valor = dicio.values()
lista_valore = []
for x, y in dicio.items():    
    #print('As chaves são: ',x)
    #print('Os valoir são: ',y)
    lista_valore.append(chave)
    lista_valore.append(valor)

print(lista_valore)
   
