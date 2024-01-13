'''Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.
1.Calcule a média das pontuações de cada equipe e armazene esses
valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente.
3.Crie uma nova lista chamada classificacao que contém tuplas, onde
cada tupla contém o nome da equipe e sua média de pontuações.
4.Exiba na tela a classificação final das equipes, mostrando o nome da
equipe e sua média, da equipe com a pontuação mais alta para a
mais baixa.'''
#lista gerada pelo site GPT
# Lista de tuplas representando os resultados das equipes
'''
resultados_equipes = [
    ("EquipeA", [10, 12, 15]),
    ("EquipeB", [8, 14, 18]),
    ("EquipeC", [11, 10, 12])
]
lista_medias = []
classificacao = ['EquipeA', [12.34],'EquipeB',[13.34],'EquipeC',[11.0]]
soma = 0
med = 0
for equipe, pontos in resultados_equipes:
  print(equipe)
  print(pontos)
  soma = pontos[0] + pontos[1] + pontos[2]
  med = soma/3
  lista_medias.append(med)


  #print('A soma dos pontos da {} è {}, com média {:.2f}'.format(equipe,soma,med))
  #itens = pontos
  #print(len(itens))

  for c in itens :
    x = itens.index(c)
    soma += itens[x]
    print(soma)
    med = soma/(len(itens))
    print('{:.2f}'.format(med))

  #print('os pontos são: ',itens)
print(lista_medias)
print('A soma dos pontos da {} è {}, com média {:.2f}'.format(equipe,soma,med))
lista_medias.reverse()
print('O inverso da lista de médias é: {}'.format(lista_medias))
# Exibindo os resultados na tela

print("Resultados da Competição:")
for equipe, pontuacoes in resultados_equipes:
    print(f"\nEquipe: {equipe}")
    print("Pontuações:")
    for rodada, pontuacao in enumerate(pontuacoes, start=1):
        print(f"Rodada {rodada}: {pontuacao} pontos")
'''
#solução para estudo
# Lista de tuplas representando os resultados das equipes
resultados_equipes = [
    ("EquipeA", [10, 12, 15]),
    ("EquipeB", [8, 14, 18]),
    ("EquipeC", [11, 10, 12])
]

# 1. Calcular a média das pontuações de cada equipe
medias = []
for equipe, pontuacoes in resultados_equipes:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append(media)

# 2. Ordenar a lista medias em ordem decrescente
medias.sort(reverse=True)

# 3. Criar a lista classificação com tuplas de nome da equipe e média
classificacao = []
for media, (equipe, _) in zip(medias, resultados_equipes):
    classificacao.append((equipe, media))

# 4. Exibir na tela a classificação final das equipes
print("Classificação Final:")
for posicao, (equipe, media) in enumerate(classificacao, start=1):
    print(f"{posicao}. {equipe}: {media:.2f} pontos")

