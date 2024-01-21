#revisão 14/01/2024
#criar lista
lista=[True, 12, False, 23.6, 'Otavio', [1,2,3,4,5]]
print(lista[2]) #mostrar o 3ª elemento da lista
for c in lista: #percorrer lista
    print(c)

#mostrar do 3ª elemento adiante
print(lista[2:])
#mostrar ate o 2ª elemento adiante
print(lista[:2]) 
#mostrar do segundo elemento até o ultimo
print(lista[2:-1])
print(lista[2:5])
#mostrar o ultimo elemento, que é uma lista o 3ª elemento
print(lista[5][2])
print(lista[-1][2])