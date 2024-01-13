'''7)Com a lista do exercício anterior insira um novo argumento na posição 1'''
lista6 = []
print('exercício 6')
lista6.append(1)
print('1ª elemento posto', lista6)
lista6.append('louco')
print('2ª elemento posto', lista6)
lista6.append(1.85)
print('3ª elemento posto', lista6)
print('exercício 7')
lista6[0] = 'novo'
print('modo1 utilizado -> lista6[0]',lista6)
lista6.insert(0,'novo1')
print('modo2 utilizado -> lista6.insert(0,"novo1")',lista6)
