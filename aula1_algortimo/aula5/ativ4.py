'''Crie um programa que receba o preço de um produto e a quantidade e mostre o valor total da compra.
(Base de cálculo: total=preco * quantidade)'''
print('Calculo de venda')
venda = float(input('digite valor unitario do produto: R$'))
qtd = int(input('Digite a quantidade do produto: '))
total = venda*qtd
print(f'O valor da venda é: R${total:.2f}')