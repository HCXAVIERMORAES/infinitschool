#lista é um tipo de dado que pode receber outros tipos de dado
'''
lista1 = [1,2,3,4,5,True,12.5,'Jose',[1,2,3,4]]
print(type(lista1))
print(lista1)
#Mostrando elementos dentro da lista
for x in lista1:
    print(x)

lista2 = [12,23,45,12,45,12,67]
for x in lista2:
    if x < 18:
        print(x)
        print('para idade {} não pode entra'.format(x))
    else:
        print(x)
        print('para idade {} pode entra'.format(x))
print('fim lista2')   

lista2 = [12,23,45,12,45,12,67]
#posiçõ: [0, 1 ,2 ,3 ,4 ,5 , 6]
print(lista2[2])
#nome_lista[posição]

#O aluno tem as seguintes notas [10,7.9,3] qual a média e caso ele tenha maior que 7 passou
nota = [10,7.9,3]
media = nota[0] + nota[1] + nota[2]/3
if media > 7:
    print('A media é {} ele passou'.format(media))
else:
    print('A media é {} ele não passou'.format(media))
   
lista = [1,2,3,4,343,325,355,583,54,33,8887,7]
print(len(lista))
var = int(input('Informe o valor '))
lista.append(var) #insere elemento no ultimo elemento da lista
print(len(lista)) #mostra o comprimento da lista
print(lista)

lista4 = ['otabio','bernado','davi', 'gabriel']
print(lista4[-1])
lista5 = [1,2,3,4,5]
lista5.remove(4) #remove o numero 4 da lista
lista5.pop(0) #remove o elemento na posição 0, ou seja o numero 1
print(lista5)
lista5.insert(6,74)
print(lista5)

#lista com lista
listao = [[1,2,3],[4,5,6],[7,8,9]]
for listinha in listao:
    print(listinha)
    for elemento in listinha :
        print(elemento)
print('fim listão')
'''
#quando se tem elemento fora de uma lista usa-se um teste para ver se é do tipo (type) list (lista)
listao = [1,[4,5,6],[7,8,9]]
for listinha in listao:
    if type(listinha) == list:
        print(listinha)
        for elemento in listinha :
            print(elemento)
    else:
        print(listinha)
print('fim listão')