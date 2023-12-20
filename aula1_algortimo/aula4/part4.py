#comamdo break
'''
i = 0
while i <= 8:
    print(i)
    i += 1
    if i == 3:
        print('é o numero 3.')
        break
print('saiu')
'''
var = 1
tentativas = 0
print('voce tem 3 tentaivas')
while var != 5:
    var = int(input((' informe um numero diferente de 5: ')))
    tentativas += 1
    if tentativas == 3:
        print('Acabou a chance')
        break

print('Saiu')