'''ATIVIDADE PRÁTICA 9
Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.'''
dados_usuarios1 = {'nome' : 'Raama', 'idade' : '18' }

for chave in dados_usuarios1.keys():
  print(f'A chave do dicionario é -> {chave}')
print('--'*10)
for valor in dados_usuarios1.values():
  print(f'O valor do dicionario é -> {valor}')
print('--'*10)
