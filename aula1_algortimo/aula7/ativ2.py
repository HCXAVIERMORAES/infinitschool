'''ATIVIDADE PRÁTICA 2 - Verifique se a fruta "banana" está presente no conjunto
frutas e imprima o resultado'''
frutas = set(["banana", "uva", "laranja", "morango"])
print(type(frutas))

print('Mostra se esta presente(True ou False)-> {} '.format('banana' in frutas))
for s in frutas:
  print('Mostra os elementod de frutas -> ',s)
