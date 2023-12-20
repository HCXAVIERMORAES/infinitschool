'''Calcule a área de um lote quadeado, onde o usuario somente envia o lado deste lote. Se 
a área for maior que 1000 metros, o preço por metro quadrado vai ser R$250,00. se for menor vai ser R$150.00'''
print('informe o lado do lote para saber o valor')
lado = float(input('Digite o lado: '))
area = lado*lado
preco = None
if area > 1000 :
    preco = area * 250
elif area < 1000 :
    preco = area * 150
print(f'O valor do lote é R${preco}')