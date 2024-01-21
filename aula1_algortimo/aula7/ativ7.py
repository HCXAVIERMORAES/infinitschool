'''ATIVIDADE PRÁTICA 7 Escreva um programa que receba duas listas e calcule
a união dos elementos únicos dessas listas, usando conjuntos.'''
lista1 = [4, 5, 9, 10]
lista2 = [4, 5, 'abobora', 'pera']
listauni = []
setlista1 = set([])
setlista2 = set([])

for s in lista1:
  setlista1.add(s)
print(f'set da lista1 ->{setlista1}')

for s in lista2:
  setlista2.add(s)
print(f'set da lista1 ->{setlista2}')

listauni.append(setlista1.intersection(setlista2))
print('A lista da união dos elementos únicos é -> ', listauni)
