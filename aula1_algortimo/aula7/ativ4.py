'''ATIVIDADE PRÁTICA 4 Remova a fruta "cereja" do conjunto frutas_vermelhas e
imprima o conjunto atualizado'''
frutas_vermelhas = set(["morango", "cereja", "framboesa"])
for s in frutas_vermelhas:
  print('Mostra os elementod de frutas_vermelhas antes -> ',s)
print('--' * 15)
frutas_vermelhas.remove('cereja')

for s in frutas_vermelhas:
  print('Mostra os elementod de frutas_vermelhas apos -> ',s)
