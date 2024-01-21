''''Dicionários são uma das estruturas de dados que permitem armazenar valores associados a chaves,
formando assim uma espécie de “mapeamento” entre chaves e valores. Em outras palavras, um
dicionário é uma coleção de pares chave-valor. Como em um Jason tem chave e valor'''
#forma de criar dicionario vazio
'''Em Python, os dicionários você pode criar dicionários utilizando
chaves vazias.
'''
meu_diciobario = {}
#urilizando o construtor dict()
dicionario1 = dict() #dicionario vazio 1ª metodo
dicionario2 = dict([('Modulo','Python'),('Instituição','Infinity School')])#2ª metodo
dicionario3 = dict(Modulo = 'Python', Instituicao = 'Infinty Sxhool')#3ª metodo

'''Para acessar um valor de um dicionário basta printarmos o dicionário
e colocar entre colchetes e aspas a chave que queremos. Também
podemos utilizar a função get() para acessar um valor.'''
dados_usuarios = {'Nome':'Raama', 'Idade':18, 'cidade':'Salvador'}
print('--'*10)
print('pegando dados com .get() e ["chave"]')
print(dados_usuarios['Idade'])
print(dados_usuarios.get('Nome'))
print('--'*10)
#declaração de dicionário
cadastro = {
    'nome' : 'otavio',
    'idade' : '26'
}
print('**'*10)
for x, y in cadastro.items():
    print(x,y)

x = list(cadastro.keys())
y = list(cadastro.values())

print(x)
print(y)

print(cadastro['nome'])#mostrar dicionario
print('**'*10)
#exemplo
nome_al = {'nome' : 'Helton',
        'idade' : '46'
        }

#mostrar dicionario
print(f"Meu nome é: {nome_al['nome']}\nE minha idade {nome_al['idade']}")

'''Para acessar um valor de um dicionário basta printarmos o dicionário
e colocar entre colchetes e aspas a chave que queremos. Também
podemos utilizar a função get() para acessar um valor.
'''
print('-='*10)
#Operações Suportadas nos Dicionários->Retorna uma lista com todas as chaves usadas no dicionário
#1) list(dicionario)
computador = {'cpu': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}
print('list(dicionario)->Retorna uma lista com todas as chaves usadas no dicionário')
print('O dicionario=>',computador)
print('Suas chaves são_>',list(computador))
print('-='*10)
print('len(dicionario)->etorna o número de itens de um dicionário->\n',len(computador))
print('-='*10)
print('''dicionaro[chave]->Retorna o valor da chave especificada entre colchetes. Caso a
chave não exista, uma exceção do tipo KeyError será lançada\nEX.:computador['RAM']->''',computador['RAM'])
print('-='*10)
print('''dicionario[chave] = valor ->Se a chave já existir no dicionário, terá seu valor
sobrescrito. Se a chave não existir, ela será criada e o valor será atribuída a ela. Ex:''')
print('Valor do dicionario->',computador['cpu'])
computador['cpu'] = 'Xiaomi'
print('Mudadno o Valor do dicionario-> computador["cpu"] = "xiaomi\n',computador['cpu'])
print('***'*10)
print('del dicionario[chave-> Remove a chave e seu respectivo valor do dicionario')
del computador['cpu']
print('Ex: del computador["cpu"]. Novo dicionario',computador)
print('-+'*10)
print('chave in dicionario-> Retorna True se a chave for encontrada no dicionário',
'senão, retornará False')
computador['cpu'] = 'Xiaomi'
print('coltando com a cpu',computador)
print('pesquisando se a chave cpu existe -> "cpu" in computador-> ',"cpu" in computador)
print('**OPERAÇÕES SUPORTADAS NOS DICIONARIOS***')
print('chave not in dicionario -> Retorna True se a chave não for encontrada no' ' dicionário senão, retornará False. ex:"cpu" not in computador')
print('cpu' not in computador)
print('***'*10)
print('dicionario.clear()->Remove todos os itens do dicionário',computador)
computador.clear()
print('apos usar o .clear()->',computador)
print('***'*10)
print('iter()-> Retorna um iterador para as chaves do dicionário. Retorna o'
'mesmo que dicionario.keys()')
computador = {'cpu': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}
print(iter(computador))
print('para usar o iter() deve utilizar um list(iter(computador))')
print('O retorno é ->', list(iter(computador)))
print('-+'*10)
print('''dicionario.get(chave, valor padrão -> Retorna o valor para a chave especificada se esta existir no dicionário, senão, será retornado um valor padrão definido. Caso
este valor não seja definido, a função retornará None''')
print('computador.get("cpu"), retorna-> ',computador.get('cpu'))
print('computador.get("placa Mâe"),qdo valor não definido, retorna-> ',computador.get('placa Mãe'))
print('computador.get("placa Mâe". "chave inexistente),qdo o valor é definido, retorna-> ',computador.get('placa Mãe', 'Chave inexistente'))
print('**'*10)
print('dicionario.copy() -> Retorna uma cópia do dicionário')
print('Ex:',computador)
sistem_computador = computador.copy()
print('Ex:sitem_computador = computador.copy(), retorna-> ', sistem_computador)
print('**'*10)
print('''dict.fromkeys(iteravel) -> Cria um novo dicionário com chaves proveniente
do iteravel (uma lista, um dicionário), os valores por padrão serão None''')
print('Ex: cria m dicionario apartir de uma lista ou dicionario, etc. ex:')
computador1 = ['CPU', 'RAM', 'SSD']
print('lista ->',computador1)
print('Novo dicionario -> dict.fromkeys(iteravel)->', dict.fromkeys(computador1))
print('**'*15)
