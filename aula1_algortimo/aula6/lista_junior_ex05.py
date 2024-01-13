'''5)Crie uma lista e com 3 elementos do tipo string e mude o 2 elemento para a palavra 'uva'
mostre a lista antes e depois'''
lista = ['a','paula','rato']
print('lista inicial: ', lista)
lista.remove('paula')
print('removendo Paula da lista: ',lista)
lista.insert(2,'uva')
print('adicionando uva na lista: ',lista)
