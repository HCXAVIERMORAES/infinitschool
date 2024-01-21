'''Sets e suas caracteristicas: não repetir elemento em sets pois ele não é repetido, não tem posições em set'''
meu_set = {'Infinty','School'} #criação
print(type(meu_set))

#criação -> para
'''Após a criação de um Set, você não pode alterar seus itens. Contudo você
pode adicionar novos itens e para isso podemos utilizar o método add().'''
convidados = {'joão','Maria','Eduarda'}
print('Set antes de adiconar Marcel -> ',convidados)
convidados.add('Marcela')
print('Depois do metodo .add("Marcela")',convidados)

var = {letra for letra in 'otavio' if letra not in 'aeiou'}
print("Uma variavel criada assim -> {letra for letra in 'otavio' if letra not in 'aeiou'} retorna os valores: ",var)
for letra in 'otavio':
    print(letra)

'''Para adicionar itens de outro conjunto ao set especificado, podemos
utilizar o método update().  Você pode utilizar esse método com qualquer
tipo de objeto iterável (tuplas, listas, dicionários etc.)'''
ids = {10, 12, 13, 14}
novos_ids = {11,13, 15}
ids.update(novos_ids)
print('Retorna os ids sem aqueles repetidos-> ',ids)

'''sets não possibilitam acessar seus elementos através de índices
(assim como Listas) ou chaves (como os Dicionários).
Assim, podemos acessá-los de duas maneiras: percorrendo o
conjunto ou verificando se o elemento desejado se encontra no set.
set_1 = {1, 2, 3}
print(set_1[0]) #gera um erro
'''
'''Para remover itens de um set, você pode, inicialmente, utilizar dois
métodos: o remove() e discard().'''
convidados = {'joão','Maria','Eduarda'}
print(convidados.remove('Maria'))
print(convidados.discard('Eduarda'))
print(convidados,'-> foi o que sobrou apos convidados.remove("Maria") e \n'
      'convidados.discard("Eduarda")')

'''Os Sets em Python nada mais são que Conjuntos Matemáticos. Neles, você
também pode aplicar os conceitos de Interseção, União, Diferença e etc.
Intersection()
O método intersection() retorna um novo conjunto contendo
apenas os itens presentes em ambos'''
convidados = {'joão','Maria','Eduarda'}
convidados2 = {'Pedro','Maria','Raama'}
print('Convidado(s) presente nas 2 listas (set)',convidados.intersection(convidados2))
'''ntersection_update()
Para atualizar um dos sets com a interseção entre eles, use o método intersection_update()'''
convidados.intersection_update(convidados2)
print('Retorno do metodo .intersection_update() ->',convidados)

'''union()
Você pode utilizar o método union() para retornar um conjunto de elementos contendo
elemento de ambos sets:'''
set1 = {1,2,3}
set2 = {'z','x','a'}
#print(set1.union(set2)) # metodo 1
print(set1 | set2) # metodo 2

#criar um set e percorrer
set = {'joão','Maria','Carla'}
for x in set:
    print(x)
print('Retorna','Maria' in set) # retorna True
