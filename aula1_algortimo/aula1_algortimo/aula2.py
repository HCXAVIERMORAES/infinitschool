#revisão
# trransforma dados

valor = 1
#print(type (valor))
#print(type(valor))
#print(valor)
#print(f'{valor:.3f}')
''' '''
'''
print(type(valor))
valor = str(valor)
print(type(valor))

valor2 = input('informe um valor.: ')
print(type(valor2))
'''
'''
valor = 'true'
print(type (valor))
valor = bool(valor)
print(type(valor))
'''
'''
valor1 =47
valor2 =3

print(valor1 % valor2)
print(valor1 // valor2)
'''
#operadores relacionai- é utilizados pra verificar resultados
home_office = True
loc = 'Teresina'
'''
print(home_office == True)
print(loc == 'Teresina' )
'''
# ou com condiciona and (se ambos forem verdade)
print(home_office == True and loc == 'Teresina')
print(f"{home_office == True} {loc == 'Teresina'}")

#Or -> ou uma deve ser verdadeiro
print(home_office == True or loc == 'Teresina')

#NOT -não nega uma condição
login = 'helton'
senha = '1234'

loginsite = input('login: ')
senhasite = input('senha: ')

print(login == loginsite and senha == senhasite)
print('voce entrou')

#condicionais (if/elif/else)
