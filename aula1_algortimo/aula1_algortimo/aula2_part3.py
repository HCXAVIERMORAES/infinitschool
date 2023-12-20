usuario = 'otavio'
senha = '1234'

usuario_valor = input('Informw o user: ')
senha_valor = input('Informw a senha: ')
#sem operadores logicos
'''
if usuario_valor == usuario:
    print('Entrou')
else:
    print('não entrou')
'''
if usuario_valor == usuario and senha_valor == senha:
     print('Entrou')
     print('Seja Bem vindo')
else:
    print('não entrou')
    
print('Ola Mundo')
print('Ola mundo, é mostrado na tela pois esta fora do bloco de condição')
