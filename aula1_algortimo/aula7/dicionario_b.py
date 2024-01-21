#Dicionaio curso em video
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'Idade': '22'}
print(pessoas)
#print(pessoas[0]) #gera um erro pois não existe o indice [0], ele é 'nome'
print(pessoas['nome'])
print(pessoas['Idade'])
#->print formatado. Na hora de referenciar os elementos usa-se [] e na declaração {}.
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')# observar as aspas
print('As chaves são:',pessoas.keys()) #mostra as chaves do dicionario
print('Os valores são:',pessoas.values()) #mostra os valores do dicionario
print('Os itens, chaves e valores: ',pessoas.items())# mostra uma composição
#de elementos, onde o dicionario pra  esse momento é uma lista[elementos] formada por 3 tuplas ('nome','Gustavo'), (etc) dos elemento.
#acessar as chaves, os valores e os itens  por laços
for k in pessoas.keys() : #pra cada uma das chaves
  print(k)

for v in pessoas.values() : #pra cada um dos valores
  print(v)

# para usar o itens tem que ter chave e valor
#del pessoas['sexo']  # apaga o elemento sexo do dicionario
pessoas['nome'] = 'Leandro' #mudando o nome
pessoas['peso'] = 95.5 # adicionado elemento
for k,v in pessoas.items():
  print(f'{k} = {v}')

#adicionando um dicionario dentro de uma lista
Brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigal': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigal': 'SP'}
Brasil.append(estado1) #adicionando o estado1 a lista
Brasil.append(estado2) #adicionando o estado2 a lista
print(estado1)#mostra o dic estado1
print(Brasil)#mostra a lista Brasil
print(Brasil[1])#mostra da lista Brasil, osegundo elemento
print(Brasil[0]['uf'])#mostra Rio de Janeiro
