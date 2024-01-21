'''ATIVIDADE PRÁTICA 8
Escreva um programa que percorra um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações'''
dados_usuarios1 = {'nome' : 'Raama', 'idade' : '18' } #dicionario

for k, v in dados_usuarios1.items():
  print(k,v)
print('--'*10)

for k in dados_usuarios1.keys():
    print('chave->',k)
print('--'*10)

for v in dados_usuarios1.values():
    print('Valor->',v)
print('--'*10)

meu_dict = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

# Iterando sobre chaves
for chave in meu_dict:
    print(chave)
print('--'*10)

# Iterando sobre valores
for valor in meu_dict.values():
    print(valor)
print('--'*10)

# Iterando sobre pares chave-valor
for chave, valor in meu_dict.items():
    print(chave, valor)
