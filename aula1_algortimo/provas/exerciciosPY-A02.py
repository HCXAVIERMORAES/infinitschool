''' Exercício de lista e tuplas
[PY-A02]
A) Qual das alternativas abaixo apresenta a forma correta de adicionar um elemento ao final de uma lista em Python?
B) Qual das alternativas abaixo apresenta a forma correta de criar uma lista vazia em Python?
C) Qual das alternativas abaixo apresenta a forma correta de obter o comprimento (número de elementos) de uma lista em Python?'''
lista = [] #->B
lista.append('elemento') #->A
lista.append('elemento2')
print(lista)
print(len(lista)) #-> C
'''Explicação perg A
  A resposta correta é a opção b) lista.append(elemento)
Porque o método append() é utilizado em listas em Python para adicionar um elemento ao final da lista. Ao chamar lista.append(elemento), o elemento é inserido no final da lista, aumentando o seu tamanho em uma unidade.
As outras opções não estão corretas:
a) lista.add(elemento) não é uma sintaxe válida em Python para adicionar elementos a uma lista.
c) lista.insert(elemento) é utilizado para inserir um elemento em uma posição específica da lista, mas requer que seja especificada a posição onde o elemento será inserido.
d) lista.extend(elemento) é usado para estender uma lista com os elementos de outra lista ou de um iterável, mas não para adicionar um único elemento.
e) lista.push(elemento) não é um método existente em listas em Python.
Explicação perg.B
A resposta correta é a opção b) len(lista).
Porque len() é uma função embutida em Python que retorna o comprimento (número de elementos) de uma lista. Ao chamar len(lista), você obterá o tamanho da lista, ou seja, a quantidade de elementos presentes nela.
As outras opções não estão corretas:
a) lista.size() não é uma sintaxe válida em Python para obter o comprimento de uma lista.
c) lista.length() não é uma sintaxe válida em Python para obter o comprimento de uma lista.
d) lista.count() é usado para contar o número de ocorrências de um elemento específico em uma lista, não para obter o comprimento da lista.
e) length(lista) não é uma função embutida em Python para obter o comprimento de uma lista.
Explicação perg.C
A resposta correta é a opção a) lista = [].
Porque é a forma correta e mais comum de criar uma lista vazia em Python. Ao utilizar lista = [], você está criando uma lista vazia, sem nenhum elemento dentro dela.
As outras opções não estão corretas:
b) lista = {} cria um dicionário vazio, não uma lista vazia
c) lista = () cria uma tupla vazia, não uma lista vazia.
d) lista = [None] cria uma lista com um elemento, o valor None, não uma lista vazia.
e) lista = "lista" cria uma variável de tipo string, não uma lista vazia.
'''
#[PY-A02] exercicios complementares
#A
produtos = ("Leite", "Batata", "Cereal", "Tomate", "Biscoito")
for dados in produtos:
    print(dados)

#B
produtos = ("Leite", "Batata", "Cereal", "Tomate", "Biscoito")
for dados in produtos:
    print(dados)

'''Explicação pergunta A
  Resposta correta: a) A diferença entre os dois é que não podemos alterar os elementos de uma tupla depois de atribuída, enquanto podemos alterar os elementos de uma lista.
As outras opções estão incorretas:
b) "Tanto a tupla quanto a lista são estruturas de dados imutáveis e ordenadas." Essa afirmação é incorreta, pois listas são estruturas de dados mutáveis, ao contrário das tuplas.
c) "A tupla é uma estrutura de dados mutável e desordenada, enquanto a lista é uma estrutura de dados imutável e ordenada." Essa afirmação é incorreta, pois inverte os conceitos de mutabilidade e ordenação para tuplas e listas.
d) "Tanto a tupla quanto a lista são estruturas de dados mutáveis, mas a tupla é ordenada e a lista é desordenada." Essa afirmação é incorreta, pois as listas são mutáveis e podem ser ordenadas.
e) "A tupla é uma estrutura de controle utilizada para realizar iterações em um loop, enquanto a lista é uma estrutura de dados imutável e ordenada." Essa afirmação é incorreta, pois não descreve adequadamente as características de tuplas e listas.

Perg. B
Resposta correta: a) Leite
Batata
Cereal
Tomate
Biscoito
  Explicação: O código utiliza um loop for para iterar sobre os elementos da tupla "produtos". Em cada iteração, o valor do elemento é armazenado na variável "dados" e é exibido com o comando print(dados). Portanto, a saída será cada elemento da tupla em uma linha separada.

  Perg.C - Qual das alternativas abaixo descreve de forma clara a diferença entre tupla e lista em Python?

  Resposta correta: a) A diferença entre os dois é que não podemos alterar os elementos de uma tupla depois de atribuída, enquanto podemos alterar os elementos de uma lista.
As outras opções estão incorretas:
b) "Tanto a tupla quanto a lista são estruturas de dados imutáveis e ordenadas." Essa afirmação é incorreta, pois listas são estruturas de dados mutáveis, ao contrário das tuplas.
c) "A tupla é uma estrutura de dados mutável e desordenada, enquanto a lista é uma estrutura de dados imutável e ordenada." Essa afirmação é incorreta, pois inverte os conceitos de mutabilidade e ordenação para tuplas e listas.
d) "Tanto a tupla quanto a lista são estruturas de dados mutáveis, mas a tupla é ordenada e a lista é desordenada." Essa afirmação é incorreta, pois as listas são mutáveis e podem ser ordenadas.
e) "A tupla é uma estrutura de controle utilizada para realizar iterações em um loop, enquanto a lista é uma estrutura de dados imutável e ordenada." Essa afirmação é incorreta, pois não descreve adequadamente as características de tuplas e listas.
'''
