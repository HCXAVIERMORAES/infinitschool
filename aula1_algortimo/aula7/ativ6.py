''''ATIVIDADE PRÁTICA 6 Crie um programa que recebe dois conjuntos e exibe a
interseção deles.'''
conj_a =  set([])
conj_b =  set([])
sair = ''
conj2 = ''
interar = 1
interar2 = 1
while sair in 'Ss':
  while conj2 in 'Ss':
    a = str(input(f'Informe {interar}ª elemento do 1ªconj.:'))
    conj_a.update(a)
    interar += 1
    conj2 = input('Desenja continuar no conjunto 1 [S/N]')

  while sair in 'Ss':
    a = str(input(f'Informe {interar2}ª elemento do 2ªconj.:'))
    conj_b.add(a)
    interar2 += 1
    sair = input('Desenja continuar [S/N]')

print('Conjunto A ->',conj_a)
print('Conjunto B ->',conj_b)
print(f'A interceção entre os conjuntos A -> {conj_a}\ne conjunto B -> {conj_b}\né { conj_a.intersection(conj_b)}')
