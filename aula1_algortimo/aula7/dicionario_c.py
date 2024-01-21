# fazendo um input no dicionario
estado = {}
brasil = []
'''Modo errado. Assim sera criado um dicionario apenas do ulimo elemento digitado
pois numa lista para fazer isso é  necessário fazer uma copia dos dados (fatiamento) da siguinte forma: brasil.append(estado[:]). Porem com o estado é um dicionario, isso não é permitido. Em dicionário para copiar um elemento usa-se o metodo .copy()
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado) #adiciona o estado na lista
print(brasil)
'''
#modo correto
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: ')).capitalize()
  estado['sigla'] = str(input('Sigla do Estado: ')).upper()
  brasil.append(estado.copy()) #adiciona o estado na lista
print(brasil)

#Mostrando estados separados
'''for e in brasil:
  print(e)'''
#ou com 2 for
for e in brasil: #for da lista
  for k,v in e.items(): #for do dicionario
    print(f'O campo {k} tem valor {v}.')
#forma 3
for e in brasil: #for da lista
  for v in e.values(): #for do dicionario
    print(v, end=' ')
  print()
