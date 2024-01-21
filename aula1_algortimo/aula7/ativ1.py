'''Crie um conjunto vazio chamado frutas e adicione as
seguintes frutas a ele:, "banana", "uva", "laranja" e "morango". Em seguida, imprima o conjunto.'''

frutas = set([]) #criando set vazio
print(type(frutas))

lista_frutas = ["banana", "uva", "laranja", "morango"]
for x in lista_frutas:
    #frutas.add(x) #1ª modo
    frutas.update(lista_frutas) #2ª modo
print(frutas)