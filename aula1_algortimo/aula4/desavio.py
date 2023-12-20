''''''''''
import random 

clientes =''
venda =''
nome = ''
telefone= ''
def Cadastro_cliente (nome, endereco, tel):
    clientes.append({
          "venda" : venda,
          "nome" : nome,
          "telefone" : telefone })

def sorteio_client():
    return  clientes[random.randint(0,len(clientes))]

end = '''

#lista = [['otavio', 3333,  'rua'],['ruan', 4444,  'rua2'],[]]
lista = [[],[],[]]
'''
print(lista[0][0])
print(lista[1])
lista.append(['nome', 'tel', 'end'])
print(lista)
'''
lista.append[0] = input("Digite nome do cliente: ")
print(lista[0])

