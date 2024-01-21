'''ATIVIDADE PRÁTICA 11 - Desenvolva um programa que recebe um dicionário, uma
chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existi
# Dicionário de exemplo
meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

# Solicitar entrada do usuário
chave_inserida = str(input("Digite a chave: "))
valor_inserido = str(input("Digite o valor: "))

# Converter o valor inserido para o tipo apropriado (pode ser int, float, etc.)
# Neste exemplo, vou considerar que os valores inseridos são do tipo string
#valor_inserido = eval(valor_inserido)

# Verificar se a chave já existe no dicionário
if chave_inserida in meu_dicionario:
    # Se a chave já existir, atualiza o valor
    print(f"A chave '{chave_inserida}' já existe. Atualizando o valor para {valor_inserido}.")
    meu_dicionario[chave_inserida] = valor_inserido
else:
    # Se a chave não existir, adiciona a chave e o valor
    print(f"Adicionando a chave '{chave_inserida}' com o valor {valor_inserido}.")
    meu_dicionario[chave_inserida] = valor_inserido

# Exibir o dicionário atualizado
print("Dicionário Atualizado:", meu_dicionario)
'''
dicionario = {'nome': 'Helton', 'idade': 46, 'sexo':  'M'}

chave = str(input('Digite a chave: '))
valor = str(input('Digite o valor: '))

if chave in dicionario:
  dicionario[chave] = valor
  print(f'A chave {chave} já existe. Atualizando para o {valor} ')
else:
  print(f'A chave não {chave} não existe. Criando a  chave e adiconando o valor {valor}  ao dicionario')

print('O dicionário atualizado é:-> ',dicionario)
