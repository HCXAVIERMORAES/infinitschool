'''ATIVIDADE PRÁTICA 10
Crie um programa que exiba os itens exclusivos de dois dicionários. Itens exclusivos são aqueles que não estão presentes em ambos os dicionários.'''
a = {'nome' : 'Raama', 'idade' : '18','nome' : 'jose', 'idade' : '26', }
b = {}

# Dois dicionários
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 2, 'c': 3, 'd': 4}

# Encontrar chaves exclusivas usando conjuntos
chaves_exclusivas1 = set(dicionario1.keys()) - set(dicionario2.keys())
chaves_exclusivas2 = set(dicionario2.keys()) - set(dicionario1.keys())

# Encontrar itens exclusivos
exclusivos1 = {}
for k in chaves_exclusivas1:
    exclusivos1[k] = dicionario1[k]

exclusivos2 = {}
for k in chaves_exclusivas2:
    exclusivos2[k] = dicionario2[k]

# Exibir resultados na tela
print("Dicionário 1:", dicionario1)
print("Dicionário 2:", dicionario2)
print("Itens exclusivos no Dicionário 1:", exclusivos1)
print("Itens exclusivos no Dicionário 2:", exclusivos2)
