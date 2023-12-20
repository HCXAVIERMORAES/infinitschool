# comando continue
var = 1
tentativas = 0
print('voce tem 3 tentativas')
while var != 5:
    var = int(input((' informe o numero 5 para sair: ')))
    tentativas += 1
    if tentativas == 3:
        print('Acabou a chance')
        continue

print('estamos fluindo')
