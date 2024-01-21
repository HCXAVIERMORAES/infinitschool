'''ATIVIDADE PRÁTICA 12 - Escreva um programa que recebe um dicionário e uma
lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso
contrário'''
tem = 0
chave = ''
dicionario = {'nome': 'Helton', 'idade': 46, 'sexo':  'M'}
lista_chave = ['uf', 'endereço', 'nome', 'sigla']
print('O dicionario é: ', dicionario)
print('A lista de chaves é: ', lista_chave)

print('nome' in dicionario)
for k in lista_chave:
  chave = k
  if chave in dicionario.keys():
    print(f'O valor "{chave}" existe no dicionario')
    tem += 1
  else:
    print(f'chave "{chave}" não encontrada no dicionario.')
    tem += 1
if tem == len(dicionario):
  print(True, 'Todas as chaves existem no dicionario')
else:
  print(False,'nem todas as chaves estão presentes no dicionario.')

print('****Resposta CHAT GPT*******')

def verificar_chaves(dicionario, lista_chaves):
    for chave in lista_chaves:
        if chave not in dicionario:
            return False
    return True

# Exemplo de uso
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
minhas_chaves = ['a', 'c', 'd']

resultado = verificar_chaves(meu_dicionario, minhas_chaves)

# Exibir o resultado
print('Dicionario ->',meu_dicionario)
print('lista de chaves ->',minhas_chaves)
print("Todas as chaves existem no dicionário:", resultado)
