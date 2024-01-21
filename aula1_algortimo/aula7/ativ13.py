'''ATIVIDADE PRÁTICA 13
Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção.
Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.'''
#opçoes
# Dicionário de mapeamento de número para nome
mapeamento_nomes = {1: 'Paulo', 2: 'José', 3: 'Aline'}
#resultado
dic_votos = {}
pare = 0
resp = int()
soma_voto = 0
print('-='*25)
print('***************URNA DE VOTAÇÃO******************')

while True:
  resp = int(input('''Escolha entre as opções:
            [1] - Paulo
            [2] - Jose
            [3] - Aline
            [0] - Para sair  '''))

  if resp == 0 :
      break
  if resp in [1,2,3]:
    dic_votos[resp] = dic_votos.get(resp,0) + 1
    print('voto Registrado com sucesso.')
  else:
     print('Opção invalida! Tente novamente.\n')

print('Resultado da votação...')
for k , v in dic_votos.items():
   print(f'{k} -> {v} votos')
   print('FIM da votação')

# Criar um novo dicionário com as chaves trocadas
#disc_voto = {mapeamento_nomes[chave]: valor for chave, valor in dic_votos.items()}
disc_voto = {}
for chave, valor in dic_votos.items():
    nome = mapeamento_nomes[chave]
    disc_voto[nome] = valor

# Exibir o novo dicionário
print('REsultado votação ->',disc_voto)



'''
# Dicionário para armazenar os resultados da votação
resultados_votacao = {}

while True:
    print("Opções de voto:")
    print("1. Opção A")
    print("2. Opção B")
    print("3. Opção C")
    print("0. Encerrar votação")

    voto = input("Digite o número da sua opção (ou 0 para encerrar): ")

    # Verificar se o usuário deseja encerrar a votação
    if voto == '0':
        break

    # Verificar se a opção de voto é válida
    if voto in ['1', '2', '3']:
        # Atualizar os resultados da votação
        resultados_votacao[voto] = resultados_votacao.get(voto, 0) + 1
        print("Voto registrado com sucesso!\n")
    else:
        print("Opção de voto inválida. Tente novamente.\n")

# Exibir resultados finais da votação
print("\nResultados finais da votação:")
for opcao, votos in resultados_votacao.items():
    print(f"Opção {opcao}: {votos} votos")

print("Votação encerrada. Obrigado por participar!")
print(resultados_votacao)
'''
print('-='*25)
